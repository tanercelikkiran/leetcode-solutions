import os

folder_path = "solutions"

file_count = 0

file_count += len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])

#Read the README.md file and change the number of problems solved by finding the line with the number of problems solved

with open("README.md", "r") as f:
    f.seek(0)
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "solved" in line:
            lines[i] = "I solved **" + str(file_count) + "** problems so far.\n"
            break

#Write the new README.md file

with open("README.md", "w") as f:
    f.writelines(lines)

