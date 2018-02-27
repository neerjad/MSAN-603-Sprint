from flask import Flask
from flask import request
from flask import render_template
from jinja2 import Environment
import json  
import os 
import sys  
import logging
from logging.handlers import TimedRotatingFileHandler

application = Flask(__name__)
  
try:
    #set up correct path for files
    prefix = sys.argv[1]
    home_path = "/srv/runme/" + prefix 
    raw_path = home_path + "/Raw.txt"
    proc_path = home_path + "/proc.txt"

    #set up logging for Raw.txt
    raw_logger = logging.getLogger("raw rotation")
    raw_logger.setLevel(logging.INFO)
    raw_logger.addHandler( TimedRotatingFileHandler( raw_path , when = 'm', interval = 2, backupCount = 5) )

    #set up logging for proc.txt
    proc_logger = logging.getLogger("proc rotation")
    proc_logger.setLevel(logging.INFO)
    proc_logger.addHandler( TimedRotatingFileHandler( proc_path , when = 'm', interval = 2, backupCount = 5) )

except OSError:
    'Path not correctly configured!'
else:
    'Error encountered!'

#start of application        
@application.route("/", methods=['POST', 'GET']) 
def json_example():
    try:
        #get json and append to Raw.txt
        req_data = request.json
        with open(raw_path, "a+"): 
            raw_logger.info(str(req_data).replace('\n','')+'\n')
    except:
        return "Malformed JSON"

    try:
        #extract name and age from data     
        data = req_data
        name = data["name"]
        age = data["prop"]["age"]

        #type checking
        assert(type(age) == int)
        assert(age > 0)
        assert( (type(name) == str) | (type(name) == unicode))
   
        with open(proc_path, 'a+'):
            proc_logger.info( name + "\t" + str(age))

    except AssertionError as assertion_error:
        return "Incorrect data types in JSON!"        
    except ValueError as value_error:
        return "Incorrect values!"
    except KeyError as key_error:
        return "Incorrect key:value pairs!"
    except:
        return "There was an error with the POST!"

    return "Your JSON file has been uploaded"
   
if __name__ == "__main__":
    application.run(host = '0.0.0.0', port = 8080, debug = True)