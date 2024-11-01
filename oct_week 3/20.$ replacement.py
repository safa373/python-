str=input("Enter the string")
print("the original string is:",str)
s='$'
new_str=str.replace(str[0],s).replace(s,str[0],1)
print("replaced string:",new_str)
