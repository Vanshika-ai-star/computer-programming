# Capitalize the first letter of each word in a string.
sentence = "capitalize each word"
capitalized_sentence = " ".join(word[0].upper() + word[1:] for word in sentence.split())
print(capitalized_sentence)  
