from collections import Counter
arr = [1,2]
frequencies = Counter(arr)

if len(frequencies.values()) == len(set(frequencies.values())):
    print('True')
else:
    print('False')