num=  int(input("Enter the number :"))
flag = 0 # to check the number
for n in range(num + 1):
    if(n*(n+1)== num):
        flag = 1
        break
if(flag == 1):
    print(num,"is a Pronic Number as it is the product oftwo consecutive number :",n, "and",n+1)
else:
    print(num,"is Not a Pronic Number")