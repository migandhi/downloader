import os
import uuid

class Staging:

    def __init__(self,prefix):
        self.uniquename = uuid.uuid1()
        self.staging_path = 'data/{}/{}'.format(prefix.replace(' ','_') , self.uniquename  )

    def run(self):
        self.free()
        cmd = "mkdir -p {staging_path}".format(staging_path=self.staging_path)
        #output = os.popen(cmd).read()
        os.mkdir(self.staging_path)
        return self.staging_path

    def free(self):
        cmd = "rm -Rf {staging_path} ".format(staging_path=self.staging_path)
        #output = os.popen(cmd).read()
        
        #try:
          #os.rmdir(self.staging_path)
        #except:
          #print("file not found")

        
