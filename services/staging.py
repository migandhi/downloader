import os
import uuid

class Staging:

    def __init__(self,prefix):
        self.uniquename = uuid.uuid1()
        self.staging_path = 'data/{}/{}'.format(prefix.replace(' ','_') , self.uniquename  )

    def run(self):
        self.free()
        cmd = "mkdir \"{staging_path}\"".format(staging_path=self.staging_path)
        #print(cmd)
        output = os.popen(cmd).read()
        return self.staging_path

    def free(self):
        cmd = "rmdir /s /q \"{staging_path}\" ".format(staging_path=self.staging_path)
        #print(cmd)
        #output = os.popen(cmd).read()