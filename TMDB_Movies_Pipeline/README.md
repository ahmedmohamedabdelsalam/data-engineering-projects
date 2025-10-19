# TMDB Movies Data Engineering Pipeline

## Project Overview
This project demonstrates a simple **Data Engineering pipeline** using Python and SQLite with movie data from TMDB (The Movie Database).  
The pipeline loads, cleans, transforms, and stores data from two TMDB datasets into a SQLite database.

## Project Objectives
1. Load two datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
2. Clean and transform the data
3. Merge the datasets into a unified structure
4. Load the processed data into a SQLite database (`movies.db`)
5. Ensure the pipeline is modular, reusable, and production-ready

## Tech Stack
- **Python 3.13+**
- **Pandas**
- **SQLite**
- **OS / Logging** for file and process management

## Project Structure


tmdb_movies_pipeline/
│
├── main.py # Main pipeline script
├── process_data.py # Data cleaning and transformation logic
├── load_data.py # Handles loading of CSV files
├── database.py # Handles database creation and insertion
├── requirements.txt # Required dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files and folders
└── tmdb_5000_movies.csv # Dataset 1 (from Kaggle)
└── tmdb_5000_credits.csv # Dataset 2 (from Kaggle)


## How to Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/ahmedmohamedabdelsalam/tmdb_movies_pipeline.git
cd tmdb_movies_pipeline

Step 2: Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Place the datasets

Download the following two CSV files from Kaggle and place them inside your project folder:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

Step 5: Run the pipeline
python main.py

Step 6: Check the database

After running the pipeline, a database file named movies.db will be created in your project folder.
You can open it using DB Browser for SQLite or any database viewer.

Expected Output

A clean and merged dataset stored in movies.db

Log messages in the terminal confirming successful load, transform, and insert operations

Reusable and modular code ready for scaling or cloud deployment

Dataset

The dataset is publicly available on Kaggle:
🔗 TMDB 5000 Movie Dataset

Author

Ahmed Mohamed Abdelsalam
AI and Data Engineer

 Cairo, Egypt
 ahmedabdelsalam.300200@gmail.com

 LinkedIn

 GitHub

License

This project is licensed under the MIT License – you are free to use, modify, and distribute it.
