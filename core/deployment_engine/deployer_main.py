import os
import json
import sys
import uuid
import time
import logging
from multiprocessing import Process
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import  Session



from deployer import deployer
deployer_object = deployer()

from database_manager import database_manager
db_object = database_manager()

retry_count = 0

config_path = str(sys.argv[1])
artifact_path = str(sys.argv[2])



class deployer_main:

    def __init__(self, config_path, artifact_path) -> None:

        print(config_path)
        f = open(config_path,)
        config_dict = json.load(f)
        
        print('########## config_dict: ', config_dict)
        #config_dict = pickle.load(f)
        for key, value in config_dict.items():
            setattr(self, key, value)

        self.artifactPath = artifact_path
        self.uid = str(uuid.uuid4())

        print("########### NAME", self.Name)


    def mainLoop(self,session, row):

        try:
            print('Starting Deployment Process')
            global retry_count
            retry_count += 1
            
            final_dir = deployer_object.createDirectoryStructure(self.Name, self.Version, session, row)
            #deployer_object. createRunTimeEnv(self.Runtime_Environment, final_dir)
            deployer_object.transferArtifacts(self.artifactPath, self.Dependencies, final_dir, session, row)
            
            # resources_avialble_in_kb = deployer_object.checkResourceAvailability()
            # if resources_avialble_in_kb > self.RequiredResouces:
            #     deployer_object.runCommands(final_dir, self.Run_Commands)

            deployer_object.pushPubSubToDataXhange(self.uid, self.Resources['Subs_Topic'], self.Resources['Pubs_Topic'],session, row)
            time.sleep(3)

            p = Process(target=deployer_object.runCommands, args=(self.uid, final_dir, self.Run_Commands))
            p.start()
            p.join()
            
            #deployer_object.runCommands(self.uid, final_dir, self.Run_Commands)
            
        except Exception as e:
            current_user_home = current_user_home = os.path.expanduser('~')
            logging.exception(e)
            print(e)
            #cmd = "rm -rf " + current_user_home

            #os.system(cmd)
            while(retry_count <= 2):
                self.mainLoop()


def setupdDbAndProcessEntries():
    host = 'localhost'
    port = 5432
    dbname = os.environ.get('DBNAME')
    username = os.environ.get('DBUSERNAME')
    password = os.environ.get('PASSWORD')

    db_url = 'postgresql://postgres:postgres@10.21.233.168:5432/dbwebapi'


    db_url = 'psotgresql' + '://' + password  + ':' + username + '@' + host + ':' + port + '/' + dbname

    engine = create_engine(db_url)
    Base = automap_base()
    Base.prepare(engine, reflect = True)

    ApplicationsDb = Base.classes.applications

    session = Session(engine)


    session = Session(engine)

    app_name = "app.json"

    while True:
        try:
            results = session.query(ApplicationsDb).where(ApplicationsDb.c.isProcessed == False)

            for row in results:
                config_path = row.extractedPath + "/" + app_name

                artifact_path = row.extractedPath + "/"
                deployer_main_object = deployer_main(config_path, artifact_path,row, session)
                
        except Exception:
            deployer_main_object.mainLoop(row, session)
            pass

        time.sleep(2)

if __name__== "__main__":

    workspace = os.getenv("WORKSPACE_DIR", "faas_on_iot_workspace");
    os.chdir(workspace)

    print('###########################')
    print('## Initiating Deployment ##')
    print('###########################')

    #config_path = "/Users/shreyasvaidya/Desktop/ADS/FaaSOnIoT-master/core/deployment_engine/user_config.json"
    #artifact_path = "/Users/shreyasvaidya/Desktop/ADS/FaaSOnIoT-master/core/deployment_engine/demo_code.py"

    setupdDbAndProcessEntries()









    


