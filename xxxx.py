def hollow_square(n):
    # Top side of the square with spaces between stars
    if n > 1:
        print("* " + "  " * (n - 2) + "*")
    else:
        print("*")
    
    # Middle part of the square (if n > 2 to have space in between)
    for i in range(n - 2):
        print("*" + " " * (2 * (n - 2) + 1) + "*")
    
    # Bottom side of the square with spaces between stars (only if n > 1)
    if n > 1:
        print("* " + "  " * (n - 2) + "*")

# Test with the example input
hollow_square(4)
