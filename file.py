import random
print("Welcome to Find The Gold!")
print("Rules : \n1. You will guess the location of the gold\n2. You will guess by entering number of row and column(example : 12, row 1, column 2)\n3. There are three level of achievements, Perfect(able to guess below 3 guesses), average(able to guess below 7 guesses), and Noob(only able to guess above 8 guesses)")
name = input("What's your name? ")
maps = [["■","■","■"],["■","■","■"],["■","■","■"]]
row = random.randint(0,2)
column = random.randint(0,2)
gold = maps[row][column]
print(maps)
print(f"Thankyou for using our program,{name}!")
