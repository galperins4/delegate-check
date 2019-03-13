import asyncio
import aiohttp
import aioboto3
from datetime import datetime
from datetime import timedelta
from shutil import copy2


class Util:
    def __init__(self):
        pass
        

    async def notifications(msg):
        async with aioboto3.client("sns",
            aws_access_key_id=aws_key_id,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region) as client:
            await client.publish(
                PhoneNumber=phone,
                Message=msg)

    async def api_get(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()
            
            
    async def retrieve(network,delegate,version):
        result = await api_get(nodes[network] + '/delegates/' + delegate)
        rank = str(result['data']['rank'])
        if result['data']['rank'] <= db[network][0]:
            active = 'yes'
        else:
            active = 'no'
        rank = rank + '/' + str(db[network][0])
        timestamp = result['data']['blocks']['last']['timestamp']['unix']
        utc_remote = datetime.utcfromtimestamp(timestamp)
        utc_local = datetime.utcnow().replace(microsecond=0)
        delta = int((utc_local - utc_remote).total_seconds())
        lb = str(int(round(delta/60)))
        tworounds = 2 * db[network][0] * db[network][1]
        if delta > tworounds:
            miss = 'yes'  
            if sns_enabled == 'yes' and delta < 2 * tworounds:
                await notifications(network + ' delegate missed a block!')
                print('Sent SMS!')
        else:
            miss = 'no'
        
        print('Network: ' + network + ' | Delegate: ' + delegate + ' | Rank: ' + rank + ' | Active: ' + active + ' | Last Block: ' + lb + ' min ago | Missed Block: ' + miss)
