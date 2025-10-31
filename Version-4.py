import random as rd
numbers=[]
magic_number= rd.randint(1,10)
print(magic_number)

guess=int(input("what is your guess?:"))
counter=3

while guess != magic_number and counter > 0 :
  counter-=1
  numbers.append(guess)
  print("your past guesses are %s " % (numbers))
  print("you have %d guesses left" % (counter))
  if counter==0:
    print("gameover")
  else:
    guess=int(input("try again:"))
  
if guess==magic_number:
    print("you win!")
    
