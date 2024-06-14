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
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    
    if answer == "back":
        print("you go back and lose ")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger, do you talk to them (yes/no)? ")
        
        if answer == "yes":
            print("you talk to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("you ingore the stranger and they are offended and lose ")
        else:
            print("Not a valid option. you lose.")
else:
    print("Not a valid option. you lose.")
    
print("Thank you for trying", name)    
    
    
 
        
    