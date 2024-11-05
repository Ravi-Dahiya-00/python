num = 1  # Start number

for i in range(6):  # Loop for each row (adjust range for more rows)
    for j in range(i):  # Loop to print numbers in each row
        print(num, end="    ")  # Print the number with spaces
        num += 1  # Increment the number
    print()  # Move to the next line after each row