import MQTTclient

from queue import Queue
from multiprocessing import Process


class Program:

    def __init__(self, config, topic_dispatcher):

        self.queue = Queue()

        self.config = config
        self.topic_dispatcher = topic_dispatcher

        self.subscriber = None
        self.publisher = None
        self.subscriber_process = None
        self.processor_process = None

    def message_processor(self, queue, publisher):
        while True:
            # Blocking call, no CPU waste here
            message = self.queue.get()  
            if message:
                callback = self.topic_dispatcher.get(message.topic, self.handle_unknown_topic)
                callback(message.topic, message.payload, publisher)

    def handle_unknown_topic(self, topic, data, publisher):
        # 알 수 없는 토픽 처리 로직
        print(f"Received message from unknown topic {topic}: {data}")

    def start(self):
        # Create MQTT Subscriber in a separate process
        self.subscriber = MQTTclient.Subcriber(config=self.config, queue=self.queue)
        self.publisher = MQTTclient.Publisher(config=self.config, queue=self.queue)

        subscriber_process = Process(target=self.subscriber.client.loop_forever)
        subscriber_process.start()


        # Process messages in a separate process
        processor_process = Process(target=self.message_processor, args=(self.queue, self.publisher))
        processor_process.start()

        # Join processes to the main process to keep them running
        subscriber_process.join()
        processor_process.join()
    