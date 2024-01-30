from typing import List

# def printNos(x: int) -> List[int]:
#     ls = []
#     printUsingRecursion(x, ls)
#     return ls

# def printUsingRecursion(x, ls):
#     if x > 0:
#         printUsingRecursion(x - 1, ls)
#         ls.append(x)
# def printNos(x: int) -> List[int]: 
#     # Write your code here
      
#   ls=[]
#   ls2=[]
#   printUsingRecusrsion(x,ls,ls2)
#   return [ls,ls2]
  
# def printUsingRecusrsion(x,ls,ls2):
#     if x==0:
      
#       return 
    
#     else: 
#       ls.append(x)
#       printUsingRecusrsion(x-1,ls,ls2)
#       ls2.append(x)

# result = printNos(5)
# print(result)

# def printNos(x: int) -> list:
#     """Prints and returns a list of numbers from 1 to x in reverse order using recursion."""
#     if x == 0:
#         return []  # Base case: return an empty list

#     ans = printNos(x - 1)  # Recursive call to build the list for smaller numbers
#     ans.append(x)  # Append the current number to the list
#     return ans  # Return the completed list

# # Example usage
# def printNos(x: int) -> List[int]: 
#     # Write your code here
      
#   ls = printUsingRecusrsion(x)
#   return ls
  
# def printUsingRecusrsion(x):
#     if x==1:      
#       return [1] 
    
#     else: 
#       return [x]+printUsingRecusrsion(x-1)
# result = printNos(5)
# print(result)  # Output: [5, 4, 3, 2, 1]

# def printNos(x: int) -> List[int]:
#     ls = []
#     printUsingRecursion(x, ls)  # Pass the list as an argument
#     return ls

# def printUsingRecursion(x, ls):
#     if x == 1:
#         ls.append(1)  # Append to the list in the base case
#     else:
#         ls.append(x)  # Append before the recursive call
#         printUsingRecursion(x - 1, ls)

# def printNos(x: int) -> List[int]:
#     ls = []
#     printUsingRecursion(x, ls)
#     return ls

# def printUsingRecursion(x, ls):
#     if x == 1:
#         ls.append(1)
#     else:
#         printUsingRecursion(x - 1, ls)  # Recursive call first
#         ls.append(x)  # Append after the recursive call


# result = printNos(5)
# print(result)  # Output: [5, 4, 3, 2, 1]


# def myfunction(n):
#   if n == 0:
#     return n
#   else:
#     return myfunction(n-1)
    
# print(myfunction(5))

# def factorial(n):
#     if n == 0:
#         print(n, 1)
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         print(n, recurse, result)
#         return result
# print(factorial(5))

from  typing import *

# def printNtimes(n: int) -> List[str]:
#     str= "Coding Ninjas" 
#     if (n>0):        
#      printNtimes(n-1)
#      print(str,end=" " )

# def printNtimes(n: int) -> List[str]:
#     ls=[]
#     x= printX(n,ls)
#     print(x)
#     return x
# def printX(n,ls):
#     if n >0 :
#         printX(n-1,ls)
#         ls.append("Coding Ninjas")
#         return ls
# print(printNtimes(3))

def printNos(x: int) -> List[int]: 
    # Write your code here
    
    if x==0:
      return []
    else:
      return [x]+printNos(x-1)
      
print(printNos(3));
"""
By seeing various types of making recursive calls, 
I mean different types of call i made with different styles all I unserstand is we can either make recursive call beofre the recursive call happens,
Or after recursive call is happens.

One thing we have to understand is once the recursion hit the base case , how the control is going there appending values. 
the control flow goes to next statements and appends each value and returs the their values to main function call 


"""
