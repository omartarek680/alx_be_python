pattern = int(input("Enter the size of the pattern: "))
counter = pattern
while counter > 0:
    for i in range(0,pattern):
        print("*",end='')
    print("")    
    counter = counter -1    