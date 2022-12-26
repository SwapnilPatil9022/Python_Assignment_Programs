# 10. Write a program which accept name from user and display length of its name.
#   Input : Marvellous          Output : 10

def Display(string):
	count = 0

	for i in range(0,len(string)):
		if(string[i] != ''):
			count = count + 1

	print("Total number of chararacter : " +str(count))

def main():
	print("----Application to calculate character program-----")

	value = (input("Enter the string\n"))

	Display(value)

if __name__ == "__main__":
	main()
