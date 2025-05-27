from flask import Flask, render_template, request
import numpy as np
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarityscore = pickle.load(open('similarityscore.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get('search_query', '').strip().lower() if request.method == 'POST' else None

    search_results = None
    search_performed = False
    
    if search_query:
        search_performed = True
        results = books[books['Book-Title'].str.lower().str.contains(search_query, na=False)]
        search_results = []
        for _, row in results.iterrows():
            search_results.append({
                'title': row['Book-Title'],
                'author': row['Book-Author'],
                'image': row['Image-URL-M']
            })

    return render_template(
        'index.html',
        bookname=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        images=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['Num-Ratings'].values),
        ratings=list(popular_df['avg_rating'].values),
        search_results=search_results,
        search_performed=search_performed 
    )

@app.route('/Find')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('User_Input')
    user_input = user_input.strip().lower()
    normalized_index = pt.index.str.strip().str.lower()

    search_performed = True
    data = None

    if user_input not in normalized_index.values:
        return render_template('recommend.html', data=None, message="No results found. Please try another title.", search_performed=search_performed)

    index = np.where(normalized_index == user_input)[0][0]

    similar_items = sorted(list(enumerate(similarityscore[index])), key=lambda x: x[1], reverse=True)[0:8]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        data.append([
            temp_df['Book-Title'].values[0],
            temp_df['Book-Author'].values[0],
            temp_df['Image-URL-M'].values[0]
        ])

    return render_template('recommend.html', data=data, message=None, search_performed=search_performed)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
