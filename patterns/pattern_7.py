def pattern_7(num):

    for row in range(1,2*num):
       col= row
       while  col < 2*num:
            print("*",end=" ")
            col+=1
       print('')
        

pattern_7(5)
