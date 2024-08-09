'''
Enter number of rows:4
    *
   * *
  *   *
 *******
  *   *
   * *
    *
 using if-else
'''

n=int(input("Enter number of rows:"))

for i in range(0,n-1):
    print(' ' * (n-i-1) ,end="")
    print("*",end="")
    if(i>0):
        print(' ' * (2*i-1),end="")
        print("*",end='')
    print()
print('*' * (2*n-1))
for i in range(1,n):
    for j in range(0,i):
        print(end=" ")
    for j in range(0,2*(n-i)-1):
        if (j==0 or j== (2*(n-i)-2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()