sentence = input("Enter a sentence: ")
search_word = input("Enter the word to search for: ")
word_count = len(sentence)
word_found = search_word in sentence
print("Number of words in the sentence:",word_count)
if word_found:
    print("The word is present in the sentence:",search_word)
else:
    print(f"The word is not present in the sentence:",search_word)
