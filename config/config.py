import os
from dotenv import load_dotenv
from pathlib import Path

class Config():
    def __init__(self):
        self.home = str(Path.home())
        env_path = self.home + '/delegate-check/config/config'
        load_dotenv(env_path)
        self.load_sns()
        self.load_delegates()
        self.load_api()
        self.load_network()
        self.load_epoch()
        

    def load_sns(self):
        self.sns_enabled = os.getenv("SNS_ENABLED")
        self.aws_key_id = os.getenv("AWS_KEY_ID")
        self.aws_secret_key = os.getenv("AWS_SECRET_KEY")
        self.aws_region = os.getenv("AWS_REGION")
        self.phone = os.getenv("PHONE")
    
    def load_delegates(self):
        pass


    def load_api(self):
        pass

    
    def load_network(self):
        pass
    
    
    def load_epoch(self):
        pass
