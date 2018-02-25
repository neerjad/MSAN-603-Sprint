from flask import Flask
from flask import request
from flask import render_template
from jinja2 import Environment

application = Flask(__name__)

# home route  
@application.route('/')  
def home_page():
    return render_template('layout.html')


@application.route('/json-example', methods=['POST']) 
def json_example():
    req_data = request.get_json()
    # name = req_data['name']
    # age = req_data['age']
    # zipcode = req_data['prop']['zipcode'] 
    # dmid = req_data['prop']['DMID']
    # print '''name: {} age: {} zipcode: {} DMID: {}'''.format(name, age, zipcode, dmid)
    with open("Raw.txt", "a") as f: 
        f.write(str(req_data).replace('\n','')+'\n') # append json to raw file 
    return 'Your JSON file has been uploaded'


if __name__ == '__main__':
    application.run(host = '0.0.0.0', port = 8080, debug = True)