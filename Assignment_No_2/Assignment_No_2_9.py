# Write a program which accept mumber from user and return addition of digits of that number.
#    input : 5187934        # output : 37

def Display(iNo):
    Sum = 0

    while(iNo != 0):
        Sum = Sum + (iNo % 10)
        iNo = iNo // 10

    print(Sum)

def main():
    no = int(input("Enter number : "))
    
    Display(no)

if __name__ == "__main__":
    main()
