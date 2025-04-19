# 
for i in range(5):
    print(i)


# 
for i in range(1,6):
    print(i)

# 
for i in range(1,10,2):
    print(i)

# 
for i in range(10,1,-1):
    print(i)

# 
for i in range(10,1,-2):
    print(i)

# strings
str="Krish Naik"

for i in str:
    print(i)

# Nested loopss
## a loop inside a loop

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")

# Example- Prime numbers between 1 and 100

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

# Examples- Calculate the sum of first N natural numbers using a while and for loop

## while loop  

n=10   
sum=0
count=1

while count<=n:
    sum=sum+count
    count=count+1

print("Sum of first 10 natural number:",sum)