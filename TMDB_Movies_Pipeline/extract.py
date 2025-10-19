import pandas as pd

def extract_data():
    # Define file paths
    movies_path = "data/raw/tmdb_5000_movies.csv"
    credits_path = "data/raw/tmdb_5000_credits.csv"
    
    # Read CSV files
    movies_df = pd.read_csv(movies_path)
    credits_df = pd.read_csv(credits_path)
    
    print(f"Movies data shape: {movies_df.shape}")
    print(f"Credits data shape: {credits_df.shape}")
    
    return movies_df, credits_df
