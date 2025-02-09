def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
