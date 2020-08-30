eng_words = []
with open("words.txt") as word_txt_file:
    for word in word_txt_file:
        eng_words.append(word.rstrip("\n"))

eng_words.sort()
print(eng_words)
        


##import os
##import csv

##filenames = os.listdir(os.curdir)
##filenames.remove('make_a_single_csv.py')
##filenames.remove('words.csv')
##filenames.sort()

##words = []
##rawrows = []
##
##for filename in filenames:
##    with open(filename) as csv_file:
##        word_reader = csv.reader(csv_file, delimiter=' ')
##        print(filename)
##        letterwords = []
##        for row in word_reader:
##            try:
##                rawrows.append(row)
##                word = row[0]
##                
##                if word.isalnum() and word not in letterwords:
##                    letterwords.append(word)
##                    words.append(word)
##            except:
##                print("Tried to get word but failed.")
##                print(row)
##
##with open('words.csv', 'w', newline='') as csvfile:
##    word_writer = csv.writer(csvfile, delimiter = ',')
##    for word in words:
##        word_writer.writerow([word])

    
