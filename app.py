import os
from webapp import create_app, socketio

env = 'prod' #os.environ.get('WEBAPP_ENV', 'dev') ## if is not in environment just return dev
app = create_app('config.%sConfig' % env.capitalize())
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if __name__ == '__main__':
    app.run(debug=True)