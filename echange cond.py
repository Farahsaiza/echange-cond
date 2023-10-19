A=float(input("enter the first number"))
B=float(input("enter the second number"))
if (A>0 and B>0) or (A<0 and B<0):
    C=A
    A=B
    B=C
    print("the first number will be: ",  A)
    print("the second number will be :", B)
else :
    S=A+B
    P=A*B
    print("the first number will be :",S)
    print("the second number will be :",P)