from settings.menu import Menu

# create instance of class Menu
menu = Menu()
print(menu.description)

menu_item_number = input()

if menu_item_number == '1':
    print(menu.get_item(menu_item_number))
elif menu_item_number == '2':
    print(menu.get_item(menu_item_number))
elif menu_item_number == '3':
    print(menu_item_number)
else:
    print("Code is not correct!!!")
