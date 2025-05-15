s = "the sky is blue"
words = s.split()
# stack = []
# reverse = []
# for word in words:
#     stack.append(word)
# while stack:
#     reverse.append(stack.pop())
#
# print(" ".join(reverse))
#

words = s.split()[::-1]
print(" ".join(words))