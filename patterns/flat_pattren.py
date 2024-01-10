def flat_pattern(num):
    for i in range(num):
        for j in range(num):
            print("*" , end=" ")
        print()

flat_pattern(5)