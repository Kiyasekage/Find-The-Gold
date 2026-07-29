import random
print("Welcome to Find The Gold!")
print("Rules : \n1. You will guess the location of the gold\n2. You will guess by entering number of row and column(example : 12, row 1, column 2)\n3. There are three level of achievements, Perfect(able to guess below 3 guesses), average(able to guess below 7 guesses), and Noob(only able to guess above 8 guesses)")
name = input("What's your name? ")
maps = [["■","■","■"],["■","■","■"],["■","■","■"]]
row = random.randint(0,2)
column = random.randint(0,2)
print(row,column)
print(maps[0],maps[1],maps[2])
while True:
    ans = int(input("Please guess the gold : "))
    ans = str(ans)
    loc1 = int(ans[0])
    loc2 = int(ans[1])
    loc = maps[loc1][loc2]
    print(loc1,loc2)
    if loc1==row and loc2==column:
        print("Congratulations, {name}.. You guessed it correctly")
        break
    else:
        print("You guessed it wrong!")
        maps[loc1][loc2] = "x"
        print(maps)
print(f"Thankyou for using our program,{name}!")
