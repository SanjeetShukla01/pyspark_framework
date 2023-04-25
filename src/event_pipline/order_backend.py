# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     25/04/23 3:24 am
# File:             order_backend.py.py
# -----------------------------------------------------------------------
import json
import time


from src.utils.logging_utils import Logger
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers="localhost:29092")
# Here bootstrap server will be same as the docker kafka producer.

logger = Logger(__name__).get_logger()

logger.info(f"Going to be generating order after 10 Seconds")
logger.info(f"Will generate one unique order every 10 Seconds")

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i*123,
        "items": "Burgers, Sandwich"
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))

    logger.info(f"Done sending...{i}")
    time.sleep(10)

