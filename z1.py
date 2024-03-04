import sqlite3

conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

def add_movie(title, director, year, genre):
    cr.execute("""
        INSERT INTO movies (title, director, year, genre) 
        VALUES (?,?,?,?)""",(title,director,year,genre)
        )
    conn.commit()  # Committing the changes to the database
    print("Movie added :)")

add_movie("Inception","Christopher Nolan",2010,"Sci-Fi")