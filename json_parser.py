import json
import sys
import os

#set up paths and lists
prefix = sys.argv[1]
path = '/srv/runme/'
name = []
age = []
output_file = str(prefix + '.txt')

#handle file/path
if os.path.isfile(os.path.join(path, output_file)):
    os.remove(os.path.join(path, output_file))

files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i)) and prefix in i]
data = []

#don't fall down the stairs...
for fyle in files:
    with open(os.path.join(path, fyle)) as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('name') == None or data.get('name') == '':
                    continue
                if type(data['prop'].get('age')) == int and data['prop'].get('age') >= 0:
                    name.append(data['name'])
                    age.append(data['prop']['age'])
            except:
                continue

with open(path +'/'+ output_file, 'w') as f:
    for i in range(len(name)):
        f.write(str(name[i]) + '\t' + str(age[i]) + '\n')