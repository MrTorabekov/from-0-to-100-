import os.path


files = ['main.py', 'main.jar', 'setup.py', 'main.go', 'index.js', 'index.html', 'main.css', 'style.css', 'main.cpp',
         'server.go', 'source.cpp']

file = "/Users/diyor/PycharmProjects/august 1/os module/data"

py = 0
jar = 0
go = 0
js = 0
cpp = 0
css = 0
html = 0

# for i in file:
#     s = os.path.split(i)[1]

for i in files:
    if i.endswith(".py"):
        py += 1
    elif i.endswith(".jar"):
        jar += 1
    elif i.endswith(".go"):
        go += 1
    elif i.endswith(".js"):
        js += 1
    elif i.endswith(".html"):
        html += 1
    elif i.endswith("css"):
        css +=1
    elif i.endswith("cpp"):
        cpp += 1

print(f"{py}, {jar}, {go}, {js}, {html}, {css}, {cpp}")


