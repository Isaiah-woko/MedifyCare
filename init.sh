pip install virtualenv
if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    virtualenv venv
fi
source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=app.py
if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    export FLASK_APP=app.py; flask db init
fi
echo --------------------
echo Generate migration DDL code
echo --------------------
flask db migrate
echo --------------------
echo Run the DDL code and migrate
echo --------------------
echo --------------------
echo This is the DDL code that will be run
echo --------------------
flask db upgrade
source venv/bin/activate;
echo --------------------
echo Generate the Test data
echo --------------------
python3 -B test_data.py
echo --------------------
echo Running the app
echo --------------------
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
