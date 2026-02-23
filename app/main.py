import sys

# Function to check if the pattern exists in the input_line
def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        # Stage 1: Check if a single character exists in the input
        return pattern in input_line
    
    elif pattern == r"\d":
        # Stage 2: Check if the input contains any digit (0-9)
        # We iterate through each character to see if it's a digit
        for char in input_line:
            if char.isdigit():
                return True
        return False
        
    else:
        # Raising error for patterns not yet implemented
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def main():
    # Ensure there are enough arguments
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh -E <pattern>")
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Call the matching logic
    if match_pattern(input_line, pattern):
        exit(0) # Match found
    else:
        exit(1) # No match found

if __name__ == "__main__":
    main()