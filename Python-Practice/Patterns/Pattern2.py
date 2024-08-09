'''
Enter number of rows:4
4
33
222
1111
'''

n=int(input("Enter number of rows:"))

for i in range(1,n+1):
    print(str(n-i+1) * i)