from filelock import FileLock, Timeout


class permission_manager():

    def __init__(self, app_name):

        self.app_name = app_name
        self.file_name = "pubsub_details_" + app_name + ".txt"

    def app_pubsub(sub_list, pub_list):

        file = self.file_name

        lockfile = self.file_name + ".lock"
        lock = FileLock(lockfile)

        lock.acquire()
        try:
            with open(file, "a") as f:

                ## printing app_id
                line=self.app_name+";"
                f.write(line)

                ## print all elements in the sub_list
                f.write("[")
                j=0
                for i in sub_list:
                    if j < len(sub_list)-1:
                        f.write(i) 
                        f.write(",")
                        j+=1
                    else:
                        f.write(i)
                    
                
                f.write("]")
                f.write(";")

                ## printing all elements in the pub_list 
                f.write("[")
                j=0
                for i in pub_list:
                    if j < len(pub_list)-1:
                        f.write(i) 
                        f.write(",")
                        j+=1
                    else:
                        f.write(i)

                f.write("]")

                f.write("\n")

        finally:
            lock.release()


