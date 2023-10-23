n = int(input("Enter the Number: "))
while(n>=10):
    x = n
    s = 0
    while(x>0):
        s = s+(x%10)
        x = x//10
    n = s
print("Super Digit of The given Numbers", n)