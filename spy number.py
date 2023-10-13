sum = 0
prod =1
n=int(input("Enter the number: "))
while(n>0):
    r= n%10
    sum=sum+r
    prod = prod+r
if(sum == prod):
    print("Given no. is Spy Number")
else:
    print("Given no. is a Spy number")