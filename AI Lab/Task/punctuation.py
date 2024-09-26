def remove_punctuation(text):
  
  result = ''
  for char in text:
    if char.isalnum() or char.isspace():
      result += char
  return result

user_input = input("Enter a string: ")
output = remove_punctuation(user_input)
print(f"Input: {user_input}")
print(f"Output: {output}")