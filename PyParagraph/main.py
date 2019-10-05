import os
import csv
import re
# set the path
data_csv = os.path.join('paragraph.csv')

#data_in = input('Enter in text. (Type "example" to use example.txt')
#data_csv = os.path.join(data_in)
#if data_in = example
    #data_csv = os.path.join('paragraph.csv')
 

text = []
word_count = 0
#treat as csv
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=" ")
    for line in csvreader:
        text.append(line)

full_string = ''
sent_err = 0
abrev = ["Dr.", "Mr.", "Mrs.", "vs.", "Apt."]
for line in text:
    for word in line:
        full_string += word + " "
        for err in abrev:
            if err == word:
                sent_err = sent_err + 1
        word_count = word_count + 1
    word += '\n'

char_count = 0
sent_count = 0
for char in full_string:
    char_count = char_count + 1
    if char == ".":
        sent_count = sent_count + 1
sent_count = sent_count - sent_err
#the_str = re.split("(?<=[.!?]) +", word)
the_str  = re.split(r'[ \t\r\f\v]*\n[ \t\r\f\v]*\n[ \t\r\f\v]*', full_string)
sent = full_string.find(". ")


avg_letter = char_count / word_count
avg_sent_len = word_count /sent_count
print("--------------------")
print("Full Text")
print("--------------------")
print(full_string)
print("--------------------")
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sent_count}")
print(f"Average Letter Count: {avg_letter}")
print(f"Average Sentence Length: {avg_sent_len}")