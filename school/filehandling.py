f=open("abcd.txt","r")
data=f.read()
print(data)
f.close()


f=open("abcd.txt","r")
line1=f.readline()
print(line1,end="")
line2=f.readline()


f=open("abcd.txt","r")
print(f.read(3))
print(f.readline())
print(f.read(4))
print("remaining data")
print("")


with open("abcd.txt","w") as f:
    f.write("Durga\n")
    f.write("Software\n")


f=open("abcd.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())



data="all students are Stupids"
f=open("abcd.txt","r+")
f.write(data)
with open("abcd.txt","r+") as f:
    text=f.read()
    print(text)
    print("The Current Cursor Position:",f.tell())
    f.seek(17)
    print("The Current Cursor Position")
    f.write("Gems!!!!")
    f.seek(0)
    text=f.read()
    print("Data After Modification")
    
    
    
    
    
    
    
    
     
import sys

def process_hidden_cases():
    try:
        # Step 1: Read all input at once (efficient for large inputs)
        inputs = sys.stdin.read().splitlines()

        # Step 2: Open a file to log test cases and solutions
        with open("hidden_cases_log.txt", "a") as log_file:
            solutions = []

            # Step 3: Process each input case
            for test_input in inputs:
                if test_input.strip():  # Ensure the input is not empty
                    # Example program logic: replace this with actual logic
                    # Assuming inputs are two space-separated integers
                    a, b = map(int, test_input.split())
                    solution = a * b  # Example: Multiplying the numbers
                    solutions.append(solution)

                    # Log input and output for debugging
                    log_file.write(f"Input: {test_input}, Output: {solution}\n")

            # Step 4: Print solutions for platform validation
            for solution in solutions:
                print(solution)

    except Exception as e:
        # Handle errors gracefully
        print(f"Error occurred: {e}", file=sys.stderr)

# Execute the function
if __name__== "_main_":
    process_hidden_cases()