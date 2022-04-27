import tkinter as tk
from tkinter import ttk

from movie.persistence.movie_dao import MovieDao
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///top_100_movie.db')
Session = sessionmaker(bind=engine)
session = Session()
movie = MovieDao(session)

window = tk.Tk()
window.title("Top 100 Movie in IMDB")
frame = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

def remove_record():
    for i in table.get_children():
            table.delete(i)

# Search
def get_title():
    remove_record()
    if(title_entry.get() == ""):
        load_all_data()
    else:
        title = movie.get_title_form_title(title_entry.get())
        imdb_id = movie.get_imdb_id_form_title(title_entry.get())
        year = movie.get_released_year_form_title(title_entry.get())
        time = movie.get_runtime_form_title(title_entry.get())
        genre = movie.get_genre_form_title(title_entry.get())
        overview = movie.get_overview_form_title(title_entry.get())
        director = movie.get_director_form_title(title_entry.get())
        star1 = movie.get_star1_form_title(title_entry.get())
        star2 = movie.get_star2_form_title(title_entry.get())
        star3 = movie.get_star3_form_title(title_entry.get())
        star4 = movie.get_star4_form_title(title_entry.get())
        groos = movie.get_gross_form_title(title_entry.get())
        table.insert(parent='', index='end', iid=0,text='', values=(title[0][0], 
                                                                    imdb_id[0][0],
                                                                    year[0][0],
                                                                    time[0][0], 
                                                                    genre[0][0],
                                                                    overview[0][0],
                                                                    director[0][0],
                                                                    star1[0][0],
                                                                    star2[0][0], 
                                                                    star3[0][0], 
                                                                    star4[0][0], 
                                                                    groos[0][0]))

title_label = tk.Label(frame, text="Movie Title").grid(column=0,row=0,padx=5)
title_entry = tk.Entry(frame, width=20)
title_entry.grid(column=1,row=0,padx=5)
title_button = tk.Button(frame,text="Search",width=15 ,command=get_title).grid(column=2,row=0,padx=5)

# Update
def update_data():
    title = movie.get_title_form_title(search_update_title_entry.get())
    if title != None:
        title = update_title.get()
        imdb_id = movie.get_imdb_id_form_title(search_update_title_entry.get())
        year = update_released_year.get()
        time = update_runtime.get()
        genre = update_genre.get()
        overview = update_overview.get()
        director = update_director.get()
        star1 = update_star1.get()
        star2 = update_star2.get()
        star3 = update_star3.get()
        star4 = update_star4.get()
        groos = update_gross.get()
        movie.update_movie(title, imdb_id, year, time, genre, overview, director, star1, star2, star3, star4, groos)
        remove_record()
        load_all_data()
    

update_label = tk.Label(frame3, text="Update This Movie: ").grid(column=0,row=0,padx=5) 
update_title_label = tk.Label(frame3, text="Title :").grid(column=0,row=1,padx=5, pady=5) 
update_title = tk.Entry(frame3, width=20)
update_title.grid(column=1,row=1,padx=5, pady=5)

search_update_title_entry = tk.Entry(frame3, width=20)
search_update_title_entry.grid(column=1,row=0,padx=5)
# search_update_title_button = tk.Button(frame3,text="Search for Update",width=15 ,command=get_title).grid(column=2,row=0,padx=5)

update_button = tk.Button(frame3, text="Update",command=update_data, width=16)
update_button.grid(column=11,row=2,padx=5, pady=5)

update_released_year_label = tk.Label(frame3, text="Released_Year :").grid(column=2,row=1,padx=5, pady=5) 
update_released_year = tk.Entry(frame3, width=20)
update_released_year.grid(column=3,row=1,padx=5, pady=5)

update_runtime_label = tk.Label(frame3, text="Runtime :").grid(column=4,row=1,padx=5, pady=5) 
update_runtime = tk.Entry(frame3, width=20)
update_runtime.grid(column=5,row=1,padx=5, pady=5)

update_genre_label = tk.Label(frame3, text="Genre :").grid(column=6,row=1,padx=5, pady=5) 
update_genre = tk.Entry(frame3, width=20)
update_genre.grid(column=7,row=1,padx=5, pady=5)

