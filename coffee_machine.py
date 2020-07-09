class CoffeeMachine:
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        # A current state variable to guide the action function.
        self.state = 'choosing an action'
        self.power = 'on'

    # A monitoring function to cycle through action types and down action paths
    # calls separate class functions: buy(), fill(), take(), and remaining()
    def user_arg(self):
        while self.power != 'off':
            self.state = input('Write action (buy, fill, take, remaining, exit):')

            if self.state == 'buy':
                buy_var = input('What do you want to buy? 1 -espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                if buy_var == 'back':
                    continue
                else:
                    self.buy(buy_var)

            if self.state == 'fill':
                water_add = int(input("Write how many ml of water do you want to add:"))
                self.fill('water', water_add)
                milk_add = int(input("Write how many ml of milk do you want to add:"))
                self.fill('milk', milk_add)
                beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
                self.fill('beans', beans_add)
                cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
                self.fill('cups', cups_add)
                self.state = 'choosing an action'

            if self.state == 'take':
                self.take()

            if self.state == 'remaining':
                self.remaining()

            if self.state == 'exit':
                self.power == 'off'
                break

    def buy(self, item):
        if item == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                self.state = 'choosing an action'
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
                self.state = 'choosing an action'
            elif self.cups < 1:
                print("Sorry, not enough cups!")
                self.state = 'choosing an action'
            else:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
                self.state = 'choosing an action'

        elif item == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
                self.state = 'choosing an action'
            elif self.milk < 75:
                print("Sorry, not enough milk!")
                self.state = 'choosing an action'
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
                self.state = 'choosing an action'
            elif self.cups < 1:
                print("Sorry, not enough cups!")
                self.state = 'choosing an action'
            else:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
                self.state = 'choosing an action'
        elif item == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                self.state = 'choosing an action'
            elif self.milk < 100:
                print("Sorry, not enough milk!")
                self.state = 'choosing an action'
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
                self.state = 'choosing an action'
            elif self.cups < 1:
                print("Sorry, not enough cups!")
                self.state = 'choosing an action'
            else:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
                self.state = 'choosing an action'

    def fill(self, item, amount):
        if item == 'water':
            self.water += amount
        if item == 'milk':
            self.milk += amount
        if item == 'beans':
            self.beans += amount
        if item == 'cups':
            self.cups += amount

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.state = 'choosing an action'

    def remaining(self):
        print()
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")
        self.state = 'choosing an action'


coffee_machine = CoffeeMachine()
coffee_machine.user_arg()
