from datetime import datetime, date
import dbm

from inventory_data import InputTexts, ExceptionsMessages
from main import clear_screen

def input_price(text):
    """Input the product price"""
    while True:
        try:
            price = float(input(text))
            break
        except:
            print(ExceptionsMessages.INPUT_YEAR_TYPE[lang])
    
    if price < 0:
        print(ExceptionsMessages.INPUT_YEAR_RANGE[lang])
        return input_price(text)
    else:
        return price


def input_requised_year(text):
    """Input a required year."""
    while True:
        try:
            year = int(input(text))
            break 
        except:
            print(ExceptionsMessages.INPUT_YEAR_TYPE[lang])
    
    if year < 0 or year > datetime.now().date().year:
        print(ExceptionsMessages.INPUT_YEAR_RANGE[lang])
        return input_requised_year(text)
    else:
        return date(year,1,1)


def input_year(text):
    """Input the year or none value."""
    while True:
        try:
            year = input(text)
            if year == "":
                return None
            year = int(year)
            break 
        except:
            print(ExceptionsMessages.INPUT_YEAR_TYPE[lang])
    
    if year < 0 or year > datetime.now().date().year:
        print(ExceptionsMessages.INPUT_YEAR_RANGE[lang])
        return input_requised_year(text)
    else:
        return date(year,1,1)


def input_required_text(text):
    """Input a required sigle string element."""
    field = input(text)
    if len(field) == 0: # must have at least 1 char
        input_required_text(text)
    elif len(field) > 300: # must have maximum of 300 char
        input_required_text(text)
    else:
        return field.upper()


def input_multiple_required_text(text):
    """Input one or more required string elements."""
    field = input(text)
    if len(field) == 0: # must have at least 1 char
        input_multiple_required_text(text)
    if ',' in field:
        return set_elements(field.upper())
    else:
        return field.upper() 


def set_elements(string_elements):
    """Return a list of strings."""
    if string_elements == None:     # stop condition 1
        return []

    elif string_elements[0] == ' ': # first element is a " "
        return set_elements(string_elements[1:])

    elif ',' in string_elements:    # string has more than 1 element
        index = string_elements.find(',')
        if string_elements[index - 1] == ' ':
            return [string_elements[:index - 1]] + set_elements(string_elements[index + 1:])
        else:
            return [string_elements[:index]] + set_elements(string_elements[index + 1:])

    else:                           # stop condition 2 (last element)
        return [string_elements]


def get_elements(list_elements):
    """Return a string with all elements."""
    delimiter = ", "
    return delimiter.join(list_elements)


def input_book():
    """Input book info and insert into the database."""
    #book_db = dbm.open("books", "c")


    title =            input_required_text(InputTexts.INPUT_BOOK_TITLE[lang])
    author =           input_multiple_required_text(InputTexts.INPUT_BOOK_AUTHOR[lang])
    genre =            input_multiple_required_text(InputTexts.INPUT_BOOK_GENRE[lang])
    publisher =        input_required_text(InputTexts.INPUT_BOOK_PUBLISHER[lang])
    info =             input_required_text(InputTexts.INPUT_BOOK_INFO[lang])
    release_year =     input_year(InputTexts.INPUT_BOOK_RELEASE_YEAR[lang])
    publication_year = input_requised_year(InputTexts.INPUT_BOOK_PUBLICATION_YEAR[lang])
    purchase_year =    input_year(InputTexts.INPUT_BOOK_PURCHASE_YEAR[lang])
    purchase_price =   input_price(InputTexts.INPUT_BOOK_PRICE[lang])

    clear_screen()
    print("\nDados do livro cadastrado\n")
    print("Título: \n    "+ title)
    print("Autor:  \n    "+ get_elements(author))
    print("Gênero: \n    "+ get_elements(genre))
    print("Info:   \n    "+ info)
    #print(publication_year)
    #print("Editora: \n    " + publisher)



#def main():
    #input_book()
    #y = input_requised_year()
    #print(y)
    # d1 = date(2020,4,20)
    # d2 = date(1993,1,18)
    # d3 = d1-d2
    # print(datetime.now().date().year)
    # print(date(2020,4,1))
    # print(d3)
    # string = ""
    # print(len(string))

if __name__ == "__main__":
    lang = "pt"
