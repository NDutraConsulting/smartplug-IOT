sudo -H pip install --editable .
export FLASK_APP=SmartPlug
export FLASK_DEBUG=true
flask run --host=0.0.0.0
