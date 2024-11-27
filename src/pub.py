import json
from dataclasses import dataclass

import paho.mqtt.client as mqtt

from logs import logger

# Initacialize logger
log = logger("Loggerpub", "logs/pub.log")


@dataclass
class MqttPublisher:
    broker: str
    port: int
    topic: str

    def __post_init__(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker, self.port)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Connected to MQTT Broker!")
        else:
            log.info(f"Failed to connect, return code {rc}")

    def publish(self, data):
        message = json.dumps(data)
        result = self.client.publish(self.topic, message)
        status = result.rc

        if status == 0:
            log.info(f"Data publish to {self.broker}:{self.topic} with {message}")
        else:
            log.info(f"Failed to send message to topic {self.broker}:{self.topic}")
