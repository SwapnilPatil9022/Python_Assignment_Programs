# Write a program which accept one number and display below pattern.
#      * * * * *
#      * * * * 
#      * * * 
#      * * 
#      * 

def Display(no):

    for i in range(0,no):
        for j in range(0,no):
            if(i <= j):
                print("*",end=" ")

        print()

def main():
    no = int(input("Enter number : "))
    
    Display(no)

if __name__ == "__main__":
    main()
