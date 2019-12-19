from SmartDHT22 import SmartDHT22
from SmartMCP3008 import SmartMCP3008
from SmartSound import SmartSound

import time
import numpy as np
import requests
import time


def main():
    iteratrions = 60
    interval = 1

    dht_sensor = SmartDHT22(pin_num=4)
    mcp_reader = SmartMCP3008()
    sound_sensor = SmartSound(GPIO_pin=5, MCP_ENV_PIN=4, MCP_AUD_PIN=3)

    temperature = []
    humidity = []
    photo = []
    
    #Sound
    gate = []
    envelope = []
    audio = []

    
    for i in range(iteratrions):
        timestamp = str(time.time())
        date_out = time.strftime("%m_%d_%Y")
        temperature.append(dht_sensor.get_temp_celsius())
        humidity.append(dht_sensor.get_humidity())
        photo.append(mcp_reader.read(pin_num=2))
        gate.append(sound_sensor.get_gate())
        envelope.append(sound_sensor.get_envelope())
        audio.append(sound_sensor.get_audio())

        temp_out = str(temperature[-1])
        hum_out = str(humidity[-1])
        light_out = str(photo[-1])
        gate_out = str(gate[-1])
        env_out = str(envelope[-1])
        audio_out = str(audio[-1])
        device_id = "0001"

        #data = 'device_id': '0001', 'date':date_out , 'time':timestamp, 'temperature':temp_out, 'humidity':hum_out, 'light':light_out, 'audio':audio_out, 'gate':gate_out, 'envolope':env_out}
        data = 'device_id='+device_id+'&date='+date_out+'&time='+timestamp+'&temperature='+temp_out+'&humidity='+hum_out+'&light='+light_out+'&audio='+audio_out+'&gate='+gate_out+'&envolope='+env_out
        print( data )
        v_headers = {'content-type':'application/x-www-form-urlencoded'}
        url = "http://127.0.0.1:5000/store_temp_light_sound_sensor_data"

        r = requests.post(url, data, headers=v_headers)
        print(r.status_code, r.reason)

        print(timestamp, temperature[-1], humidity[-1], photo[-1], gate[-1], envelope[-1], audio[-1])
        time.sleep(interval)
        


    
if __name__ == '__main__':
    main()
