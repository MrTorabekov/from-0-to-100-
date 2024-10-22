# file = open('matn.txt',"w")
# file.write("My hobby is write coding")
# file.close()

# file = open('matn.txt','w')
# file.write("My hobby is write coding\n")
# file.write("My hobby is reading docs about python")

# matn = open('matn.txt','r')
# text = matn.read()
# print(text)

texts = open('matn.txt','r')
# print(texts.readline())

for i in texts:
    print(i)