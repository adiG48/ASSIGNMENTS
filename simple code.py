def get_sum(num):
    sum=0
    while (num != 0):
        sum=sum+(num % 10)
        num=num//10
    print("SUM OF THE DIGITS OF THE NUMBER",num,"IS",sum)
def get_rev(num):
    a=0
    while num>0:
        b=num%10
        a=(a*10)+b
        num=num//10
    print("THE REVERSE OF THE NUMBER",num,"IS",a)
def get_pali(num):
    rev=0
    s=num
    while num>0:
        a=num%10
        rev=rev*10+a
        num=num//10
    if s==rev:
        print(s,"IS PALINDROME!!")
    else:
        print(s,"NOT A PALINDROME")
    
num=int(input("number"))
c=int(input("ENTER YOUR CHOICE TO FIND\n1.sum of the digits\n2.reverse of the digit\n3.to check palindrome"))
if c==1:
    get_sum(num)
elif c==2:
    get_rev(num)
elif c==3:
    get_pali(num)
else:
    print("NOT A VALID INPUT")
