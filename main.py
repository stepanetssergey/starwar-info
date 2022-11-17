from settings.menu import Menu
from objects.personage import Personage

# create instance of class Menu
menu = Menu()
print(menu.description)

menu_item_number = input()

if menu_item_number == '1':
    print(menu.get_item(menu_item_number), end=' ')
    personage_name = input()
    current_personage = Personage(personage_name)
    if personage_name == '':
        print(current_personage.get_all())
    else:
        #print(current_personage.get_one())
        current_personage.show_personage(current_personage.get_one())
elif menu_item_number == '2':
    print(menu.get_item(menu_item_number))

elif menu_item_number == '3':
    print(menu_item_number)
else:
    print("Code is not correct!!!")
