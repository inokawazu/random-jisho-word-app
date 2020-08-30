eng_words = []
with open("words.txt") as word_txt_file:
    for word in word_txt_file:
        eng_words.append(word.rstrip("\n"))