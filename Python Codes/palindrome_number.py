num = int(input("Enter number : "))

nno = num

rno = 0

while(nno > 0):
    d = nno % 10
    rno = rno * 10 + d
    nno = nno // 10

if(rno == num):
    print(num, " is Palindrome")
else:
    print(num, " is not Palindrome!")
