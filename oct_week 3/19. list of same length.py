list1=input("enter the first list separated by spaces:").split()
list2=input("enter the second list separated by spaces:").split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list2)):
    list2[i]=int(list2[i])
if (len(list1)==len(list2)):
    print("list are of same length")
else:
    print("list are of different length")
if (sum(list1)==sum(list1)):
    print("list sum to same value")
else:
    print("list sum to different value")
common_values=set(list1)&set(list2)
if common_values:
    print("Common_values:",common_values)
else:
    print("no common_values")
