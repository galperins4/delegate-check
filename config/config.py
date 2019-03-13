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
        self.ark_net = os.getenv("ARK_NET").split(',')
        self.dark_net = os.getenv("DARK_NET").split(',')
        self.qredit_net = os.getenv("QREDIT_NET").split(',')
        self.phantom_net = os.getenv("PHANTOM_NET").split(',')
        self.persona_net = os.getenv("PERSONA_NET").split(',')
        self.ripa_net = os.getenv("RIPA_NET").split(',')
        self.swapblocks_net = os.getenv("SWAPBLOCKS_NET").split(',')
        self.blockpool_net = os.getenv("BLOCKPOOL_NET").split(',')
    
    
    def load_epoch(self):
        self.persona_epoch = os.getenv("PERSONA_EPOCH").split(',')
        self.ripa_epoch = os.getenv("RIPA_EPOCH").split(',')
        self.swapblocks_epoch = os.getenv("SWAPBLOCKS_EPOCH").split(',')
        self.blockpool_epoch = os.getenv("BLOCKPOOL_EPOCH").split(',')
