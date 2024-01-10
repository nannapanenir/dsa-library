
def right_angle_triangle(num):
    for i in range(1,num):
        for j in range(1,num):
            if j==(num-i):
                print("*"*i, end="")
            else:
                print(" ", end="")
        print('')

right_angle_triangle(5)

"""
right angle tri-angle 
   *
  ** 
 ***
****

if you add space astric it will give star pyrmid

"""