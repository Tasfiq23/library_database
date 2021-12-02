from models import Base, session,Book,engine
import datetime
import csv 


def menu():
    while True:
        print('''
            \nProgramming Books
            \r1) Add book 
            \r2) View all book
            \r3) Search for book
            \r4) Book analysis
            \r5) Exit ''')
        choice = input('What would you like to do? ')
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''
            \r Please choose one of the options above.
            \r A number from 1-5 ''') 
def clean_date(date_str):
    #datetime.date()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = months.index(split_date[0])+1
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year,month,day)

def clean_price(price_str):
    price = float(price_str)
    return int(price * 100)



def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title = title, author=author,published_date = date,price =price)
                session.add(new_book)
        session.commit()




def app():
    app_running = True 
    while app_running:
        choice = menu()
        if choice == 1:
            # add book
            pass
        if choice== 2:
            pass
        if choice== 3:
            pass
        if choice== 4:
            pass
        else:
            print('\nGoodbye')
            app_running = False






if __name__=='__main__':
    Base.metadata.create_all(engine)
     # app()
    add_csv()
    

    for book in session.query(Book):
        print(book)
    

# imports models file 
# main menu -add,search,analysis,exit,view
# add books  to the database
# edit books
# delete books
# search books
# data cleaning
# loop runs program

