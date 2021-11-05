N=int(input("enter a number:"))
even=0
odd=0
for i in range (1,N+1):
    if i % 2 ==0 :
        even = even+i
    else :
        odd= odd + i
print("sum of ods",odd)
print("average of evens",even/(even+odd))