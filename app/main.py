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

    # Stage 4: Positive Character Groups [abc]
    # Check if pattern starts with [ and ends with ]
    elif pattern.startswith("[") and pattern.endswith("]"):
        allowed_chars = pattern[1:-1] # Get characters inside []
        return any(char in allowed_chars for char in input_line)
        
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