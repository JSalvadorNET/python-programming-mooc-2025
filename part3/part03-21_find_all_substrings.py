word = input("Please type in a word: ")
char = input("Please type in a character: ")

# Percorre toda a palavra procurando a letra
for i in range(len(word)):
    if word[i] == char:
        if i <= len(word) - 3:  # Garante que há pelo menos 3 caracteres disponíveis
            print(word[i:i+3])
