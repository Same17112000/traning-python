def most_common_word(string):
    words = string.lower().split()

    word_Counts = {}
    for word in words:
        if word in word_Counts:
            word_Counts[word] += 1
        else:
            word_Counts[word] = 1
    
    max_Count = 0
    most_common_word = None
    for word, count in word_Counts.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    return most_common_word, max_count

string = input()

most_common_word, count = most_common_word(string)

print(f"The most common word is '{most_common_word}' appearing {count} times.")
