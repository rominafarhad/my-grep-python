import sys

def match_line(input_line, pattern):
    # If pattern is empty, it's a match
    if not pattern:
        return True
    
    # Handle the '+' quantifier
    if len(pattern) > 1 and pattern[1] == '+':
        char_to_repeat = pattern[0]
        remaining_pattern = pattern[2:]
        
        # Must match at least one instance
        if not input_line or input_line[0] != char_to_repeat:
            return False
            
        # Check all possible repetitions
        i = 0
        while i < len(input_line) and input_line[i] == char_to_repeat:
            if match_line(input_line[i+1:], remaining_pattern):
                return True
            i += 1
        return False

    # Basic character matching
    if input_line and (pattern[0] == input_line[0] or pattern[0] == '.'):
        return match_line(input_line[1:], pattern[1:])
        
    return False

def match_pattern(input_line, pattern):
    # Stage 6: Start anchor
    if pattern.startswith("^"):
        return match_line(input_line, pattern[1:])
    
    # Stage 7: End anchor
    if pattern.endswith("$"):
        # This is a simple way for the end anchor
        return input_line.endswith(pattern[:-1])

    # For other stages (d, w, groups), we'll keep our previous simple logic
    # But for a real engine, we try to match at every position:
    for i in range(len(input_line) + 1):
        if match_line(input_line[i:], pattern):
            return True
    return False

# Keep your main() function the same as before
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