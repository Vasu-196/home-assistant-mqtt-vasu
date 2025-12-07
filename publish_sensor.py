import json
import time
import random
import paho.mqtt.client as mqtt

# ========= REQUIRED BY ASSIGNMENT =========
student_name = "Adi Vasudeva Rao"
unique_id = "42130603"
topic = "home/vasu-2025/sensor"   # example: home/vasu-2025/sensor
# =========================================

# Extra sensor key (you can rename this to sound / light / vibration etc.)
extra_key = "motion"

# Simulate extra sensor value (no real sensor needed!)
def get_extra_value():
    return random.choice([0, 1])

MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60

client = mqtt.Client()

# If you use username/password in Mosquitto, uncomment and edit:
# client.username_pw_set("mqtt_user", "mqtt_password")

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")

client.on_connect = on_connect
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE)
client.loop_start()

try:
    while True:
        payload = {
            "student_name": student_name,
            "unique_id": unique_id,
            "temperature": 25,
            "humidity": 60,
            extra_key: get_extra_value()
        }
        payload_str = json.dumps(payload)
        result = client.publish(topic, payload_str, qos=1)
        status = result[0]
        if status == 0:
            print(f"Published -> topic: {topic} payload: {payload_str}")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(5)   # send every 5 seconds
except KeyboardInterrupt:
    print("Stopping publisher...")
finally:
    client.loop_stop()
    client.disconnect()
