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

    # Stage 4 & 5: Character Groups [abc] and [^abc]
    elif pattern.startswith("[") and pattern.endswith("]"):
        if pattern.startswith("[^"):
            excluded_chars = pattern[2:-1]
            return any(char not in excluded_chars for char in input_line)
        else:
            allowed_chars = pattern[1:-1]
            return any(char in allowed_chars for char in input_line)

    # Stage 6: Start of string anchor (^)
    elif pattern.startswith("^"):
        remaining_pattern = pattern[1:]
        return input_line.startswith(remaining_pattern)

    # Stage 7: End of string anchor ($)
    elif pattern.endswith("$"):
        required_end = pattern[:-1] # Remove the $ from end
        return input_line.endswith(required_end)
        
    else:
        # If it's none of the above, just check if pattern is in the string
        return pattern in input_line

def main():
    if len(sys.argv) < 3:
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()