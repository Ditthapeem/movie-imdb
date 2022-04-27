import tkinter as tk
from tkinter import ttk

from movie.persistence.imdb_dao import IMDBDao
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///top_100_movie.db')
Session = sessionmaker(bind=engine)
session = Session()
imdb = IMDBDao(session)

window = tk.Tk()
window.title("Top 100 Movie in IMDB")
frame = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

def remove_record():
    for i in table.get_children():
            table.delete(i)

# Search
def get_id():
    remove_record()
    if(id_entry.get() == ""):
        load_all_data()
    else:
        imdb_id = imdb.get_imdb_id_from_id(id_entry.get())
        imdb_rating = imdb.get_imdb_rating_from_id(id_entry.get())
        meta_score = imdb.get_meta_score_from_id(id_entry.get())
        no_of_vote = imdb.get_no_of_vote_from_id(id_entry.get())
        certificate = imdb.get_certificate_from_id(id_entry.get())
        poster_link = imdb.get_poster_link_from_id(id_entry.get())
        table.insert(parent='', index='end', iid=0,text='', values=(imdb_id[0][0],
                                                                    imdb_rating[0][0],
                                                                    meta_score[0][0],
                                                                    no_of_vote[0][0],
                                                                    certificate[0][0],
                                                                    poster_link[0][0]))
id_label = tk.Label(frame, text="IMDB ID").grid(column=0,row=0,padx=5)
id_entry = tk.Entry(frame, width=20)
id_entry.grid(column=1,row=0,padx=5)
id_button = tk.Button(frame,text="Search",width=15 ,command=get_id).grid(column=2,row=0,padx=5)


# Update

def update_data():
    remove_record()
    id = imdb.get_imdb_id_from_id(search_id_entry.get())
    if id != None:
        imdb_rating = update_imdb_rating_entry.get()
        meta_score = update_meta_score_entry.get()
        no_of_vote = update_no_of_vote_entry.get()
        certificate = update_certificate_entry.get()
        poster_link = update_poster_link_entry.get()
        imdb.update_imdb(id, imdb_rating, meta_score, no_of_vote, certificate, poster_link)
        remove_record()
        load_all_data()


update_label = tk.Label(frame3, text="Update This ID").grid(column=0,row=0,padx=5) 
update_id_label = tk.Label(frame3, text="IMDB ID :").grid(column=0,row=1,padx=5, pady=5) 
update_id_entry = tk.Entry(frame3, width=20)
update_id_entry.grid(column=1,row=1,padx=5, pady=5)

search_id_entry = tk.Entry(frame3, width=20)
search_id_entry.grid(column=1,row=0,padx=5)
# search_id_button = tk.Button(frame3,text="Search for Update",width=15 ,command=get_id).grid(column=2,row=0,padx=5)

update_imdb_rating_label = tk.Label(frame3, text="IMDB Rating :").grid(column=2,row=1,padx=5, pady=5) 
update_imdb_rating_entry = tk.Entry(frame3, width=20)
update_imdb_rating_entry.grid(column=3,row=1,padx=5, pady=5)

update_meta_score_label = tk.Label(frame3, text="Meta score :").grid(column=4,row=1,padx=5, pady=5) 
update_meta_score_entry = tk.Entry(frame3, width=20)
update_meta_score_entry.grid(column=5,row=1,padx=5, pady=5)

update_no_of_vote_label = tk.Label(frame3, text="Number of Vote :").grid(column=0,row=2,padx=5, pady=5) 
update_no_of_vote_entry = tk.Entry(frame3, width=20)
update_no_of_vote_entry.grid(column=1,row=2,padx=5, pady=5)

update_certificate_label = tk.Label(frame3, text="Certificate :").grid(column=2,row=2,padx=5, pady=5) 
update_certificate_entry = tk.Entry(frame3, width=20)
update_certificate_entry.grid(column=3,row=2,padx=5, pady=5)

update_poster_link_label = tk.Label(frame3, text="Poster Link :").grid(column=4,row=2,padx=5, pady=5) 
update_poster_link_entry = tk.Entry(frame3, width=20)
update_poster_link_entry.grid(column=5,row=2,padx=5, pady=5)

update_button = tk.Button(frame3, text="Update",command=update_data, width=16)
update_button.grid(column=5,row=3,padx=5, pady=5)

# Table
table = ttk.Treeview(frame2)
table['columns'] = ('imdb_id','imdb_rating', 'meta_score' , 'no_of_vote' , 'certificate' , 'poster_link')
table.column('#0', width=0,stretch="NO")
table.column('imdb_id', width=100)
table.column('imdb_rating', width=100)
table.column('meta_score', width=100)
table.column('no_of_vote', width=100)
table.column('certificate', width=100)
table.column('poster_link', width=150)

table.heading('#0', text='')
table.heading('imdb_id', text='IMDB ID')
table.heading('imdb_rating', text='IMDB Rating')
table.heading('meta_score', text='Meta score')
table.heading('no_of_vote', text='No of Vote')
table.heading('certificate', text='Certificate')
table.heading('poster_link', text='Poster Link')

table.grid(row=0, column=0, sticky='nsew')

def load_all_data():
    imdb_id = imdb.get_imdb_id()
    imdb_rating = imdb.get_imdb_rating()
    meta_score = imdb.get_meta_score()
    no_of_vote = imdb.get_no_of_vote()
    certificate = imdb.get_certificate()
    poster_link = imdb.get_poster_link()
    for i in range(101):
        table.insert(parent='', index='end', iid=i,text='', values=(imdb_id[i][0],
                                                                    imdb_rating[i][0],
                                                                    meta_score[i][0],
                                                                    no_of_vote[i][0],
                                                                    certificate[i][0],
                                                                    poster_link[i][0]))  

load_all_data()

frame.pack(padx=10,pady=10,expand=1)
frame3.pack(padx=10,pady=10,expand=1)
frame2.pack(side=tk.LEFT, padx=10,pady=10, expand=1)
window.mainloop()