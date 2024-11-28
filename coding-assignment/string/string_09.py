# 7. Find the longest word in a sentence.
sentence = "Find the longest word here"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word) 
