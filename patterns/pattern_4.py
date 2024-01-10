

def pattern_4(num):
    for i in range(num+1,0,-1):
        for j in range(i) :
            print("*" , end=" ")
        print()
        

pattern_4(5)




"""
Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 
"""