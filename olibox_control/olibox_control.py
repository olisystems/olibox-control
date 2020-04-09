
import atexit
import control_pkg as pkg


@atexit.register
def main():
    pkg.config_mqtt()


#pkg.init()
