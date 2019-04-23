f = open('tm.txt', 'r')
text = f.read()
f.close()

# Count all letters and punctuation
letterCount = dict()
for letter in text:
    letter = letter.lower() # convert to lower case

    # Skip some types of punctuation by ending the loop early
    if letter == ' ' or letter == '\n':
        continue

    if letter in letterCount:
        letterCount[letter] += 1
    else:
        letterCount[letter] = 1
    
# Sort by number of occurrences, by converting to a list
letterList = list(letterCount.items())
letterList.sort(key=lambda x: x[1], reverse=True)

# Print out most common letters/symbols alongside their counts
for letter, count in letterList:
    print("%s, %d" % (letter, count))

