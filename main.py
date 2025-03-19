#Game of ROCK,PAPER,SISOR

'''
R=1
P=-1
S=0

'''
import random
computer=random.choice([1,-1,0])


youstr=input("Enter your choice(R,P,S): ")
dict={'R':1,'P':-1,'S':0}
reversedict={1:"Rock",-1:"Paper",0:"Sisor"}

you=dict[youstr]

print(f"you chose: {reversedict[you]}\nComputer chose: {reversedict[computer]}")

if(computer==you):
    print("ITS A DRAW")

else:
     if(computer==1 and you==-1):
         print("YOU WIN")
     elif(computer==1 and you==0):
         print("YOU LOSE")
     elif(computer==-1 and you==1):
         print("YOU LOSE")
     elif(computer==-1 and you==0):
         print("YOU WIN")
     elif(computer==0 and you==1):
         print("YOU WIN")
     elif(computer==0 and you==-1):
         print("YOU LOSE")

     else:
         print("SORRY!! Something went wrong ")
