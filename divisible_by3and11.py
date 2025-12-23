#program to check whether given number is divisible by both 3 and 11 or not
#1: take a number
n=int(input("enter a number"))
#2: check whether n is divisible by 3 and 11 or not
if n%3==0 & n%11==0:
    print(f"the given number {n} is divisible by 3 and 11")
else:
    print(f"the given number is {n} is not divisible by 3 and 11 ")
