name = input("type your name: ")
print("Welcome", name, "to this adventure!" )

answer = input("you are on a dirt road, it has come to an end and you can go left and right, which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? type walk to walk around and swim to swim accross: ")
    
    if answer == "swim":
        print("you swim accross and were eaten by an alligator. ")
    elif answer == "walk":
        print("you walk for many miles, ran out of water and you lost the game.")
       
    else:
         print("Not a valid option. you lose.")
                

elif answer == "right":
    print()
    
else:
    print("Not a valid option. you lose.")    
        
    