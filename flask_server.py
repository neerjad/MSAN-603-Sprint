from flask import Flask
from flask import request
from flask import render_template
from jinja2 import Environment
import json  
import os 

application = Flask(__name__)

# home route  
@application.route('/')  
def home_page():
    return render_template('layout.html')

  
# check a file for valid json
name = []
age = []  

def json_from_file(filename):
    with open(filename, 'r') as f:
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
        return 

       
@application.route('/json-example', methods=['POST']) 
def json_example():
    req_data = request.get_json() 
    with open("Raw.txt", "a") as f: 
        f.write(str(req_data).replace('\n','')+'\n') # append json to Raw.txt file 
    
    valid_json = json_from_file('Raw.txt') # append valid json to proc.txt file
    with open('proc.txt', 'w') as f1:
        for i in range(len(name)):
            f1.write(str(name[i]) + '\t' + str(age[i]) + '\n')

    return 'Your JSON file has been uploaded'
      
 

if __name__ == '__main__':
    application.run(host = '0.0.0.0', port = 8080, debug = True)