update_overview_label = tk.Label(frame3, text="Overview :").grid(column=8,row=1,padx=5, pady=5) 
update_overview = tk.Entry(frame3, width=20)
update_overview.grid(column=9,row=1,padx=5, pady=5)

update_director_label = tk.Label(frame3, text="Director :").grid(column=10,row=1,padx=5, pady=5) 
update_director = tk.Entry(frame3, width=20)
update_director.grid(column=11,row=1,padx=5, pady=5)

update_star1_label = tk.Label(frame3, text="Star1 :").grid(column=0,row=2,padx=5, pady=5) 
update_star1 = tk.Entry(frame3, width=20)
update_star1.grid(column=1,row=2,padx=5, pady=5)

update_star2_label = tk.Label(frame3, text="Star2 :").grid(column=2,row=2,padx=5, pady=5) 
update_star2 = tk.Entry(frame3, width=20)
update_star2.grid(column=3,row=2,padx=5, pady=5)

update_star3_label = tk.Label(frame3, text="Star3 :").grid(column=4,row=2,padx=5, pady=5) 
update_star3 = tk.Entry(frame3, width=20)
update_star3.grid(column=5,row=2,padx=5, pady=5)

update_star4_label = tk.Label(frame3, text="Star4 :").grid(column=6,row=2,padx=5, pady=5) 
update_star4 = tk.Entry(frame3, width=20)
update_star4.grid(column=7,row=2,padx=5, pady=5)

update_gross_label = tk.Label(frame3, text="Gross :").grid(column=8,row=2,padx=5, pady=5) 
update_gross = tk.Entry(frame3, width=20)
update_gross.grid(column=9,row=2,padx=5, pady=5)

# Table
table = ttk.Treeview(frame2)
table['columns'] = ('Series_Title' , 'IMDB_ID' , 'Released_Year' , 'Runtime' , 'Genre' , 'Overview' , 'Director' , 'Star1' , 'Star2' , 'Star3' , 'Star4' , 'Gross')
table.column('#0', width=0,stretch="NO")
table.column('Series_Title', width=100)
table.column('IMDB_ID', width=100)
table.column('Released_Year', width=100)
table.column('Runtime', width=100)
table.column('Genre', width=100)
table.column('Overview', width=100)
table.column('Director', width=100)
table.column('Star1', width=100)
table.column('Star2', width=100)
table.column('Star3', width=100)
table.column('Star4', width=100)
table.column('Gross', width=100)

table.heading('#0', text='')
table.heading('Series_Title', text='Series Title')
table.heading('IMDB_ID', text='IMDB ID')
table.heading('Released_Year', text='Released Year')
table.heading('Runtime', text='Runtime')
table.heading('Genre', text='Genre')
table.heading('Overview', text='Overview')
table.heading('Director', text='Director')
table.heading('Star1', text='Star1')
table.heading('Star2', text='Star2')
table.heading('Star3', text='Star3')
table.heading('Star4', text='Star4')
table.heading('Gross', text='Groos')

table.grid(row=0, column=0, sticky='nsew')
# Load data into table
def load_all_data():
    title = movie.get_title()
    imdb_id = movie.get_imdb_id()
    year = movie.get_released_year()
    time = movie.get_runtime()
    genre = movie.get_genre()
    overview = movie.get_overview()
    director = movie.get_director()
    star1 = movie.get_star1()
    star2 = movie.get_star2()
    star3 = movie.get_star3()
    star4 = movie.get_star4()
    groos = movie.get_gross()
    for i in range(101):
        table.insert(parent='', index='end', iid=i,text='', values=(title[i][0], 
                                                                    imdb_id[i][0],
                                                                    year[i][0],
                                                                    time[i][0], 
                                                                    genre[i][0],
                                                                    overview[i][0],
                                                                    director[i][0],
                                                                    star1[i][0],
                                                                    star2[i][0], 
                                                                    star3[i][0], 
                                                                    star4[i][0], 
                                                                    groos[i][0]))
load_all_data()

# Exit button
# ttk.Button(frame2, text="Quit", command=window.destroy).grid(column=1, row=1)
frame.pack(padx=10,pady=10,expand=1)
frame3.pack(padx=10,pady=10,expand=1)
frame2.pack(side=tk.LEFT, padx=10,pady=10, expand=1)
window.mainloop()