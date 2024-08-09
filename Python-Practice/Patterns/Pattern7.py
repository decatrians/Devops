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

for i in range(0,n):
    for j in range(1,n-i):
        print(end=" ")
    for j in range(0,2*i+1):
        if (j==0 or j== 2*i or i== n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,n):
    for j in range(0,i):
        print(end=" ")
    for j in range(0,2*(n-i)-1):
        if (j==0 or j== (2*(n-i)-2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()