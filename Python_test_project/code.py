from tinydb import TinyDB, Query

book_list = TinyDB('db.json')

class Books:
    def __init__(self, book_details):
        self.book_details = book_list.insert({'Author': input('Enter Author: ')})

def get_all():
    for item in book_list:
        print(item)


get_all()

Author = Query()
print ('This is the author I searched for', book_list.search(Author.Author == 'Skoczylis, Joshua'))

book_list.update({'Author': 'Blair, Tony'}, Author.Author == 'Blair')

get_all()