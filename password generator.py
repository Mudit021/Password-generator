import random as r
a=int(input("Enter the number of characters:"))
b=[]
e=[]
i=0
j=0
# this will generate random list of number between 0 to 9
while i<a:
	g=r.randint(0,9)
	b.append(g)
	i+=1
# this will generate random list of alphabets in both capitalized as well as small
while j<a:
	c=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
	d=r.choice(c)
	j+=1
	e.append(d)
#then we will concatenate the two strings and shuffle them to generate the password
alphanum=e+b
r.shuffle(alphanum)

print('the numbers are:',*b)
print('the alphabets are:',*e)
print('the generated password is:',*alphanum)
