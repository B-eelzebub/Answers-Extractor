import csv
# basically initialising all the files rn
"""print("Enter the stuff you want: ")
contents = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    contents += line + "\n"
file = open("Test.txt", "w")
file.write(contents)
file.close()"""
file_in = open("Test.txt", "r")
file_out = open("CSV.csv", "w", newline="")
writer = csv.writer(file_out)
lst = []
old = []
final = []
# takes each line and only saves the important stuff leaving the rest
# old and new cause more than one correct option stuff is annoy so you have to edit the past
for line in file_in:
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
file_in.close()
# editing to remove duplicates
edit = []
for row in range(len(final)):
    try:
        if final[row][0] != final[row + 1][0] and final[row] not in edit:
            edit.append(final[row])
            continue
        elif len(final[row + 1][1]) > len(final[row][1]):
            edit.append(final[row+1])
    except:
        pass
if len(old[1]) == 1:
    edit.append(final[row])
writer.writerows(edit)
# printing just answers for easy copy paste
for row in edit:
    print(row[1])
# input("Press enter to quit: ")
