# Sets
# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
nameSet = set("my name is Mayank and Mayank is my name".split())
print(nameSet)
# This will print out a list containing "my", "name", "is", "Mayank", and finally "and".
# Since the rest of the sentence uses words which are already in the set, they are not inserted twice.

# Sets are a powerful tool in Python since they have the ability to calculate differences and
# intersections between other sets. For example, say you have a list of participants in events A and B:
print('Define two events')
eventA = set(['Ayush', 'Shivanshu', 'Mayank'])
print(eventA)
eventB = set(['Mayank', 'Sameer'])
print(eventB)
# To find out which members attended both events, you may use the "intersection" method:
print('+++++++++intersection+++++++++')
print(eventA.intersection(eventB))
print(eventB.intersection(eventA))
# To find out which members attended only one of the events, use the "symmetric_difference" method:
print('+++++++++symmetric_difference+++++++++')
print(eventA.symmetric_difference(eventB))
print(eventB.symmetric_difference(eventA))
# To find out which members attended only one event and not the other, use the "difference" method
print('+++++++++difference+++++++++')
print(eventA.difference(eventB))
print(eventB.difference(eventA))
# To receive a list of all participants, use the "union" method:
print('+++++++++union+++++++++')
print(eventA.union(eventB))
print(eventB.union(eventA))

# Exercise :
# In the exercise below, use the given lists to print out a set containing all the participants from event A
# which did not attend event B.
# Given
print("+++++++Exercise++++++++++++")
a = ['Ayush', 'Shivanshu', 'Mayank']
b = ['Mayank', 'Sameer']
A, B = set(a), set(b)
print(A.difference(B))
