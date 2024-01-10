
def star_pyramid(num):
    for i in range(num):
        
        for j in range(i+2):        
            print("*", end=" ")
        print()


star_pyramid(5)



"""
Input Format: N = 6
Result:
     *     
    ***    
   *****   
  *******  
 ********* 
***********

"""