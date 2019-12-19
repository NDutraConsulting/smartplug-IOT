import sqlite3
import os
import sys
import json
class SensortoSequel():
  
    def __init__(self):
        # print("INIT DB", file=sys.stderr)
        
        # Setup DB
        db_filename = 'data.db'
        create_tables = not os.path.isfile(db_filename)
        
        self.conn = sqlite3.connect(db_filename, check_same_thread=False)
        self.c = self.conn.cursor()


        self.conn.commit()

    #### Public facing POST method ###
    ##################################################
    """ As a automation farmer
        I want to be able to run my sensors 24 hours 
        a day and store all of the sensor data for that 
        day on a second by second basis.
        So that data can be easily mapped to data 
        collected about the growth patterns of the plants
  
        To reduce table overload and slow query times
        we will create a new table for each device at 
        the begining of each new day.
        
        The following function:
        Creates new tables for the device and date
        Inserts a new device-date key
        Inserts all sensor data into the appropriate table
        tablename = device-"+device_id+"_"+sensor_name+"_"+todays_date
               
    """
    def POST_Temp_Light_And_Sound_For_Device_with_Date(self, device_id, date, time, temp, hum, light, gate_in, env_in, audio_in ):
        ### Create the tables for this specific device on the given date 
        self.create_tables(date, device_id)
        
        self.set_device_date(device_id, date)
        self.set_temp(time, temp, hum, device_id, date)
        self.set_light(time, light, device_id, date)
        self.set_sound(time, gate_in, env_in, audio_in, device_id, date)



    #### Storage management for device sensor data ###
    ##################################################
    """ The device_date table reduces  
        the time to retrieve a query   
        and makes it easier to run the 
        sensors continuously.          
    """
    def create_tables(self, date_in, device_id_in):

        #date_device_key = create_Date_Device_Key(date_in, device_id_in)

        self.c.execute("CREATE TABLE IF NOT EXISTS device_dates (date, device_id, date_device_key UNIQUE)")
        #self.c.execute("DROP TABLE device_dates")

        temp_tablename = self.create_sensor_tablename("temp", device_id_in, date_in)        
        self.c.execute("CREATE TABLE IF NOT EXISTS "+temp_tablename+" (time, temperature, humidity)")

        light_tablename = self.create_sensor_tablename("light", device_id_in, date_in) 
        self.c.execute("CREATE TABLE IF NOT EXISTS "+light_tablename+" (time, level)")

        sound_tablename = self.create_sensor_tablename("sound", device_id_in, date_in) 
        self.c.execute("CREATE TABLE IF NOT EXISTS "+sound_tablename+" (time, gate, envelope, audio)")


    def set_device_date(self, device_id_in, date_in):
        device_id = device_id_in
        date = date_in
        date_device_key = self.create_Date_Device_Key(date, device_id)
        #self.c.execute("INSERT OR IGNORE INTO device_dates VALUES ({}, {}, {})".format(date, device_id, date_device_key))
        self.c.execute("""INSERT OR IGNORE INTO device_dates VALUES (?, ?, ?)""", (date, device_id, date_device_key) )
        self.conn.commit()



    def get_device_dates(self):
        cur = self.c.execute('SELECT date_device_key FROM device_dates ORDER BY date')
        data = cur.fetchall()
        res = []
        for i in range(len(data)):
            item = {'date_device_key':data[i][0]}
            res.append(item)
        return res


    @staticmethod
    def create_Date_Device_Key(date, device_id):
        return date +"__DeviceID__"+ device_id

    def create_sensor_tablename(self, sensor_name, device_id, date):
        return sensor_name+"_"+self.create_Date_Device_Key(date, device_id)

    @staticmethod
    def create_sensor_tablename_from_date_device_key( sensor_name, date_device_key):
        return sensor_name+"_"+date_device_key

    #### End of Storage management for device sensor data ###
    #########################################################



    def set_temp(self, time, temp, hum, device_id, date):
        temp_tablename = self.create_sensor_tablename("temp", device_id, date)
        temperature = temp
        humidity = hum
        insert_sql = "INSERT INTO "+temp_tablename+" VALUES ({}, {}, {})"
        self.c.execute(insert_sql.format(time, temperature, humidity))
        self.conn.commit()
    
    def set_light(self, time, light, device_id, date):
        lightLevel = light
        light_tablename = self.create_sensor_tablename("light", device_id, date) 
        insert_sql = "INSERT INTO "+light_tablename+" VALUES ({}, {})"
        self.c.execute(insert_sql.format(time, lightLevel))
        self.conn.commit()

    def set_sound(self, time, gate_in, env_in, audio_in, device_id, date):
        sound_tablename = self.create_sensor_tablename("sound", device_id, date) 
        gate = gate_in
        envelope = env_in
        audio = audio_in
        insert_sql = "INSERT INTO "+sound_tablename+" VALUES ({}, {}, {}, {})"
        self.c.execute(insert_sql.format(time, gate, envelope, audio))
        self.conn.commit()



    def get_temp(self, date_device_key):
        temp_tablename = self.create_sensor_tablename_from_date_device_key( "temp", date_device_key)       
        select_sql = 'SELECT time, temperature, humidity FROM '+ temp_tablename
        cur = self.c.execute(select_sql)
        data = cur.fetchall()
        res = []
        for i in range(len(data)):
            item = {'time':data[i][0], 'temperature':data[i][1],'humidity':data[i][2]}
            res.append(item)
        return res

    def get_light(self, date_device_key):
        light_tablename = self.create_sensor_tablename_from_date_device_key( "light", date_device_key)
        select_sql = 'SELECT time, level FROM '+light_tablename
        cur = self.c.execute(select_sql)
        data = cur.fetchall()
        res = []
        for i in range(len(data)):
            item = {'time':data[i][0], 'level':data[i][1]}
            res.append(item)
        return res

    def get_sound(self, date_device_key):
        sound_tablename = self.create_sensor_tablename_from_date_device_key( "sound", date_device_key)
        select_sql = 'SELECT gate, envelope, audio, time FROM '+sound_tablename
        
        cur = self.c.execute(select_sql)
        data = cur.fetchall()
        res = []
        for i in range(len(data)):
            item = {'time':data[i][3], 'gate':data[i][0], 'envelope':data[i][1], 'audio':data[i][2]}
            res.append(item)
        return res




