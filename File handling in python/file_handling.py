def process_file(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    # Attempt to convert each line to an integer
                    number = int(line.strip())  # Remove leading/trailing whitespace
                    print(f"Number: {number}")
                except ValueError:  # Catch the error if it's not a number
                    print(f"Skipping non-integer line: {line.strip()}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Use "example.txt" as the file name
file_name = "example.txt"  # You can replace this with your actual file name if needed

# Call the function with the file name "example.txt"
process_file(file_name)
