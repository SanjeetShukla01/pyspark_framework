### Event Driven Architecture





5. Imagine you have a high-rate producing Kafka Producer, but your consumers are unable to keep up with the incoming data. How do you resolve this issue? The interviewer is trying to assess your knowledge of Lag Monitoring and how you handle it & is your system really notify the stack holders in case of lag?

2. Suppose your streaming pipeline fails and you need to restart it - how does Kafka help you read the events or messages that were not processed due to the failure? The interviewer wants to test your understanding of Kafka's retention period.

3. Another important aspect of a Kafka streaming pipeline is whether it is idempotent - in case of failure, does it generate the same result or add duplicate results in different sinks used in the pipeline?

4. If you have a Kafka topic with a large number of partitions, how do you ensure an even distribution of data and efficient processing in each partition?

5. Have you ever used headers in Kafka events or messages? The interviewer may ask you about the benefits of passing some pieces of information in Kafka headers instead of just passing the payload.

6. How do you handle late-arriving data and race conditions in your Kafka streaming pipeline?

7. Finally, if your streaming pipeline is only reading data with some source and writing to some sink with minimal transformation, the interviewer might ask you about Kafka Connect and how you could have implemented the same thing using it instead of Kafka and Spark Streaming or Kafka and Apache Flink. Be ready for these types of questions and show your versatility in using different tools and approaches to tackle the same problem.



Github Rep:
https://github.com/irtiza07/python-kafka-demo
https://www.youtube.com/watch?v=qi7uR3ItaOY

https://github.com/Sanjeet01/python-notebooks-for-apache-kafka/blob/main/01%20-%20Producer.ipynb



https://github.com/bhimrazy/kafka-in-docker-and-python-fastapi


