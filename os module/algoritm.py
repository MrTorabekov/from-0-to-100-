import os

'''

create folder data
create files all
files = ['main.py', 'main.jar', 'setup.py', 'main.go', 'index.js', 'index.html', 'main.css', 'style.css', 'main.cpp','server.go','source.cpp']
files = {
    '.py' : 4,
    '.cpp' : 2,
    '.css' : 3,
}
'''
files = ['main.py', 'main.jar', 'setup.py', 'main.go', 'index.js', 'index.html', 'main.css', 'style.css', 'main.cpp',
         'server.go', 'source.cpp']

# os.mkdir('data')

# for x in files:
#     with open(f'data/{x}', 'w') as file:
#         ...

# print(os.getcwd())

data = {

}
file = os.listdir('/Users/macbookair/dev/pdp/10a/data')
for x in file:
    s = os.path.splitext(x)[1]
    if s in data:
        data[s] += 1
    else:
        data[s] = 1

print(data)
