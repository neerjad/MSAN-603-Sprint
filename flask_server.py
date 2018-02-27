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
  

# TODO: make this run on AWS properly with a testtest user 
# adding what could be useful for running on AWS in comments  

prefix = sys.argv[1]
home_path = "/srv/runme/" + prefix 
raw_path = home_path + "/Raw.txt"
proc_path = home_path + "/proc.txt"

raw_logger = logging.getLogger("raw rotation")
raw_logger.setLevel(logging.INFO)
raw_logger.addHandler( TimedRotatingFileHandler( raw_path , when = 'm', interval = 2, backupCount = 5) )

proc_logger = logging.getLogger("proc rotation")
proc_logger.setLevel(logging.INFO)
proc_logger.addHandler( TimedRotatingFileHandler( proc_path , when = 'm', interval = 2, backupCount = 5) )



#start of application        
@application.route("/", methods=['POST', 'GET']) 
def json_example():

    req_data = request.json

    try:
        with open(raw_path, "a+"): 
            raw_logger.info(str(req_data).replace('\n','')+'\n') # append json to Raw.txt file  
    except:
        return "Malformed JSON"

    try:     
        data = req_data
        name = data["name"]
        age = data["prop"]["age"]

        assert(type(age) == int)
        assert(age > 0)
        assert(type(name) == str)
   
        with open(proc_path, 'a+'):
            proc_logger.info( name + "\t" + str(age))

    except ValueError as value_error:
        return "Incorrect values"
    except LookupError as lookup_error:
        return "LookUpError encountered"
    except KeyError as key_error:
        return "Your JSON blob does not have the correct key:value pairs"
    else:
        return "There was an error with your POST"

    return "Your JSON file has been uploaded"
   
if __name__ == "__main__":
    application.run(host = '0.0.0.0', port = 8080, debug = True)

        
