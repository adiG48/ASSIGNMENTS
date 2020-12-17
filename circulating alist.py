list=[1,2,3,4,5]
n=int(input("Enter The Value of N:"))
list1=list[n:len(list)+1]
m=list[:n]
list2=list1+m
print("The Circulate of the list for",n,"time is",list2)