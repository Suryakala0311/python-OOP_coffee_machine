from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

should_continue = True

while should_continue:
    choice = input("What would you like (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        should_continue = False
    elif choice == "espresso" or "latte" or "cappuccino":
        coffee_type = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee_type):
            if money_machine.make_payment(coffee_type.cost):
                coffee_maker.make_coffee(coffee_type)
    
