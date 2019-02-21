import sqlite3
import random

conn = sqlite3.connect('quotes.db')
c = conn.cursor()

#Create initial table quotesList
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS quotesList(theme TEXT, author TEXT, quote TEXT)')

#Adds data into the quotesList table
def data_entry(theme, author, quote):
    c.execute("INSERT INTO quotesList (theme, author, quote) VALUES (?, ?, ?, ?)",
               (theme, author, quote))
    conn.commit()

create_table()