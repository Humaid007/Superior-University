def sort_words(text):
 
  words = text.split()
  sorted_words = []

  while words:
    smallest_word = words[0]
    for word in words:
      if word < smallest_word:
        smallest_word = word

    sorted_words.append(smallest_word)
    words.remove(smallest_word)

  return " ".join(sorted_words)

user_input = input("Enter a sentence: ")
output = sort_words(user_input)
print(f"Input: {user_input}")
print(f"Output: {output}")