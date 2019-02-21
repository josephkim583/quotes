import sqlite3
import random

conn = sqlite3.connect('quotes.db', check_same_thread=False)
c = conn.cursor()

#Create initial table quotesList
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS quotesList(theme TEXT, author TEXT, quote TEXT)')

#Adds data into the quotesList table
def data_entry(theme, author, quote):
    c.execute('''INSERT INTO quotesList (theme, author, quote) VALUES (:theme, :author, :quote)''', 
            {'theme' : theme, 'author' : author, 'quote' : quote})
    conn.commit()

#Given category parameters get a random quote related to the provided categories
def read_from_db(theme, author):
    quotes = []
    if theme == None and author == None:
        c.execute('''SELECT quote FROM quotesList''')

    elif theme == None or author == None:
        c.execute('''SELECT quote FROM quotesList WHERE theme = :theme 
                                                    OR author = :author''',
                                                    {'theme': theme, 'author' : author})
    else:                                             
        c.execute('''SELECT quote FROM quotesList WHERE theme = :theme 
                                                    AND author = :author''',
                                                    {'theme': theme, 'author' : author})
    
    #Add all quotes with matching categories into quotes list    
    for row in c.fetchall():
        quotes.append(row[0])

    if len(quotes) == 0:
        return "No entries are available"
    else:
        return (quotes[random.randint(0,len(quotes) - 1)])

 
'''
Hard coded quotesList table for now


create_table()
data_entry("Life", "Shaw", "Life isn't about finding yourself. Life is about creating yourself.")
data_entry("Life", "Lincoln", "In the end, it's not the years in your life that count. It's the life in your years.")
data_entry("Life", "Socrates", "An unexamined life is not worth living.")
data_entry("Life", "Bell", "When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one that has opened for us.")
data_entry("Life", "Lincoln", "Slavery sucks.")

data_entry("Love", "Jung", "You may hold my hand for a while, but you hold my heart forever.")
data_entry("Love", "Jung", "I know I am in love with you because my reality is finally better than my dreams.")
data_entry("Love", "Kim", "Love is great.")
data_entry("Love", "Kim", "I love my princess.")
'''


