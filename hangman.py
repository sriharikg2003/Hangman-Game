import numpy as np
import time 
import sridraw as hang
         
def welcome():
       print("WELCOME TO HANG MAN GAME")
       global name
       name=input("Enter your name\n")
       print("\nHai {}, \nLet's begin the game".format(name.upper()))
       time.sleep(1)
       print("\nYou have 8 choices\nFor each wrong guess your body parts apper on the hanging stage\nOnce you fail all attempts, You will be killed\nThis is the Stage\nIf you lose you will be hanged here\n")
       time.sleep(4)
       print(hang.stage)
       
       
def hangmandraw(index,question):
       if index==7 :
              global name
              print("Oh..You are gonna die now!!".format(name),"The word was {}".format(question))
              for i in range(8):
               print(hang.l[i])
               time.sleep(0.4)
              time.sleep(0.5) 
              print("Sorry {} , you are dead now".format(name) )
       else:      
        print("Aw...Wrong Guess...You may die soon ")
        for i in range(index+1):
              print(hang.l[i])

welcome()

def niceprint(name):
       for i in name:
              print(i," ",end="")
       print("\n")              

error_num=0

def guess(question,formword):
       time.sleep(.5)
       letter=input("Guess a letter ")
       index_array=[]

       for i in range(len(question)):
              if question[i]==letter:
                     index_array.append(i)
                     formword[i]=letter

       if question.rfind(letter) >=0:
              print("\nGreat\n")
              niceprint(formword)
             
                          
       else:
              global error_num
              hangmandraw(error_num,question)
              error_num=error_num+1

file=open("words.txt")
words=[]
for f in file:
       if len(f)<6:
         words.append(f.replace('\n',""))
         

index=np.random.randint(0,len(words))
question=words[index]
print("Your Guessing Word is Ready : No of Letters = ",len(question))

formword=[]
question_array=[]

for i in question:
       question_array.append(i)
for i in range(len(question)):        
       formword.append("_")


for i in range(8):
       if formword==question_array:
                   print("Hey Congrats!! You Won ".format(name)) 
                   break
       guess(question,formword)
       if i==7 and error_num!=8:
              hangmandraw(7,question)



