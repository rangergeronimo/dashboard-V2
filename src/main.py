import time

from generador import Sensor
from pub import MqttPublisher

if __name__ == "__main__":
    # set broker connection
    broker = "localhost"
    port = 1883
    topic = "test"
    mqtt_publisher = MqttPublisher(broker, port, topic)

    # Initacialize class instance
    sensor = Sensor("Generador")

    print("Starting the main routine...")
    time.sleep(3)

    while True:
        data = sensor._return()  # Call retrun fx to get data from sensor hub

        # Publish to MQTT Broker
        mqtt_publisher.publish(data)

        time.sleep(2)  # wait before publish new record.

        if data["fuel"] <= 0:
            print("Program wil end now...")
            time.sleep(0.5)
            break
