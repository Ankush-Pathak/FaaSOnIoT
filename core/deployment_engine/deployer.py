import os
import json
from collections import namedtuple

from permission_manager import permission_manager


class deployer:
    
    def createRunTimeEnv(self, env_name, final_dir):

        print('Executing createRunTimeEnv()')
        os.chdir(final_dir)
        if env_name == 'venv':
            cmd = "sudo apt-get install python3.8"
            os.system(cmd)
        if env_name == 'default':
            pass


    def createDirectoryStructure(self, app_name, app_version) -> str:

        print('Executing createDirectoryStructure()')
        current_user_home = os.path.expanduser('~')
        app_name = app_name
        app_version = app_version

        default_directory_struct = 'com/app'
        final_directory_structure = default_directory_struct + '/'+app_name + '/' + app_version + '/'   
        
        if not os.path.isdir('com'):
            os.makedirs(final_directory_structure)

        return final_directory_structure


    ## remember final_directory_path and deployment directory path are same and needs to be passed from the main function

    def transferArtifacts(self, artifact_path, dependency_path, deployment_dir_path):

        print('Executing transferArtifacts()')
        cmd_to_copy = "cp -r " + artifact_path + " " + deployment_dir_path 
        os.system(cmd_to_copy)

        cmd_to_copy = "cp -r " + dependency_path + " " + deployment_dir_path 
        os.system(cmd_to_copy)


    def runCommands(self, deployment_dir_path, Run_Commands):

        print('Executing runCommands()')
        os.chdir(deployment_dir_path)
        print("############ Run_Commands: ", Run_Commands)
        for command in Run_Commands['Exec_Commands']:
            os.system(command)


    def checkResourceAvailability(self) -> int:

        print('Executing checkResourceAvailability()')
        MemInfoEntry = namedtuple('MemInfoEntry', ['value', 'unit'])
        meminfo = {}
        with open('/proc/meminfo') as file:
            for line in file:
                key, value, *unit = line.strip().split()
                meminfo[key.rstrip(':')] = MemInfoEntry(value, unit)
        return meminfo['MemAvailable'].value


    def pushPubSubToDataXhange(self, app_name, sub_topics, pub_topics):

        permit_object = permission_manager(app_name)
        permit_object.app_pubsub(sub_list, pub_list)




