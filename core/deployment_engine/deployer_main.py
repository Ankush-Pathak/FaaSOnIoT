import os
import pickle
import getpass
import json
import shutil
from collections import namedtuple

from deployer import deployer

deployer_object = deployer()

retry_count = 0


class deployer_main:
    
    def __init__(self, config_path, artifact_path) -> None:
        print(config_path)
        f = open(config_path,)
        config_dict = json.load(f)
        print('########## config_dict: ', config_dict)
        #config_dict = pickle.load(f)
        for key in config_dict.keys():
            self.key = config_dict[key]
        self.artifactPath = artifact_path

        

    def mainLoop(self):
        try:
            print('Starting Deployment Process')
            retry_count += 1
            final_dir = deployer_object.createDirectoryStructure()
            deployer_object. createRunTimeEnv(self.Runtime_Environment, final_dir)
            deployer_object.transferArtifacts(final_dir)
            resources_avialble_in_kb = deployer_object.checkResourceAvailability()
            if resources_avialble_in_kb > self.RequiredResouces:
                deployer_object.runCommands(final_dir)
            pushPubSubToDataXhange()
        except Exception as e:
            current_user_home = current_user_home = os.path.expanduser('~')
            print(e)
            #cmd = "rm -rf " + current_user_home

            #os.system(cmd)
            while(retry_count <= 2):
                mainLoop()

            

if __name__== "__main__":
    print('START#####################')

    config_path = "/app/user_config.json"
    artifact_path = "/app/demo_code.py"

    deployer_main_object = deployer_main(config_path, artifact_path)
    deployer_main_object.mainLoop()


