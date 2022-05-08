# movie-imdb
IMDB Dataset of top 100 movies and tv shows.

## movie data table
| Series_Title | IMDB_ID | Released_Year | Runtime | Genre | Overview | Director | Star1 | Star2 | Star3 | Star4 | Gross |
|--------------|---------|---------------|---------|-------|----------|----------|-------|-------|-------|-------|-------|

1. Series_Title - Name of the movie
2. IMDB_ID - ID of IMDB
3. Released_Year - Year at which that movie released
4. Runtime - Total runtime of the movie
5. Genre - Genre of the movie
6. Overview - mini story/ summar
7. Director - Name of the Director
8. Star1,Star2,Star3,Star4 - Name of the Stars
9. Gross - Money earned by that movie

## imdb data table
| IMDB_ID | IMDB_Rating | Meta_score | No_of_Votes | Certificate | Poster_Link |
|---------|-------------|------------|-------------|-------------|-------------|

1. IMDB_ID - ID of IMDB
2. IMDB_Rating - Rating of the movie at IMDB site
3. Meta_score - Score earned by the movie
4. No_of_votes - Total number of votes
5. Certificate - Certificate earned by that movie
6. Poster_Link - Link of the poster that imdb using

# How to import data from csv file into database

        # create the database using specified schema
        sqlite3 top_100_movie.db -init top_100_movie.schema    

        # import data from csv files
        sqlite3> .mode csv
        sqlite3> .import --skip 1 data/top_100_imdb_data.csv IMDB
        sqlite3> .import --skip 1 data/top_100_movie_data.csv movie
        
# UML Class Diagram
[UML](../../wiki/uml-class-diagram)

# Package Diagram
[Package Diagram](../../wiki/package-diagram)

# API 
[API documentation](https://docs.google.com/document/d/1-Fz8Sp7Q4I1MeDKUyzjogXSRpLQ_BZGmHuK2lsHeEXQ/edit?usp=sharing)
