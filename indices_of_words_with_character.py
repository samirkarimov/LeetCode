def indices_of_words_with_character(words, x):
    indexes=[]
    for index in range(len(words)):
        if x in words[index]:
            indexes.append(index)
    return indexes


# Example usage:
words = ["apple", "banana", "ornge", "grape"]
character_to_find = "a"
result_indices = indices_of_words_with_character(words, character_to_find)

print(result_indices)
