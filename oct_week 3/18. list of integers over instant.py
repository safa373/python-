list=int(input("Enter the number of integers to input:"))
integers=[]
for i in range(list):
    integer=int(input("Enter the number of integers:"))
    integers.append(integer)
    if(integer>50):
        integers[i]="over"
print(integers)
