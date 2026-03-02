#To check the given number is binary or not

n='1010'
for i in n:
    if i!='0' and i!='1':
        print("Not Binary")
        break 
else:
    print("Binary")