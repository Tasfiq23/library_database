from models import Base, session,Book,engine
import datetime
import csv 
import time


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
def submenu():
    while True:
        print('''
            \n1) Edit
            \r2) Delete
            \r3) Return to main menu''')
        choice = input('What would you like to do? ')
        if choice in ['1','2','3']:
            return choice
        else:
            input('''
            \r Please choose one of the options above.
            \r A number from 1-3 ''') 
def clean_date(date_str):
    #datetime.date()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = months.index(split_date[0])+1
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year,month,day)
    except ValueError:
        input('''
              \n*****DATE ERROR****
              \rThe date format should include a valid Month,Day,Year
              \rEX: January 13, 2003
              \rPress enter to try again.
              \r********************''')
        return
    else:    
        return datetime.date(year,month,day)

def clean_price(price_str):
    try:
        price = float(price_str)
        
    except ValueError:
        input('''
              \n*****PRICE ERROR****
              \rThe price format should be a number without any symbol
              \rEX: 20.00
              \rPress enter to try again.
              \r********************''')
        return      
    else:
        return int(price * 100)
    
    
def clean_id(id_str,options):
    try:
        book_id = int(id_str)
    except ValueError:
        input('''
              \n*****ID ERROR****
              \rThe id format should be a number without any symbol
              \rPress enter to try again.
              \r********************''')  
        return 
    else:
        if book_id in options:
            return book_id
        else:
            input(f'''
              \n*****ID ERROR****
              \rOptions:{options}
              \rPress enter to try again.
              \r********************''') 
            return  
        

def edit_check(column_name,current_value):
    print(f'\n**** EDIT {column_name} ****')
    if column_name == 'Price':
        print(f'\rCurrent Value: {current_value/100}')
    elif column_name == 'Date':
        print(f'\rCurrent Value: {current_value.strftime("%B %d %Y ")}')
    else:
        print(f'\rCurrent Value: {current_value}')

    if column_name == 'Date' or column_name == 'Price':
        while True:
            changes = input('What would you like to change the value to? ')
            if column_name == 'Date':
                changes = clean_date(changes)
                if type(changes) == datetime.date:
                    return changes
            elif column_name == 'Price':
                changes = clean_price(changes)
                if type(changes) == int:
                    return changes
            
    else:
        return input('What would you like to change the value to? ')
    
    

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
        if choice == '1':
            # Add books
            title=input("Title: ")
            author =  input("Author: ")
            date_error = True
            while date_error:
                date = input("Published Date(Ex: October 25, 2017): ")
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error =False
            price_error = True
            while price_error:
                price = input("Price(Ex: 25.65): ")
                price= clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title = title,author=author,published_date=date,price=price)
            session.add(new_book)
            session.commit()
            print('Book is Added')
            time.sleep(1.5)
                    

        elif choice== '2':
            # View Books
            for book in session.query(Book):
                print(f'{book.id} | {book.title} | {book.author}')
            input('\nPress Enter to return to the main menu')
            
        elif choice== '3':
            #Search book
            id_options = []
            for book in session.query(Book):
                id_options.append(book.id)
            id_error= True
            while id_error:    
                id_choice=input(f'''
                    \nId Options: {id_options}
                    \rBook id: ''')
                id_choice = clean_id(id_choice,id_options)
                if type(id_choice) == int:
                    id_error=False
            the_book = session.query(Book).filter(Book.id==id_choice).first()
            print(f'''\n{the_book.title} by {the_book.author} \nPublished:{the_book.published_date} \nPrice: ${the_book.price/100}''')
            
            sub_choice = submenu()
            if sub_choice == '1':
                # edit
                the_book.title = edit_check('Title',the_book.title)
                the_book.author = edit_check('Author',the_book.author)
                the_book.published_date = edit_check('Date',the_book.published_date)
                the_book.price = edit_check('Price',the_book.price)
                print(session.dirty)
            elif sub_choice == '2':
                # delete
                pass    
            
                    
        elif choice== '4':
            pass
        else:
            print('\nGoodbye')
            app_running = False







if __name__=='__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()
    
    

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

