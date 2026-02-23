import sys

def match_line(input_line, pattern, captured_groups=None):
    if captured_groups is None:
        captured_groups = []
    
    if not pattern:
        return True

    # Handle Backreferences (\1, \2, ...)
    if len(pattern) > 1 and pattern[0] == '\\' and pattern[1].isdigit():
        group_index = int(pattern[1]) - 1
        if group_index < len(captured_groups):
            group_value = captured_groups[group_index]
            if input_line.startswith(group_value):
                return match_line(input_line[len(group_value):], pattern[2:], captured_groups)
        return False

    # Handle Grouping (abc)
    if pattern.startswith("("):
        end_paren = pattern.find(")")
        sub_pattern = pattern[1:end_paren]
        remaining_pattern = pattern[end_paren + 1:]
        
        # Try to match the sub_pattern and capture it
        for i in range(1, len(input_line) + 1):
            potential_match = input_line[:i]
            # Simple check for the group match
            if potential_match == sub_pattern: # Simplified for this stage
                if match_line(input_line[i:], remaining_pattern, captured_groups + [potential_match]):
                    return True
        return False

    # Handle '?' quantifier
    if len(pattern) > 1 and pattern[1] == '?':
        char_to_match = pattern[0]
        if input_line and (input_line[0] == char_to_match or char_to_match == '.'):
            if match_line(input_line[1:], pattern[2:], captured_groups):
                return True
        return match_line(input_line, pattern[2:], captured_groups)

    # Basic char match (including dot)
    if input_line and (pattern[0] == input_line[0] or pattern[0] == '.'):
        return match_line(input_line[1:], pattern[1:], captured_groups)
        
    return False

def match_pattern(input_line, pattern):
    if '|' in pattern:
        for option in pattern.split('|'):
            if match_pattern(input_line, option): return True
        return False

    if pattern.startswith("^"):
        return match_line(input_line, pattern[1:])
    
    if pattern.endswith("$"):
        return input_line.endswith(pattern[:-1])

    for i in range(len(input_line) + 1):
        if match_line(input_line[i:], pattern):
            return True
    return False

def main():
    if len(sys.argv) < 3: exit(1)
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    if match_pattern(input_line, pattern): exit(0)
    else: exit(1)

if __name__ == "__main__":
    main()