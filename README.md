# Book Recommender System

## Overview
This is a web-based book recommender system built using Python and Flask. It allows users to browse a curated list of top 50 books, search for books by title, and get personalized book recommendations based on a collaborative filtering algorithm. The application provides a simple, user-friendly interface to explore books by title, author, and cover image.

## Features
- **Browse Top 50 Books**: View a list of popular books with titles, authors, ratings, and vote counts.
- **Search Books**: Search for books by title with a case-insensitive partial match.
- **Personalized Recommendations**: Enter a book title to get up to 8 similar book recommendations based on precomputed similarity scores.
- **About Page**: Learn about the application's features and purpose.
- **Responsive Interface**: Built with Flask templates and styled with Bootstrap (assumed).

## Technologies Used
- Python 3.x
- Flask (web framework)
- NumPy (for data processing)
- Pickle (for loading precomputed data)
- HTML, Jinja2 (for templating)
- Bootstrap (assumed for frontend styling, not explicitly included)
- JavaScript (minimal, for form handling)

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- A web browser (e.g., Chrome, Firefox)

## Usage
- **Home Page**: Browse the top 50 books or use the search bar to find books by title. Search results display the book title, author, and cover image.
- **Find Similar Titles**: Go to the "Find" page, enter a book title, and get up to 8 recommended books based on collaborative filtering.
- **About Page**: Learn about the application's features and explore its capabilities.
- **Navigation**: Use the navigation bar to switch between Home, Find, and About pages.

## Project Structure
```plaintext
├── app.py                    # Main Flask application
├── templates/                # HTML templates
│   ├── index.html            # Home page with top 50 books and search
│   ├── recommend.html        # Recommendation page
│   ├── about.html            # About page
├── popular.pkl               # Top 50 books data
├── books.pkl                 # Full book dataset
├── pt.pkl                    # Pivot table for recommendations
├── similarityscore.pkl       # Precomputed similarity scores
├── README.md                 # This file
```

## Data Files
The application relies on four pickle files:
- `popular.pkl`: Contains `Book-Title`, `Book-Author`, `Image-URL-M`, `Num-Ratings`, and `avg_rating` for top 50 books.
- `books.pkl`: Contains `Book-Title`, `Book-Author`, `Image-URL-M` for a larger book dataset.
- `pt.pkl`: A pivot table (likely user-book ratings) with book titles as the index.
- `similarityscore.pkl`: Precomputed similarity scores for collaborative filtering.

**Note**: These files are provided in the compressed format.Excel Files.7z contain orginal 3 excel files which is then later used to create files in Derived Files.7z which are then used in the main program.

## Known Issues
- The `about.html` template has incomplete HTML structure (missing `<html>`, `<head>`, `<body>` tags). Consider fixing it for proper rendering.
- The application assumes Bootstrap is available but does not include a CDN link in the templates. Add Bootstrap CSS/JavaScript for proper styling.
- No error handling for missing pickle files or invalid data formats.

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
