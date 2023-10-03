import pyperclip

# get text from clipboard and copy to GPA
text = pyperclip.paste()
print(text)

# split text into lines
lines = text.split("\n")

earned = 0
total = 0
for line in lines:
    print(line)
    if "-" in line:
        continue

    if "/" in line:
        if "\t" not in line:
            earned += float(line.split("/")[0].strip())
            total += float(line.split("/")[1].strip())
        else:
            earned += float(line.split("/")[0].strip())
            total += float(line.split("/")[1].split("\t")[0].strip())

print("GPA: " + str(earned / total))
print("Earned: " + str(earned) + "point out of " + str(total) + "points.")
