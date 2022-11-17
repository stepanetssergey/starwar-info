class Menu:

    description = """
                    MENU
                    Show personage(s) [ 1 ]
                    Show planets  [ 2 ]
                    Show starships [ 3 ]
                   """
    menu_items = {
        '1': 'Input personage name (or Enter for list of personages):',
        '2': 'Show planets',
        '3': 'Show starships',
        'not_correct': 'Code is not correct!!!'
    }

    def get_item(self, item_number):
        return self.menu_items[item_number]

