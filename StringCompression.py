chars = ["a","a","b","b","c","c","c"]

read = 0
write = 0

while read<len(chars):
    char = chars[read]
    count = 0
    while read<len(chars) and chars[read] == char:
        count +=1
        read += 1

    chars[write] = char
    write +=1

    if count>1:
        for digit in str(count):
            chars[write] = digit
            write += 1

print(chars[:write])
print(write)