import random as rnd
c=rnd.randint(1,6)
count=0
life=0
flag=0
print  "Welcome to my dice game!\n Here all you have to do is guess a number\nAnd your PC will do the rest.\n"
print  "Rules: You have only 3 lives. You get wrong, you fail.\n You get right, score's given 5 for each success!\nEnjoy :p"
print  "Enter your guess:" 

while(flag!=1):
	n=int(input())
	if n<1 or n>6:
		print  "Give a number between [1,6]."
	elif n==c:
	    count+=1
	    print "You got a correct answer!"
	elif n!=c:
		life+=1
		print "Answer's wrong! Life left", 3-life

	if life==3:
		flag=1
		print "Well, better luck next time!"
