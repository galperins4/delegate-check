from chalice import Chalice
from config.config import Config
from util.util import Util
import asyncio


app = Chalice(app_name='delegate-check')


@app.route('/')
def index():
    delegate_check()
    return {'status': 'success'}

def delegate_check():
    c = Config()
    u = Util(c)
    tasks = get_tasks(c)
    
    # Async Loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()


def get_tasks(c):
    tasks_list = []
    for i in c.delegates:
        # only 1 delegate to process
        if len(c.delegates[i]) == 1 and c.delegates[i][0] != 'delegatename':
            #print(i,c.delegates[i][0], c.networks[i][2])
            tasks_list.append(asyncio.ensure_future(u.retrieve(i,c.delegates[i][0], c.networks[i][2])))
    
        # multiple delegates to process
        else:
            for j in c.delegates[i]:
                if j != 'delegatename':
                    #print(i,j, c.networks[i][2])
                    tasks_list.append(asyncio.ensure_future(u.retrieve(i,j,c.networks[i][2])))
    return tasks_list

'''                  
if __name__ == '__main__':
    c = Config()
    u = Util(c)
    tasks = get_tasks()
    
    # Async Loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()
'''
