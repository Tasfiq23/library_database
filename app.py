from models import Base, session,Book,engine




if __name__=='__main__':
    Base.metadata.create_all(engine)
# import models file 
# main menu -add,search,analysis,exit,view
# add books  to the database
# edit books
# delete books
# search books
# data cleaning
# loop runs program

