#program to check whether given char is vowel or not
#1: take single character th
ch=input("enter a character")
ch.lower()
#2: check whether ch is a,e,i,o,u.if then print vowel else consonant
if len(ch)==1:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print(f"the character {ch} is vowel")
    else:
        print(f"the character {ch} is consonant")
else:
    print("please a single character input")



