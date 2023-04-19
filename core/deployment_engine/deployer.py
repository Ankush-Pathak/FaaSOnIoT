import os
import pickle
import getpass
import json
import shutil
from collections import namedtuple

class deployer:
    # def __init__(self, config_path, artifcat_path) -> None:
    #     config_dict = json.load(config_path)
    #     #config_dict = pickle.load(f)
    #     for key in config_dict.keys():
    #         self.key = config_dict[key]
    #     self.artifactPath = artifcat_path

        

    def createRunTimeEnv(self, envName, final_dir):
        print('Executing createRunTimeEnv()')
        os.chdir(final_dir)
        if envName == 'venv':
            cmd = "sudo apt-get install python3.8"
            os.system(cmd)
        if envName == 'default':
            pass

    def createDirectoryStructure(self) -> str:
        print('Executing createDirectoryStructure()')
        current_user_home = os.path.expanduser('~')
        app_name = self.Name
        app_version = self.Version

        default_directory_struct = 'com/app'
        final_directory_structure = default_directory_struct + '/'+app_name + '/' + app_version + '/'
        os.makedirs(final_directory_structure)
        return final_directory_structure

    ## remember final_directory_path and deployment directory path are same and needs to be passed from the main function

    def transferArtifacts(self, deployment_dir_path):
        print('Executing transferArtifacts()')
        cmd_to_copy = "cp -r " + self.artifactPath + " " + deployment_dir_path 
        os.system(cmd_to_copy)

    def runCommands(self, deployment_dir_path):
        print('Executing runCommands()')
        os.chdir(deployment_dir_path)
        for command in self.Run_Commands.Exec_Commands:
            os.system(command)

    def checkResourceAvailability() -> int:
        print('Executing checkResourceAvailability()')
        MemInfoEntry = namedtuple('MemInfoEntry', ['value', 'unit'])
        meminfo = {}
        with open('/proc/meminfo') as file:
            for line in file:
                key, value, *unit = line.strip().split()
                meminfo[key.rstrip(':')] = MemInfoEntry(value, unit)
        return meminfo['MemAvailable'].value




    def fallBack():
        pass


    def pushPubSubToDataXhange():
        pub_topic = self.Resources.Pubs_Topic
        subs_topic = self.Resources.Subs_Topic

        ## add code to send to dataXchange



    ###  write a function to check continuously if an error has occurent during runtime or deployment 