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
        self.apis = self.load_api()
        self.networks = self.load_network()
        self.epochs = self.load_epoch()
        

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
        delegates = self.format_dict(ark,dark,qredit,phantom,persona,ripa,swapblocks, blockpool)
        
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
        api = self.format_dict(ark_api,dark_api,qredit_api,phantom_api,persona_api,ripa_api,swapblocks_api,blockpool_api)
        
        return api

    
    def load_network(self):
        ark_net = self.format_network(os.getenv("ARK_NET").split(',')))
        dark_net = self.format_network(os.getenv("DARK_NET").split(','))
        qredit_net = self.format_network(os.getenv("QREDIT_NET").split(','))
        phantom_net = self.format_network(os.getenv("PHANTOM_NET").split(','))
        persona_net = self.format_network(os.getenv("PERSONA_NET").split(','))
        ripa_net = self.format_network(os.getenv("RIPA_NET").split(','))
        swapblocks_net = self.format_network(os.getenv("SWAPBLOCKS_NET").split(','))
        blockpool_net = self.format_network(os.getenv("BLOCKPOOL_NET").split(','))
        network = self.format_dict(ark_net,dark_net,qredit_net,phantom_net,persona_net,ripa_net,swapblocks_net,blockpool_net)
    
        return network
    
    
    def load_epoch(self):
        persona_epoch = os.getenv("PERSONA_EPOCH").split(',')
        ripa_epoch = os.getenv("RIPA_EPOCH").split(',')
        swapblocks_epoch = os.getenv("SWAPBLOCKS_EPOCH").split(',')
        blockpool_epoch = os.getenv("BLOCKPOOL_EPOCH").split(',')
        epoch = {"persona":persona_epoch,
                 "ripa":ripa_epoch,
                 "swapblocks":swapblocks_epoch,
                 "blockpool":blockpool_epoch}
        
        return epoch
    
    
    def format_dict(self,a,b,c,d,e,f,g,h):
        formatted_dict = {'ark':a,
                          'dark':b, 
                          'qredit':c,
                          'phantom':d,
                          'persona':e,
                          'ripa':f,
                          'swapblocks':g,
                          'blockpool':h}
        
        return formatted_dict

                                     
    def format_network(self, n):
        return [int(n[0]), int(n[1]), n[2]]
                                     
                                     
