import asyncio
import aiohttp
import aioboto3
from datetime import datetime
from datetime import timedelta
from shutil import copy2


class Util:
    def __init__(self, config):
        self.config = config
        

    async def notifications(self,msg):
        async with aioboto3.client("sns",
            aws_access_key_id=aws_key_id,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region) as client:
            await client.publish(
                PhoneNumber=phone,
                Message=msg)

    async def api_get(self,url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()
            
            
    async def retrieve(self,network,delegate,version):
        if version == 'v2':
            result = await self.api_get(self.config.apis[network] + '/delegates/' + delegate)
            rank = str(result['data']['rank'])
            if result['data']['rank'] <= self.config.networks[network][0]:
                active = 'yes'
            else:
                active = 'no'
            rank = rank + '/' + str(self.config.networks[network][0])
            timestamp = result['data']['blocks']['last']['timestamp']['unix']
            utc_remote = datetime.utcfromtimestamp(timestamp)
        else:
            result = await self.api_get(self.config.apis[network] + '/delegates/get?username=' + delegate)
            rank = str(result['delegate']['rate'])
            if result['delegate']['rate'] <= self.config.networks[network][0]:
                active = 'yes'
            else:
                active = 'no'
            rank = rank + '/' + str(self.config.networks[network][0])
            pubkey = str(result['delegate']['publicKey'])
            result = await self.api_get(self.config.apis[network] + '/blocks?generatorPublicKey=' + pubkey + '&limit=1')
            timestamp = result['blocks'][0]['timestamp']
            utc_remote = datetime(self.config.epochs[network][0], self.config.epochs[network][1], self.config.epochs[network][2], 
                                      self.config.epochs[network][3], self.config.epochs[network][4], 
                                      self.config.epochs[network][5]) + timedelta(seconds=timestamp)

        
        utc_local = datetime.utcnow().replace(microsecond=0)
        delta = int((utc_local - utc_remote).total_seconds())
        lb = str(int(round(delta/60)))
        tworounds = 2 * self.config.networks[network][0] * self.config.networks[network][1]
        if delta > tworounds:
            miss = 'yes'  
            if self.config.sns_enabled == 'yes' and delta < 2 * tworounds:
                await self.notifications(network + ' delegate missed a block!')
                print('Sent SMS!')
        else:
            miss = 'no'
        
        print('Network: ' + network + ' | Delegate: ' + delegate + ' | Rank: ' + rank + ' | Active: ' + active + ' | Last Block: ' + lb + ' min ago | Missed Block: ' + miss)
