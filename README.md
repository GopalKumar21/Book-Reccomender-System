# Book Recommender System

## Overview
This is a web-based book recommender system built using Python and Flask, leveraging a collaborative filtering algorithm to provide personalized book recommendations. Users can browse a curated list of the top 50 books, search for books by title, and get recommendations for similar books based on precomputed similarity scores. The data processing and machine learning model were developed using Jupyter Notebooks, with raw data sourced from Excel files and processed into pickle files for the application.

## Features
- **Browse Top 50 Books**: View a curated list of popular books with titles, authors, ratings, vote counts, and cover images.
- **Search Books**: Perform a case-insensitive search for books by title, displaying matching results with title, author, and image.
- **Personalized Recommendations**: Enter a book title to receive up to 8 similar book recommendations based on a collaborative filtering model.
- **About Page**: Learn about the application's features and purpose.
- **Responsive Interface**: Built with Flask templates and styled with Bootstrap (assumed, not explicitly included).

## Technologies Used
- Python 3.x
- Flask (web framework)
- NumPy (for data processing)
- Jupyter Notebook (for data preprocessing and machine learning model building)
- Pickle (for loading precomputed data)
- HTML, Jinja2 (for templating)
- Bootstrap (assumed for frontend styling, not explicitly included)
- JavaScript (minimal, for form handling)

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Jupyter Notebook (for data preprocessing and model building, if regenerating pickle files)
- A web browser (e.g., Chrome, Firefox)
- A tool to extract `.7z` files (e.g., 7-Zip)



## Usage
- **Home Page**: Browse the top 50 books or use the search bar to find books by title. Search results display the book title, author, and cover image.
- **Find Similar Titles**: Navigate to the "Find" page, enter a book title, and get up to 8 recommended books based on collaborative filtering.
- **About Page**: Explore the application's features and purpose.
- **Navigation**: Use the navigation bar to switch between Home, Find, and About pages.

## Data Preprocessing and Model Building
The application relies on precomputed data stored in pickle files, generated using Jupyter Notebooks. The process involves:
1. **Raw Data**: The original dataset is stored in three Excel files (in `Excel Files.7z`), likely containing book metadata (titles, authors, image URLs) and user ratings.
2. **Preprocessing**:
   - Use a Jupyter Notebook to read the Excel files (using `pandas`).
   - Clean and transform the data to create:
     - `popular.pkl`: Top 50 books based on ratings and vote counts.
     - `books.pkl`: Full book dataset with `Book-Title`, `Book-Author`, and `Image-URL-M`.
     - `pt.pkl`: A pivot table of user-book ratings for collaborative filtering.
   - Compute `similarityscore.pkl` using a collaborative filtering algorithm (e.g., cosine similarity) on the pivot table.
3. **Output**: Save the processed data as pickle files in the project root (included in `Derived Files.7z`).
**Note**: The preprocessing notebook is not included in the repository. Contact the repository owner for details on the data processing and model-building script.

## Project Structure
```plaintext
├── app.py                    # Main Flask application
├── templates/                # HTML templates
│   ├── index.html            # Home page with top 50 books and search
│   ├── recommend.html        # Recommendation page
│   ├── about.html            # About page
├── Excel Files.7z            # Compressed original Excel files (raw data)
├── Derived Files.7z          # Compressed derived pickle files
├── popular.pkl               # Top 50 books data (after extracting Derived Files.7z)
├── books.pkl                 # Full book dataset
├── pt.pkl                    # Pivot table for recommendations
├── similarityscore.pkl       # Precomputed similarity scores
├── README.md                 # This file
```

## Data Files
The application relies on four pickle files (included in `Derived Files.7z`):
- `popular.pkl`: Contains `Book-Title`, `Book-Author`, `Image-URL-M`, `Num-Ratings`, and `avg_rating` for top 50 books.
- `books.pkl`: Contains `Book-Title`, `Book-Author`, `Image-URL-M` for a larger book dataset.
- `pt.pkl`: A pivot table (likely user-book ratings) with book titles as the index.
- `similarityscore.pkl`: Precomputed similarity scores for collaborative filtering.

The raw data is provided in `Excel Files.7z`, containing three Excel files with book metadata and user ratings. These are processed in Jupyter to generate the pickle files.

## Known Issues
- The `about.html` template has incomplete HTML structure (missing `<html>`, `<head>`, `<body>` tags). Consider fixing it for proper rendering.
- The application assumes Bootstrap is available but does not include a CDN link in the templates. Add Bootstrap CSS/JavaScript for proper styling, e.g.:
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```
- No error handling for missing pickle files or invalid data formats. Consider adding checks in `app.py`.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows Python PEP 8 standards and test thoroughly.


## Contact
For questions or feedback, feel free to reach out:
- GitHub: [GopalKumar21](https://github.com/GopalKumar21)
- Email: [gopalkumar172111@gmail.com](mailto:gopalkumar172111@gmail.com)
