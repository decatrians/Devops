'''
Enter number of rows:4
    *
   ***
  *****
 *******
  *****
   ***
    *
'''

n=int(input("Enter number of rows:"))

for i in range(0,n):
    for j in range(1,n-i):
        print(end=" ")
    print("*" * (2*i+1))

for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(end=" ")
    print("*" * (2*i-1))