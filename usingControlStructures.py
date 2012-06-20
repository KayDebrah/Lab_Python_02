
#Question 5
theinput=raw_input("Enter an Integer: ")

varx=int(theinput)

if varx%2==0:
    print "Even"
else:
    print "Odd"


primaryschoolage=4
votingage=18
min_presidentage=50
retirement_age=60

PersonAge=input("Enter your age: ")
Age=int(PersonAge)

if Age<primaryschoolage:
    print "Too Young to be schooling"
    
elif Age>primaryschoolage and Age<votingage:
    print "Is of School Age"
    
elif Age>=votingage and Age<min_presidentage:
    print "Remember to Vote"
    
elif Age>=min_presidentage and Age<retirement_age:
    print "Vote for Me"
    
elif Age>=retirement_age:
    print "Too Old to Work"

#question7
value=39

while value<40:      
    print value
    if value==0:
        break 
    value-=3


#Question8
for i in range(6,30,1):
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                print i


#question9
n=0

while n<100:
    n+=1
    if (79*n)%97==1:
        print "Correct answer: ",n
        break
    print "Not Correct: ", n
        


