n=input("enter the string:")
string=n.lower()
print(string)
count=0
vowels=["a","e","i","o","u"]
for char in string:
    if char in vowels:
        count=count+1
print("the no of vowels in given sentence is:",count)
