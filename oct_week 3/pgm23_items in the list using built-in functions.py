list1=input("Enter the list:")
list2=list(map(int,list1.split()))
sort1=sorted(list2)
print("Sorted list:",sort1)
max1=max(list2)
print("Maximum value:",max1)
min1=min(list2)
print("Minimum value:",min1)
sort1.reverse()
print("Reverse:",sort1)
count=len(list2)
print("Length of list:",count)
sum=sum(list2)
print("Sum of list:",sum)
