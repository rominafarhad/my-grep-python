import sys

def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    
    elif pattern == r"\d":
        return any(char.isdigit() for char in input_line)

    elif pattern == r"\w":
        return any(char.isalnum() or char == "_" for char in input_line)

    elif pattern.startswith("[") and pattern.endswith("]"):
        if pattern.startswith("[^"):
            excluded_chars = pattern[2:-1]
            return any(char not in excluded_chars for char in input_line)
        else:
            allowed_chars = pattern[1:-1]
            return any(char in allowed_chars for char in input_line)

    # Stage 6: Start of string anchor (^)
    elif pattern.startswith("^"):
        remaining_pattern = pattern[1:] # Remove the ^
        # Check if input_line starts exactly with the remaining pattern
        return input_line.startswith(remaining_pattern)
        
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

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