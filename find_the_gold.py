import random
def checker_chance(p_chance):
    if p_chance<=3:
        print("You've achieve perfect level!")
    elif p_chance>3 and p_chance<=7:
        print("You've achieve average level!")
    else:
        print("You've achieve noob level!")
print("Welcome to Find The Gold!")
print("Rules : \n1. You will guess the location of the gold\n2. You will guess by entering number of row and column(example : 12, row 1, column 2)\n3. Row and column starts from 1\n4. There are three level of achievements, Perfect(able to guess below 3 guesses), average(able to guess below 7 guesses), and Noob(only able to guess above 8 guesses)")
name = input("What's your name? ")
maps = [["■","■","■"],["■","■","■"],["■","■","■"]]
row = random.randint(0,2)
column = random.randint(0,2)
print("",maps[0],"\n",maps[1],"\n",maps[2])
chance = 0
while True:
    ans = int(input("Please guess the gold : "))
    ans = str(ans)
    loc1 = int(ans[0])-1
    loc2 = int(ans[1])-1
    print(loc1,loc2)
    if maps[loc1][loc2]=="X":
        print("Cannot enter the same number of row and column as before")
    chance+=1
    if loc1==row and loc2==column:
        print(f"Congratulations, {name}.. You guessed it correctly")
        break
    else:
        print("You guessed it wrong!")
        maps[loc1][loc2] = "X"
        print("",maps[0],"\n",maps[1],"\n",maps[2])
checker_chance(chance)
print(f"Thankyou for using our program,{name}!")
