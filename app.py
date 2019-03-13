#from chalice import Chalice
#from util.async import Async
from config.config import Config


#app = Chalice(app_name='delcheck')

'''
@app.route('/')
def index():
    delegate_check()
    return {'status': 'success'}

'''
def delegate_check():
    pass


if __name__ == '__main__':
    c = Config()
    tasks = []
    
    for i in c.delegates:
        # only 1 delegate to process
        if len(c.delegates[i]) == 1 and c.delegates[i][0] != 'delegatename':
            print(i,c.delegates[i][0], c.networks[i][2])
            #tasks.append(asyncio.ensure_future(retrieve(i,c.delegates[i][0], c.networks[i][2]))
    
        # multiple delegates to process
        else:
            for j in c.delegates[i]:
                print(i,j, c.networks[i][2])
