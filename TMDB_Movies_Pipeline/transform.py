import pandas as pd
import ast

def transform_data(movies_df, credits_df):
    # Rename column for merging
    credits_df.rename(columns={'movie_id': 'id'}, inplace=True)
    
    # Merge movies and credits datasets
    df = movies_df.merge(credits_df, on='id')
    
    # Helper function to extract director name
    def get_director(crew_list):
        try:
            crew = ast.literal_eval(crew_list)
            for c in crew:
                if c['job'] == 'Director':
                    return c['name']
        except:
            return None

    # Helper function to extract top 3 cast members
    def get_top_cast(cast_list):
        try:
            cast = ast.literal_eval(cast_list)
            names = [c['name'] for c in cast[:3]]
            return ", ".join(names)
        except:
            return None

    # Create new columns
    df['director'] = df['crew'].apply(get_director)
    df['main_cast'] = df['cast'].apply(get_top_cast)

    # Select useful columns
    df = df[['title', 'release_date', 'budget', 'revenue', 'runtime', 
             'vote_average', 'vote_count', 'director', 'main_cast', 'genres']]
    
    # Remove missing titles or release dates
    df.dropna(subset=['title', 'release_date'], inplace=True)
    
    print(f"Transformed data shape: {df.shape}")
    return df
