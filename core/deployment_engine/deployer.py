import os
import json
from collections import namedtuple

from permission_manager import permission_manager


class deployer:
    
    def createRunTimeEnv(self, env_name, final_dir, session, row):

        print('Executing createRunTimeEnv()')
        os.chdir(final_dir)
        if env_name == 'venv':
            cmd = "sudo apt-get install python3.8"
            os.system(cmd)
        if env_name == 'default':
            pass
        
        status = "runtime env created"
        row.status = status
        session.commit()

    def createDirectoryStructure(self, app_name, app_version, row, session) -> str:

        print('Executing createDirectoryStructure()')
        current_user_home = os.path.expanduser('~')
        app_name = app_name
        app_version = app_version

        default_directory_struct = 'com/app'
        final_directory_structure = default_directory_struct + '/'+app_name + '/' + app_version + '/'   
        
        if not os.path.isdir('com'):
            os.makedirs(final_directory_structure)

        status = "directory structure created"
        row.status = status
        session.commit()

        return final_directory_structure


    ## remember final_directory_path and deployment directory path are same and needs to be passed from the main function

    def transferArtifacts(self, artifact_path, dependency_path, deployment_dir_path, session, row):

        print('Executing transferArtifacts()')
        cmd_to_copy = "cp -r " + artifact_path + "/* " + deployment_dir_path 
        os.system(cmd_to_copy)

        # cmd_to_copy = "cp -r " + dependency_path + " " + deployment_dir_path 
        # os.system(cmd_to_copy)

        status = "artifcat transffered"
        row.status = status
        session.commit()

    def runCommands(self, app_uid, deployment_dir_path, Run_Commands, session, row):

        print('Executing runCommands()')

        os.chdir(deployment_dir_path)
        print("############ Run_Commands: ", Run_Commands)
        for command in Run_Commands['Exec_Commands']:
            prefix_plus_cmd = "APP_ID="+app_uid+" "+command
            os.system(prefix_plus_cmd)

        status = "commands executed"
        row.status = status
        session.commit()


    def checkResourceAvailability(self, session, row) -> int:

        print('Executing checkResourceAvailability()')
        MemInfoEntry = namedtuple('MemInfoEntry', ['value', 'unit'])
        meminfo = {}
        with open('/proc/meminfo') as file:
            for line in file:
                key, value, *unit = line.strip().split()
                meminfo[key.rstrip(':')] = MemInfoEntry(value, unit)
        return meminfo['MemAvailable'].value



    def pushPubSubToDataXhange(self, app_id, sub_topics, pub_topics, session, row):

        permit_object = permission_manager(app_id)
        permit_object.app_pubsub(sub_topics, pub_topics)

        status = "pushed pub sub info"
        row.status = status
        session.commit()




