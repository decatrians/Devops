check_num=int(input("Enter Number:"))
def check_prim_not(num):
  if (num<2):
      return False
  else:
      for i in range(2,int(num**0.5)+1):
          if check_num%i==0:
             return True
  

prime_checker=check_prim_not(check_num)
if (prime_checker):
   print("Given number is not prime number")
else:
   print("Given Number is Prime number")