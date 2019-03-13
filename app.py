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
    test = [(i,c.delegates[i]) for i in c.delegates]
    print(test)
