with open("data.txt")as f:
    content=f.readlines()
print(content)
content=[x.strip() for x in content]
print(content)