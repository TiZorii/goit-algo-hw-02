from collections import deque

def is_palindrome(s):
    # Видалити пробіли та привести до нижнього регістру
    s = ''.join(s.split()).lower()
    # Додати символи до двосторонньої черги
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Тест
test_string = "A man a plan a canal Panama"
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")
