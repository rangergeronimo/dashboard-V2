import json
from datetime import datetime

import customtkinter as ctk
import paho.mqtt.client as mqtt
import ttkbootstrap as tb
from PIL import Image

# MQTT client setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# WINDOWS DEFINITION
root = tb.Window(themename="cosmo", size=(600, 600))
root.title("IoT Fuel Monitor")


def get_actual_time() -> None:
    now = datetime.now().strftime("%Y-%m-%d  %I:%M:%S %p")
    realtime_label.configure(text=now)
    realtime_label.after(1, get_actual_time)


def check_for_alarm():
    if fuel_floodgauge.variable.get() <= 0:
        indicator_1.configure(
            bootstyle="danger",
            text="NOK",
        )


def subcribe_to_broker(broker_address: str, port: int, topic: str) -> None:
    client.on_message = on_message
    client.connect(broker_address, port)
    client.subscribe(topic)
    client.loop_start()


def on_message(client, userdata, message):
    fuel = json.loads(message.payload)
    fuel_floodgauge.configure(value=fuel["fuel"])
    check_for_alarm()
    root.update()


# WIDGETS DEFINITIONS
realtime_label = tb.Label(root, bootstyle="inverse")
realtime_label.grid(row=0, column=3, padx=10, pady=5, sticky="n")


fuel_floodgauge = tb.Floodgauge(
    root,
    bootstyle="info",
    font=("Helvetica", 10),
    mask="{} L",
    orient="vertical",
    length=150,
    maximum=105,
    value=0,
)
fuel_floodgauge.grid(row=2, column=0, padx=10, pady=10)

image = ctk.CTkImage(
    dark_image=Image.open("images/pic.jpg"),
    size=(450, 410),
)
image_label = ctk.CTkLabel(root, image=image, text="")
image_label.grid(row=2, column=3, pady=20)

indicator_1 = tb.Label(
    root,
    bootstyle="success",
    font=("Arial", 16, "bold"),
    text="OK",
)
indicator_1.grid(row=1, column=3, pady=5, sticky="nw", ipady=20, ipadx=20)


# GRID SET UP
root.columnconfigure((0, 1, 2, 3), weight=2)

if __name__ == "__main__":
    # MQTT broker details
    broker_address = "localhost"
    port = 1883
    topic = "test"
    subcribe_to_broker(broker_address, port, topic)

    get_actual_time()

    root.mainloop()
