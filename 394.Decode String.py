s = "3[a]1[bc]ef"
stack = []
current_str = ""
num = 0


for char in s:
    if char.isdigit():
        num = num * 10 + int(char)
    elif char == "[":
        stack.append((current_str, num))
        current_str = ""
        num = 0
    elif char == "]":
        prev_string , repeat_num = stack.pop()
        current_str = prev_string + current_str * repeat_num
    else:
        current_str += char

print(current_str)

