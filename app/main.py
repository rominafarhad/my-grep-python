import sys

# Function to check if the pattern exists in the input_line
def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        # Stage 1: Check if a single character exists in the input
        return pattern in input_line
    else:
        # Raising error for patterns not yet implemented
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def main():
    # Ensure the first argument is -E
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Extract pattern and input data
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    # Call the matching logic
    if match_pattern(input_line, pattern):
        exit(0) # Success: Match found
    else:
        exit(1) # Failure: No match found

if __name__ == "__main__":
    main()