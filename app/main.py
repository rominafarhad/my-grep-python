import sys

def match_pattern(input_line, pattern):
    # Stage 1: Single character match
    if len(pattern) == 1:
        return pattern in input_line
    
    # Stage 2: Digit character class (\d)
    elif pattern == r"\d":
        return any(char.isdigit() for char in input_line)

    # Stage 3: Word character class (\w)
    elif pattern == r"\w":
        return any(char.isalnum() or char == "_" for char in input_line)

    # Stage 4 & 5: Positive and Negative Character Groups
    elif pattern.startswith("[") and pattern.endswith("]"):
        if pattern.startswith("[^"):
            # Negative: Match any character NOT in the brackets
            excluded_chars = pattern[2:-1]
            return any(char not in excluded_chars for char in input_line)
        else:
            # Positive: Match any character IN the brackets
            allowed_chars = pattern[1:-1]
            return any(char in allowed_chars for char in input_line)
        
    else:
        # Fallback for patterns we haven't implemented yet
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def main():
    # Ensure there are enough arguments
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh -E <pattern>")
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    # The first argument must be -E
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Core logic to determine if the pattern matches the input
    if match_pattern(input_line, pattern):
        exit(0) # Success: Match found
    else:
        exit(1) # Failure: No match found

if __name__ == "__main__":
    main()