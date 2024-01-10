
def pattern_5(num):
    for i in range(num+1,0,-1):
        for j in range(i) :
            print(j , end=" ")
        print()
        

pattern_5(5)

"""
Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

"""