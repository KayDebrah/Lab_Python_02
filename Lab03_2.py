num=raw_input("Enter Number: ")
number=int(num)

num1=0
length=len(num)
while num1<length:
    length=length-1
    numdisplay=int(num[length])
    soln=(numdisplay+7)%10
    print soln ,
    

