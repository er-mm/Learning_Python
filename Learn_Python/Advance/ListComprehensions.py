# List Comprehensions
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
# let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
# first we are trying to solve this using lists
sentence = "the quick brown fox jumps over the lazy dog"
words_list = sentence.split()
print(words_list)
print('length of word list array = %d.' % len(words_list))
lenOfList = []
for word in words_list:
    if word != 'the':
        lenOfList.append(len(word))
print(lenOfList)
print('length of lenOfList array = %d.' % len(lenOfList))

# Using a list comprehension, we could simplify this process to this notation:
print('Find length using list comprehensions')
lenOfComprehensionList = [len(word) for word in words_list if word != 'the']
print(lenOfComprehensionList)

# Exercise
# Using a list comprehension, create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.
# given the nummbers  are :
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [posNum for posNum in numbers if posNum > 0]
print('====Exercise====')
print(newlist)
newlistAsIntegers = [int(posNum) for posNum in numbers if posNum > 0]
print('====newlistAsIntegers====')
print(newlistAsIntegers)


