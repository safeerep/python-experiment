f = open("created_file.py", "w")
f.write("print('hey safee..')")
f.close()

with open("created_file.py", "r") as f:
    content = f.read()
    print(content)