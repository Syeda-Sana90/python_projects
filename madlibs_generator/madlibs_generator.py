with open("story.txt","r") as f:
    story = f.read()        # read all story

words = set()        # set does not show duplicated words
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): # enumerate give us to access to the position as well as the element at that position.   
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i +1]           # slice
        words.add(word)
        start_of_word = -1

answer = {}         # dictionary

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answer[word] = answer

for word in words:
    story = story.replace(word, answer[word])

print(story)

