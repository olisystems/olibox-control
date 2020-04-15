
import atexit
import olibox_control.control_pkg as pkg


@atexit.register
def main():
    pkg.config_mqtt()


pkg.init()
