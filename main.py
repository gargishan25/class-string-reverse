word = input("Enter a word. ")
list_word = []
for i in range((len(word)-1),-1,-1):
    list_word.append(word[i])
word = "".join(list_word)
print(word)