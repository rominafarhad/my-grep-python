import sys

def match_line(input_line, pattern):
    if not pattern:
        return True
    
    # Handle '?' quantifier
    if len(pattern) > 1 and pattern[1] == '?':
        char_to_match = pattern[0]
        remaining_pattern = pattern[2:]
        if input_line and (input_line[0] == char_to_match or char_to_match == '.'):
            if match_line(input_line[1:], remaining_pattern):
                return True
        return match_line(input_line, remaining_pattern)

    # Handle '+' quantifier
    if len(pattern) > 1 and pattern[1] == '+':
        char_to_repeat = pattern[0]
        remaining_pattern = pattern[2:]
        if not input_line or (input_line[0] != char_to_repeat and char_to_repeat != '.'):
            return False
        i = 0
        while i < len(input_line) and (input_line[i] == char_to_repeat or char_to_repeat == '.'):
            if match_line(input_line[i+1:], remaining_pattern):
                return True
            i += 1
        return False

    # Basic char match (including dot)
    if input_line and (pattern[0] == input_line[0] or pattern[0] == '.'):
        return match_line(input_line[1:], pattern[1:])
        
    return False

def match_pattern(input_line, pattern):
    # Stage 11: Alternation (|)
    # Check if '|' is in pattern (simplified for basic cases)
    if '|' in pattern:
        options = pattern.split('|')
        for option in options:
            if match_pattern(input_line, option):
                return True
        return False

    if pattern.startswith("^"):
        return match_line(input_line, pattern[1:])
    
    if pattern.endswith("$"):
        return input_line.endswith(pattern[:-1])

    # Try matching at every possible starting position
    for i in range(len(input_line) + 1):
        if match_line(input_line[i:], pattern):
            return True
    return False

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