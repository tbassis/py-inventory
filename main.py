import os
from book import input_book
from inventory_data import MenuTexts, ExceptionsMessages


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """Inventory main menu."""
    clear_screen()

    while True:
        try:
            print(MenuTexts.MAIN_MENU[lang])
            option = int(input(MenuTexts.MAIN_MENU_SELECT[lang]))   # text with menu options
            break
        except: # input isn't a int
            clear_screen()
            input(ExceptionsMessages.MAIN_MENU_TYPE[lang])  # error message
            clear_screen()
    
    # check if selected menu is valid
    if option > 0 and option <= menu:
        return option
    else:
        clear_screen()
        input(ExceptionsMessages.MAIN_MENU_RANGE[lang]) # error message
        return main_menu()


def book_menu():
    """Book inventory menu."""
    clear_screen()

    while True:
        try:
            print(MenuTexts.BOOK_MENU[lang])
            book_action = int(input(MenuTexts.BOOK_MENU_SELECT[lang]))
            break
        except:
            clear_screen()
            input(ExceptionsMessages.MAIN_MENU_TYPE[lang])
            clear_screen()
    
    # check if selected action is valid
    if book_action == 1:
        pass
    elif book_action == 2:
        pass
    elif book_action == 3:
        clear_screen()
        input_book()
    elif book_action == 4:
        pass
    elif book_action == 5:   # back to main menu
        clear_screen()
        pass


def main():
    option = main_menu()

    if option == 1:
        book_menu()
        main()
    #elif option == 2:
    #    movie_menu()
    else:
        clear_screen()
        pass

    


if __name__ == "__main__":
    lang = "pt"
    menu = 3
    menu_book = 5
    main()