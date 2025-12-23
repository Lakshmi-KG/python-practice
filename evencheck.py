#program check whether the given number is even or odd
#1: take a number n
n=int(input("enter a number"))
#2: check whether n is divisible by 2. if remainder o-> even,else odd
if n%2==0:
    print(f"given number {n} id even")
else:
    print(f"given number {n} is odd")

