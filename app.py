from chalice import Chalice

app = Chalice(app_name='delcheck')


@app.route('/')
def index():
    delegate_check()
    return {'status': 'success'}


def delegate_check():
    pass
