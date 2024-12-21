import pandas as pd
import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    'dbname': 'NetflixShows',
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 5432,
}

def connect_to_db():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def process_and_insert_data(csv_path):
    data = pd.read_csv(csv_path)
    data.fillna('', inplace=True)

    conn = connect_to_db()
    cur = conn.cursor()
    try:

        for _, row in data.iterrows():
            cur.execute("""
                INSERT INTO Show (title, type, release_year, description)
                VALUES (%s, %s, %s, %s)
                RETURNING show_id;
            """, (row['title'], row['type'], row['release_year'], row['description']))
            show_id = cur.fetchone()[0]
            
            directors = [d.strip() for d in row['director'].split(',') if d]
            for director in directors:
                cur.execute("""
                    INSERT INTO Director (name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                    RETURNING director_id;
                """, (director,))
                director_id = cur.fetchone()
                if director_id:
                    cur.execute("""
                        INSERT INTO Show_Director (show_id, director_id)
                        VALUES (%s, %s);
                    """, (show_id, director_id[0]))
            
            cast_members = [c.strip() for c in row['cast'].split(',') if c]
            for cast_member in cast_members:
                cur.execute("""
                    INSERT INTO Cast (name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                    RETURNING cast_id;
                """, (cast_member,))
                cast_id = cur.fetchone()
                if cast_id:
                    cur.execute("""
                        INSERT INTO Show_Cast (show_id, cast_id)
                        VALUES (%s, %s);
                    """, (show_id, cast_id[0]))
            countries = [country.strip() for country in row['country'].split(',') if country]
            for country in countries:
                cur.execute("""
                    INSERT INTO Country (name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                    RETURNING country_id;
                """, (country,))
                country_id = cur.fetchone()
                if country_id:
                    cur.execute("""
                        INSERT INTO Show_Country (show_id, country_id)
                        VALUES (%s, %s);
                    """, (show_id, country_id[0]))
                    
            genres = [genre.strip() for genre in row['listed_in'].split(',') if genre]
            for genre in genres:
                cur.execute("""
                    INSERT INTO Genre (name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                    RETURNING genre_id;
                """, (genre,))
                genre_id = cur.fetchone()
                if genre_id:
                    cur.execute("""
                        INSERT INTO Show_Genre (show_id, genre_id)
                        VALUES (%s, %s);
                    """, (show_id, genre_id[0]))
            cur.execute("""
                INSERT INTO Show_Metadata (show_id, date_added, rating, duration)
                VALUES (%s, %s, %s, %s);
            """, (show_id, row['date_added'], row['rating'], row['duration']))

        conn.commit()
        print("Data inserted successfully!")

    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cur.close()
        conn.close()

file_path = 'Day2 Design and Implement DB and interacting with Python Libraries/netflix_titles.csv'
process_and_insert_data(file_path)
