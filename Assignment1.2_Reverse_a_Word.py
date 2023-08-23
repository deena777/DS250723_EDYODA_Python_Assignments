
# Write a Python program that accepts a word from the user and reverse it.

print()
word = input("Enter a word to reverse: ")
print("Length of word:",len(word))
reversed_word = ""
for i in range(len(word)-1,-1,-1):
    reversed_word += word[i]   
print("Reversed word:", reversed_word,"\n")