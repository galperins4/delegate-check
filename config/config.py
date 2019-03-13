import os
from dotenv import load_dotenv
from pathlib import Path

class Config():
    def __init__(self):
        self.home = str(Path.home())
        env_path = self.home + '/delegate-check/config/config'
        load_dotenv(env_path)
        self.load_sns()
        self.delegates = self.load_delegates()
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
        ark = os.getenv("ARK").split(',')
        dark = os.getenv("DARK").split(',')
        qredit = os.getenv("QREDIT").split(',')
        phantom = os.getenv("PHANTOM").split(',')
        persona = os.getenv("PERSONA").split(',')
        ripa = os.getenv("RIPA").split(',')
        swapblocks = os.getenv("SWAPBLOCKS").split(',')
        blockpool = os.getenv("BLOCKPOOL").split(',')
        delegates = [ark,dark,qredit,phantom,persona,ripa,swapblocks, blockpool]
        
        return delegates


    def load_api(self):
        ark_api = os.getenv("ARK_API")
        dark_api = os.getenv("DARK_API")
        qredit_api = os.getenv("QREDIT_API")
        phantom_api = os.getenv("PHANTOM_API")
        persona_api = os.getenv("PERSONA_API")
        ripa_api = os.getenv("RIPA_API")
        swapblocks_api = os.getenv("SWAPBLOCKS_API")
        blockpool_api = os.getenv("BLOCKPOOL_API")
        api = [ark_api,dark_api,qredit_api,phantom_api,persona_api,ripa_api,swapblocks_api,blockpool_api]
        
        return api

    
    def load_network(self):
        ark_net = os.getenv("ARK_NET").split(',')
        dark_net = os.getenv("DARK_NET").split(',')
        qredit_net = os.getenv("QREDIT_NET").split(',')
        phantom_net = os.getenv("PHANTOM_NET").split(',')
        persona_net = os.getenv("PERSONA_NET").split(',')
        ripa_net = os.getenv("RIPA_NET").split(',')
        swapblocks_net = os.getenv("SWAPBLOCKS_NET").split(',')
        blockpool_net = os.getenv("BLOCKPOOL_NET").split(',')
        network = [ark_net,dark_net,qredit_net,phantom_net,persona_net,ripa_net,swapblocks_net,blockpool_net]
    
        return network
    
    
    def load_epoch(self):
        persona_epoch = os.getenv("PERSONA_EPOCH").split(',')
        ripa_epoch = os.getenv("RIPA_EPOCH").split(',')
        swapblocks_epoch = os.getenv("SWAPBLOCKS_EPOCH").split(',')
        blockpool_epoch = os.getenv("BLOCKPOOL_EPOCH").split(',')
        epoch = [persona_epoch,ripa_epoch,swapblocks_epoch,blockpool_epoch]
        
        return epoch
