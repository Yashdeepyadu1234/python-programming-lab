
##10) write a python program to print the following pattern
##   *****
##   *****
##   *****
##   *****
##   *****
##   **********
##   **********
##   **********
##   **********
##   **********

n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
for i in range(1,(n)+1):
    for j in range(1,2*n+1):
        print("*",end="")
    print()
