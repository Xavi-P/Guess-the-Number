import os

play=True
attempt=0
wins=0
round=1




while play:
  
  import random as rd
  numbers=[]
  magic_number= rd.randint(1,100)
  print("Welcome to guess the number!")
  # print(magic_number)
  guess=int(input("what is your guess?:"))
  counter=6

  while guess != magic_number and counter > 0 :
    counter-=1
    numbers.append(guess)
    print("your already guessed  %s " % (numbers))
    if magic_number<guess:
      print("try a lower number")
    if magic_number>guess:
        print("try a higher number")
    print("you have %d guesses left" % (counter))
    if counter==0:
      print("GAMEOVER")
    elif guess != magic_number:
      guess=int(input("try again:"))
  
  if guess==magic_number:
    print("you win!")
    wins+=1
  if guess==magic_number or counter==0:
    attempt+=1
    print("SCOREBOARD")
    print("----------")
    print ("you've won %d out %d rounds" % (wins,attempt))
    
    print("would you like to play another round?")
    response=input("y/n")
      
    if response == "y":
        
      os.system("cls")
      round+=1
      
      print("Okay round "+str(round))
    else:
      play=False
      print(" bye bye ")
