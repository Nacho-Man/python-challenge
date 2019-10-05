import os
import csv
import re
# set the path
data_csv = os.path.join('paragraph.csv')

data_in = input('Enter in text. (Type "example" to use example.txt) \n')
data_csv = os.path.join(data_in)
if data_in == "example":
    data_csv = os.path.join('paragraph.csv')
 

text = []
word_count = 0
#treat as csv
if data_in == "example":
    with open(data_csv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ")
        for line in csvreader:
            text.append(line)

full_string = ''
sent_err = 0

if data_in != "example":
    full_string = data_in
    text = data_in    

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
space_count = 0
for char in full_string:
    char_count = char_count + 1
    if char == '.' or char == '?':
        sent_count = sent_count + 1
    if char == ' ':
        space_count = space_count + 1
sent_count = sent_count - sent_err
#the_str = re.split("(?<=[.!?]) +", word)
#the_str  = re.split(r'[ \t\r\f\v]*\n[ \t\r\f\v]*\n[ \t\r\f\v]*', full_string)
#sent = full_string.find(". ")
if data_in != "example":
    full_string = data_in
char_wo = char_count - word_count

avg_letter = char_wo / word_count
avg_sent_len = 0
if sent_count != 0:
    avg_sent_len = word_count / sent_count
print("--------------------")
print("Full Text")
print("--------------------")
print(full_string)
print("--------------------")
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sent_count}")
print(f"Average Letter Count: {round(float(avg_letter), 1)}")
print(f"Average Sentence Length: {round(float(avg_sent_len), 1)}")