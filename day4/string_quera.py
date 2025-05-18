def string_operations(text: str, operation: str):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    if operation == "reverse":
        return text[::-1]
    elif operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "count_vowels":
        vowel_count = 0
        for char in text:
            if char in vowels:
                vowel_count += 1
        return vowel_count
    elif operation == "is_palindrome":
        return text == text[::-1]
    else:
        return "Invalid operation"
    
# Example usage
text = input().strip()
operation = input().strip()
print(string_operations(text, operation))

