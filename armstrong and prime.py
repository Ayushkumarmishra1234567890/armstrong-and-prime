#armstrong number
n=int(input())
n1=n
s=0
while n>0:
    l=n%10
    s=s+(l**3)
    n=n//10
if(n1==s):
    print("Armstrong number")
else:
    print("Not Armstrong number")

#prime number
n=int(input("n: "))
i=2
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
        break
if(c==0):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
