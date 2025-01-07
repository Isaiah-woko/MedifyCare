import os
from webapp import create_app, socketio

env = 'dev' #os.environ.get('WEBAPP_ENV', 'dev') ## if is not in environment just return dev
app = create_app('config.%sConfig' % env.capitalize())

if __name__ == '__main__':
    app.run(debug=True)
