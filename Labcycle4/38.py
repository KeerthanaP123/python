f=open("abc.txt","r")
f1=open("pqr.txt","w")
content=f.readlines()
type(content)
for i in range(0,len(content)):
    if i%2!=0:
        f1.write(content[i])
    else:
        pass
f1.close()
f1=open("pqr.txt","r")
content1=f1.read()
print(content1)
f.close()
f1.close()
