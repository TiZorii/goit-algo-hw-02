def check_balanced_symbols(s):
    stack = []
    opening = {'(': ')', '[': ']', '{': '}'}
    closing = {')', ']', '}'}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if opening[top] != char:
                return "Несиметрично"
    
    if stack:
        return "Несиметрично"
    return "Симетрично"

# Тести
test_cases = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for test in test_cases:
    print(f"{test}: {check_balanced_symbols(test)}")
