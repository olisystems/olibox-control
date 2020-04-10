
import sys
import time

import json
import os

import paho.mqtt.client as mqtt

from .environments import get_locals
from .helpers import write_values


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("connected OK Returned code=", rc)
        client.subscribe("DOSE/OLI_70/PV/setPowerLimit", 0)
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected Returned code=", rc)
    client.connected_flag = False


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    obj = {'setOutputLimit': {payload['timestamp']: payload['SetPowerLimit']}}
    write_values('data.json', obj)
    print(msg)
    #print("Message received-> " + msg.topic + " " + str(msg.payload))


def config_mqtt():
    vars = get_locals()
    oli_box_id = vars['oli_box_id']
    client_name = f'OLI_{oli_box_id}_PUB'
    pwd = vars['mqtt_password']
    usr = vars['mqtt_username']
    mqtt_broker_ip = vars['mqtt_broker_ip']
    mqtt_broker_port = vars['mqtt_broker_port']

    print('Configuring MQTT Client and connecting to Broker...')

    mqtt.Client.connected_flag = False

    client = mqtt.Client(client_name)
    client.username_pw_set(usr, pwd)
    cert = 'ca-certificates.crt'
    client.tls_set(cert)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_log = on_log

    try:
        client.connect(mqtt_broker_ip, int(mqtt_broker_port), keepalive=60)
        client.loop_forever()
        while not client.connected_flag:
            print("In wait loop")
            time.sleep(1)
    except Exception as e:
        print(f"Connection Failed: {e}")
        sys.exit("quitting")

    print('...done.')
