'''
Enter number of rows:4
1
22
333
4444
'''

n=int(input("Enter number of rows:"))

for i in range(1,n+1):
    print(str(i) * i)