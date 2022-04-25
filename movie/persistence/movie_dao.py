import movie.model as model
from movie.persistence.dao import Dao
from sqlalchemy import select, update

class MovieDao(Dao):

    def get_all(self):
        stm = select(model.Movie)
        result = self.session.execute(stm).fetchall()
        return result

    def get_title(self):
        stm = select(model.Movie.series_title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_imdb_id(self):
        stm = select(model.Movie.imdb_id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_released_year(self):
        stm = select(model.Movie.release_year)
        result = self.session.execute(stm).fetchall()
        return result

    def get_runtime(self):
        stm = select(model.Movie.runtime)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_genre(self):
        stm = select(model.Movie.genre)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_overview(self):
        stm = select(model.Movie.overview)
        result = self.session.execute(stm).fetchall()
        return result

    def get_director(self):
        stm = select(model.Movie.director)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_star1(self):
        stm = select(model.Movie.star1)
        result = self.session.execute(stm).fetchall()
        return result

    def get_star2(self):
        stm = select(model.Movie.star2)
        result = self.session.execute(stm).fetchall()
        return result

    def get_star3(self):
        stm = select(model.Movie.star3)
        result = self.session.execute(stm).fetchall()
        return result

    def get_star4(self):
        stm = select(model.Movie.star4)
        result = self.session.execute(stm).fetchall()
        return result

    def get_gross(self):
        stm = select(model.Movie.gross)
        result = self.session.execute(stm).fetchall()
        return result

    def get_form_title(self, title):
        title = title.title()
        stm = select(model.Movie).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_title_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.series_title).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_imdb_id_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.imdb_id).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_released_year_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.release_year).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_runtime_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.runtime).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_genre_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.genre).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_overview_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.overview).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_director_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.director).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_star1_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.star1).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_star2_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.star2).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_star3_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.star3).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_star4_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.star4).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_gross_form_title(self, title):
        title = title.title()
        stm = select(model.Movie.gross).where(model.Movie.series_title == title)
        result = self.session.execute(stm).fetchall()
        return result

    def get_from_year(self, year):
        title = title.title()
        stm = select(model.Movie).where(model.Movie.release_year > year)
        result = self.session.execute(stm).fetchall()
        return result
    
    def update_movie(self, title, imdb_id, year, time, genre, overview, director, star1, star2, star3, star4, gross):
        id = imdb_id
        stm = update(model.Movie).where(model.Movie.imdb_id == id[0][0]).values(series_title=title, imdb_id=int(id[0][0]), release_year=int(year), runtime=time, genre=genre, overview=overview, director=director, star1=star1, star2=star2,star3=star3, star4=star4, gross=gross)
        self.session.execute(stm)
        # f"UPDATE {model.Movie.__tablename__} SET series_title={title}, imdb_id={int(id[0][0])}, release_year={int(year)}, runtime={time}, genre={genre}, overview={overview}, director={director}, star1={star1}, star2={star2},star3={star3}, star4={star4}, gross={gross} WHERE imdb_id={int(id[0][0])}"