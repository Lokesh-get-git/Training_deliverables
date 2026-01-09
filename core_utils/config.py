
import json
import os
class Config:
    def __init__(self,path=None):
        self.data={}
        if path:
            self.load(path)

    def load(self,path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"file with the path{path} not found")
        with open(path,"r") as file:
            self.data=json.load(file)
    def get(self,key):
        if key in os.environ:
            print("os")
            return os.environ.get(key)
        print("data")
        return self.data.get(key)