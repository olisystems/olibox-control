

import click
import toml


@click.command()
@click.option('--mqtt-broker-ip', prompt='MQTT broker IP', help='MQTT broker IP', default='unbelievable-politician.cloudmqtt.com')
@click.option('--mqtt-broker-port', prompt='MQTT broker port', help='Mqtt broker port', default='8883')
@click.option('--ssl-cert-path', prompt='What is the path of the SSL certficate?', default='ca-certificates.crt')
@click.option('--mqtt-username', prompt='MQTT username', default='gmnzhypg')
@click.option('--mqtt-password', prompt='MQTT password', hide_input=True, confirmation_prompt=True)
@click.option('--project-id', prompt='project id', help='Project ID', default='dose')
@click.option('--oli-box-id', prompt='oli box id', help='Oli box ID', default='6')
@click.option('--dest-type', prompt='destination type', help='destination type i.e. charging station', default='chargingStation')
@click.option('--command', prompt='command', help='Command i.e. set charging limit', default='setChargingLimit')
def init(mqtt_broker_ip,
         mqtt_broker_port,
         ssl_cert_path,
         mqtt_username,
         mqtt_password,
         oli_box_id,
         project_id,
         dest_type,
         command
         ):
    config = f"""

    title = "OLI Box Config"

    [mqtt_connection]
    mqtt_broker_ip = '{mqtt_broker_ip}'
    mqtt_broker_port = '{mqtt_broker_port}'
    ssl_cert_path = '{ssl_cert_path}'
    mqtt_username = '{mqtt_username}'
    mqtt_password = '{mqtt_password}'

    [topic_config]
    project_id = '{project_id}'
    oli_box_id = '{oli_box_id}'
    dest_type = '{dest_type}'
    command = '{command}'
    """
    parsed_config = toml.loads(config)
    formatted_config = toml.dumps(parsed_config)

    with open('config.toml', 'w+') as f:
        f.write(formatted_config)
