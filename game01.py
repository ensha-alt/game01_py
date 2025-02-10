# THIS IS A GAME OF SNAKE , WATER AND GUN 
import random 
'''  1 for snake
-1 for water
0 for gun '''

print("GAME STARTS\n choose g for gun , s for snake , w for water \n")

computer= random.choice([1,0,-1])
youstr=input("enter your choice ")
youDict={"s":1, "g":0, "w":-1}
reverseDict={1:"snake" , 0:"gun" , -1:"water"}

you=youDict[youstr]
            

print(f"you choose {reverseDict[you]} \n computer choose {reverseDict[computer]}")

if(you==computer):
    print("its a draw!")

else:
    if(computer==-1 and you==1):
        print("you win") 

    elif(computer==-1 and you==0):
            print("you loose") 

    elif(computer==1 and you==-1):
            print("you loose") 
    elif(computer==1 and you==0):
            print("you win") 
    elif(computer==0 and you==1):
            print("you loose") 
    elif(computer==0 and you==-1):
            print("you win") 
    else:
        print("something went wrong")        
    

print("\nGAME OVER ")        