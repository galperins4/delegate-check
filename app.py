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
    print(c.delegates)
    print(c.apis)
    print(c.networks)
    print(c.epochs)
    print(c.sns_enabled)
    print(c.aws_key_id)
    print(c.aws_secret_key)
    print(c.aws_region)
    print(c.phone)
