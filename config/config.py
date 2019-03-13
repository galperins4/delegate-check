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
        self.ark = os.getenv("ARK").split(',')
        self.dark = os.getenv("DARK").split(',')
        self.qredit = os.getenv("QREDIT").split(',')
        self.phantom = os.getenv("PHANTOM").split(',')
        self.persona = os.getenv("PERSONA").split(',')
        self.ripa = os.getenv("RIPA").split(',')
        self.swapblocks = os.getenv("SWAPBLOCKS").split(',')
        self.blockpool = os.getenv("BLOCKPOOL").split(',')


    def load_api(self):
        self.ark_api = os.getenv("ARK_API")
        self.dark_api = os.getenv("DARK_API")
        self.qredit_api = os.getenv("QREDIT_API")
        self.phantom_api = os.getenv("PHANTOM_API")
        self.persona_api = os.getenv("PERSONA_API")
        self.ripa_api = os.getenv("RIPA_API")
        self.swapblocks_api = os.getenv("SWAPBLOCKS_API")
        self.blockpool_api = os.getenv("BLOCKPOOL_API")

    
    def load_network(self):
        pass
    
    
    def load_epoch(self):
        pass
