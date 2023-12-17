import paho.mqtt.client as mqtt
 
class Publisher:

    def __init__(self):
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.client.connect("127.0.0.1", 60906)
        

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("connected OK")
        else:
            print("Bad connection Returned code=", rc)

    def on_disconnect(self, client, userdata, flags, rc=0):
        print(str(rc))

    def publish(self, topic, message):
        self.client.publish(topic, message)

    

