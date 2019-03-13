#from chalice import Chalice
#from util.async import Async
from config.config import Config
import asyncio
#import aiohttp
#import aioboto3
#from datetime import datetime
#from datetime import timedelta
#from shutil import copy2


#app = Chalice(app_name='delcheck')

'''
@app.route('/')
def index():
    delegate_check()
    return {'status': 'success'}

'''
def delegate_check():
    pass


def get_tasks():
    tasks = []
    for i in c.delegates:
        # only 1 delegate to process
        if len(c.delegates[i]) == 1 and c.delegates[i][0] != 'delegatename':
            #print(i,c.delegates[i][0], c.networks[i][2])
            tasks.append(asyncio.ensure_future(retrieve(i,c.delegates[i][0], c.networks[i][2])))
    
        # multiple delegates to process
        else:
            for j in c.delegates[i]:
                if j != 'delegatename':
                    #print(i,j, c.networks[i][2])
                    tasks.append(asyncio.ensure_future(retrieve(i,j,c.networks[i][2])))
    return tasks

                    
if __name__ == '__main__':
    c = Config()
    tasks = get_tasks()
    
    # Async Loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()
    
    
    
    for i in c.delegates:
        # only 1 delegate to process
        if len(c.delegates[i]) == 1 and c.delegates[i][0] != 'delegatename':
            #print(i,c.delegates[i][0], c.networks[i][2])
            tasks.append(asyncio.ensure_future(retrieve(i,c.delegates[i][0], c.networks[i][2])))
    
        # multiple delegates to process
        else:
            for j in c.delegates[i]:
                if j != 'delegatename':
                    #print(i,j, c.networks[i][2])
                    tasks.append(asyncio.ensure_future(retrieve(i,j,c.networks[i][2])))

