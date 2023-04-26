import os
import json
import sys
import uuid
import time
import logging
from multiprocessing import Process
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session

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
        f = open(config_path, )
        config_dict = json.load(f)

        print('########## config_dict: ', config_dict)
        # config_dict = pickle.load(f)
        for key, value in config_dict.items():
            setattr(self, key, value)

        self.artifactPath = artifact_path
        self.uid = str(uuid.uuid4())

        print("########### NAME", self.name)

    def mainLoop(self, session, row):

        try:
            print('Starting Deployment Process')
            global retry_count
            retry_count += 1

            final_dir = deployer_object.createDirectoryStructure(self.name, self.version, session, row)
            # deployer_object. createRunTimeEnv(self.Runtime_Environment, final_dir)
            deployer_object.transferArtifacts(self.artifactPath, self.dependencies, final_dir, session, row)

            # resources_avialble_in_kb = deployer_object.checkResourceAvailability()
            # if resources_avialble_in_kb > self.RequiredResouces:
            #     deployer_object.runCommands(final_dir, self.Run_Commands)

            deployer_object.pushPubSubToDataXhange(self.uid, self.resources['subscribeTo'], self.resources['publishTo'],
                                                   session, row)
            time.sleep(3)

            deployer_object.runCommands(self.uid, final_dir, self.commands)

        except Exception as e:
            current_user_home = current_user_home = os.path.expanduser('~')
            logging.exception(e)
            print(e)
            # cmd = "rm -rf " + current_user_home

            # os.system(cmd)
            while (retry_count <= 2):
                self.mainLoop()


def setupdDbAndProcessEntries():
    host = 'localhost'
    port = 5432
    dbname = os.environ.get('DBNAME')
    username = os.environ.get('DBUSERNAME')
    password = os.environ.get('PASSWORD')


    db_url = 'psotgresql' + '://' + password + ':' + username + '@' + host + ':' + port + '/' + dbname

    engine = create_engine(db_url)
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    ApplicationsDB = Base.classes.applications


    session = Session(engine)

    config_file = "app.config"

    while True:
        try:
            results = session.query(ApplicationsDB).where(ApplicationsDB.isProcessed == False)

            for row in results:
                config_path = row.extractedPath + "/" + config_file

                artifact_path = row.extractedPath + "/"
                deployer_main_object = deployer_main(config_path, artifact_path, row, session)

                deployer_main_object.mainLoop(row, session)
        except Exception as e:
            logging.exception(e)

        time.sleep(2)


if __name__ == "__main__":
    workspace = os.getenv("WORKSPACE_DIR", "faas_on_iot_workspace");
    os.chdir(workspace)

    print('###########################')
    print('## Initiating Deployment ##')
    print('###########################')

    # config_path = "/Users/shreyasvaidya/Desktop/ADS/FaaSOnIoT-master/core/deployment_engine/user_config.json"
    # artifact_path = "/Users/shreyasvaidya/Desktop/ADS/FaaSOnIoT-master/core/deployment_engine/demo_code.py"

    setupdDbAndProcessEntries()
