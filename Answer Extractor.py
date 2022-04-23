import pyperclip as pc
# Get multiline input from user and store as string
lines = []
print("Enter your lines below:")
try:
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
except:
    pass

# Initialising different list variables for storing stuff
lst = []
old = []
final = []
# takes each line and only saves the important stuff leaving the rest
# old and new cause more than one correct option stuff is annoy, so you have to edit the past
for line in lines:
    if not line[0].isalpha():
        for char in line:
            if char.isdigit() and len(lst) == 0:
                lst.append(char)
                # print(old)
                final.append(old)
            elif char.isdigit():
                lst[0] += char
            if char.isalpha() and len(lst) == 0:
                old[1] += char.upper()
            elif char.isalpha():
                lst.append(char.upper())
                old = list(lst)
                # print(lst)
                final.append(lst)
                lst = []
final.append(old)

# editing to remove duplicates
edit = []
for row in range(len(final)):
    try:
        if final[row][0] != final[row + 1][0] and final[row] not in edit:
            edit.append(final[row])
            continue
        elif len(final[row + 1][1]) > len(final[row][1]):
            edit.append(final[row + 1])
    except:
        pass
if len(old[1]) == 1:
    # noinspection PyUnboundLocalVariable
    edit.append(final[row])

# Copying things to clipboard for instant pasting
out = ""
for row in edit:
    out += row[1] + "\n"

print("Your options have been copied to your clipboard")
pc.copy(out)

input("\nPress enter to exit:\n")
