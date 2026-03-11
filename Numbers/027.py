#Convert Decimal number to Binary number with built-in function
n=8
print(bin(n))

#Convert Decimal number to Octal number with built-in function
n=8
print(oct(n))

#Convert Decimal number to Binary number without built-in function
decimal=8
binary=""
if binary==0:
    binary="0"
while decimal>0:
    remainder=decimal%2
    binary=str(remainder)+binary
    decimal=decimal//2
print(binary)

#Convert Decimal number to Octal number without built-in function
decimal=64
octal=""
if octal==0:
    octal="0"
while decimal>0:
    remainder=decimal%8
    octal=str(remainder)+octal
    decimal=decimal//8
print(octal)