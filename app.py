from flask import Flask, request, jsonify
import config
import malwaredetect
import json
import os
import logging



app = Flask(__name__)

#### recording app log ###################################################################

logger = logging.getLogger(__name__)
LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()
logging.basicConfig(level=LOGLEVEL)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('./malwarelog.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('app started to run')
    


########################## Main Page #########################################################
@app.route('/')
def index():
    try:
        logger.info("home page loaded successfully")
        return "<h1>Webpage</h1>"
    except Exception as e:        
        print("unable to load home page: ",e)
        return "unable to load home page"

########################## To insert URL into database from json request######################
@app.route('/insertdata/',methods=["POST"])
def insertdata():
    try:        
        data = request.json
        obj = malwaredetect.malwaredetect()
        response = obj.table_values(data)
        logger.info("Use POST method to insert the data")       
        return response
    except Exception as e:
        logger.error("Error while processing json request:{}".format(e)) 
        print(" Error while processing json request: ",e)
        return "Error while processing json request"

######################### Get all values from a database #####################################
@app.route('/getalldata/',methods=["GET"])
def getalldata():
    try:
        logger.info("Use GET method to view the data from the database")
        obj = malwaredetect.malwaredetect()
        response = obj.getallvalues()
        return response
    except Exception as e:
        logger.error("Error while processing json request : {}".format(e))
        print("Error while processing json request: ",e)
        return "Error while processing json request"

######################### To check whether a url is available in database ###################
@app.route('/malwarecheck/',methods=["POST"])
def malwarecheck():
    try:
        logger.info("Use POST method to check status of the URL")
        data = request.json
        obj = malwaredetect.malwaredetect()
        response = obj.detection(data)
        return response
    except Exception as e:
        logger.exception("Error while processing json request: {}".format(e))
        print(" Error while processing json request: ",e)
        return "Error while processing json request"
        

######################### To insert the URL from a text file into database ###############
@app.route('/getfile/',methods=["POST"])
def getfile():
    try:
        logger.info("use POST method to load bulk data to the database")
        file = request.files['file']
        fileContent = file.read().decode("utf-8")
        replaceWhitespace=fileContent.replace("\n", ",").strip()
        splitter = replaceWhitespace.split(",")
        for i in splitter:
            if i.strip() != "":
                userrequest = {'url':i.strip()}
                obj=malwaredetect.malwaredetect()
                response=obj.table_values(userrequest)
        return response
    except Exception as e:
        logger.exception("Error while processing json request : {}".format(e))
        print("Error while processing input file: ",e)
        return "Error while processing input file"

################################ To clear values from a database ##########################
@app.route('/deleteall/',methods=["DELETE"])
def deleteall():
    try:
        logger.info("use DELETE method to delete the values in the database")
        obj= malwaredetect.malwaredetect()
        response = obj.deleteall()
        return response
    except Exception as e:
        logger.error("Error while processing json request: {}".format(e))
        print("Error while processing json request: ",e)
        return "Error while processing json request"
        
if __name__ == '__main__':
    obj= malwaredetect.malwaredetect()
    response = obj.table_creation()
    app.run(debug=True,host='0.0.0.0')    
    
        
