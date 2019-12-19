
import os
from flask import Flask, render_template, g, request, redirect
from sqlite3 import dbapi2 as sqlite3
import sys

import time
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))

##### APP SETUP #####
app = Flask(__name__)

##### DB SETUP #####
import SensortoSequel
sensor_DB_wrapper = SensortoSequel.SensortoSequel()

##### ROUTES #####
@app.route('/home', methods=['GET'])
def home():
    sensor_options_array = sensor_DB_wrapper.get_device_dates()
    return render_template('home.html', options=sensor_options_array)

@app.route('/temperature_sensor', methods=['GET'])
def temperature_sensor():
    data = sensor_DB_wrapper.get_temp()
    return render_template('temperature.html', entries=data)

@app.route('/light_sensor', methods=['GET'])
def light_sensor():
    data = sensor_DB_wrapper.get_light()
    return render_template('light.html', entries=data)

@app.route('/sound_sensor', methods=['GET'])
def sound_sensor():
    data = sensor_DB_wrapper.get_sound()
    return render_template('sound.html', entries=data)



@app.route('/get_temp', methods=['POST'])
def get_temperature_data():
    date_device_key = request.form['date_device_key']
    data = sensor_DB_wrapper.get_temp(date_device_key)
    return render_template('temp_ajax.html', entries=data)


@app.route('/get_light', methods=['POST'])
def get_light_data():
    date_device_key = request.form['date_device_key']
    data = sensor_DB_wrapper.get_light(date_device_key)
    return render_template('light_ajax.html', entries=data)

@app.route('/get_sound', methods=['POST'])
def get_sound_data():
    date_device_key = request.form['date_device_key']
    data = sensor_DB_wrapper.get_sound(date_device_key)
    return render_template('sound_ajax.html', entries=data)



@app.route('/test_temp')
def test_temperature_data():
    date_device_key = "03_10_2018__DeviceID__abc"
    data = sensor_DB_wrapper.get_sound(date_device_key)
    return render_template('test.html')



@app.route('/store_temp_light_sound_sensor_data', methods=['POST'])
def store_sensor_data():
    device_id = request.form['device_id']
    date = request.form['date']
    timestamp = request.form['time']
    temp = request.form['temperature']
    hum = request.form['humidity']
    light = request.form['light']
    audio_in = request.form['audio']
    gate_in = request.form['gate']
    env_in = request.form['envolope']

    #Store data in sqlite
    sensor_DB_wrapper.POST_Temp_Light_And_Sound_For_Device_with_Date(device_id, date, timestamp, temp, hum, light, gate_in, env_in, audio_in )
    return "200"

@app.route('/test_store_sensor_data')
def test_store_sensor_data():
    device_id = "abc"
    date = time.strftime("%m_%d_%Y")
    timestamp = "0"
    temp = "10"
    hum = ".2"
    light = "20"
    audio_in = "12"
    gate_in = "34"
    env_in = "8"

    #Store data in sqlite
    sensor_DB_wrapper.POST_Temp_Light_And_Sound_For_Device_with_Date(device_id, date, timestamp, temp, hum, light, gate_in, env_in, audio_in )

    #sensor_options_array = sensor_DB_wrapper.get_device_dates()
    return render_template('test.html')


@app.route('/store_temperature_sensor_data', methods=['POST'])
def store_temperature_sensor_data():
    date = request.form['date']
    timestamp = request.form['time']
    temp = request.form['temperature']

@app.route('/store_light_sensor_data', methods=['POST'])
def store_light_sensor_data():
    date = request.form['date']
    timestamp = request.form['time']
    light = request.form['light']


@app.route('/store_sound_sensor_data', methods=['POST'])
def store_sound_sensor_data():
    date = request.form['date']
    timestamp = request.form['time']
    audio = request.form['audio']
    gate = request.form['gate']
    envolope = request.form['envolope']

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
