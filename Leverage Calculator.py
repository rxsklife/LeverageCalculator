# Text art for Risky Biz Leverage Calculator
print("""

██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗  ██████╗░██╗███████╗
██╔══██╗██║██╔════╝██║░██╔╝╚██╗░██╔╝  ██╔══██╗██║╚════██║
██████╔╝██║╚█████╗░█████═╝░░╚████╔╝░  ██████╦╝██║░░███╔═╝
██╔══██╗██║░╚═══██╗██╔═██╗░░░╚██╔╝░░  ██╔══██╗██║██╔══╝░░
██║░░██║██║██████╔╝██║░╚██╗░░░██║░░░  ██████╦╝██║███████╗
╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝╚══════╝

████████╗██████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
░░░██║░░░██████╔╝███████║██║░░██║██║██╔██╗██║██║░░██╗░
░░░██║░░░██╔══██╗██╔══██║██║░░██║██║██║╚████║██║░░╚██╗
░░░██║░░░██║░░██║██║░░██║██████╔╝██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝   
""")
print("By: @rxsklife | trade responsibly :p")
print("\033[33mInstructions: Type any amount that ends in '0'\n\033[0m")


# Function to find multiplication combinations
def find_multiplication_combinations(num):
    print("\nLeverage:")
    for i in range(1, num):
        for j in range(1, num):
            if i*j == num:
                if i % 10 == 0 or j % 10 == 0:
                    # Check if the leverage is within limit
                    if i <= 100:
                        print("{:,}X on ${:,}".format(i, j))

                        # Flush the output buffer to ensure live printing
                        import sys
                        sys.stdout.flush()
                    else:
                        # Stop calculating once 100x leverage has been printed
                        return

# User input for initial total volume
num = int(input("Total Volume: $"))

# Call function with initial user input
find_multiplication_combinations(num)

# Loop to allow user to run again
while True:
    rerun = input("\nRun again? (Y/N): ")
    if rerun.lower() != 'y':
        break
    num = int(input("Total Volume: $"))
    find_multiplication_combinations(num)





