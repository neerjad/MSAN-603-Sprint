import json
import sys
import os

prefix = sys.argv[1]
# prefix = 'group'
import os

path = '/srv/runme/'
# path = '/Users/neerjadoshi/msan/BusinessStrategies/MSAN-603-Sprint/jsonfiles'
name = []
age = []
output_file = str(prefix + '.txt')
if os.path.isfile(os.path.join(path, output_file)):
    os.remove(os.path.join(path, output_file))
files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i)) and prefix in i]
data = []

for file in files:
    with open(os.path.join(path, file)) as f:
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

# for i in range(0, len(name)):
#     print str(name[i]) + '\t' + str(age[i])
with open(path +'/'+ output_file, 'w') as f:
    for i in range(len(name)):
        f.write(str(name[i]) + '\t' + str(age[i]) + '\n')
