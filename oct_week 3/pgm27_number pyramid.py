n=int(input("Enter the no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        product=i*j
        print(product,end=" ")
    print()
