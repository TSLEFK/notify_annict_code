import botostubs
import boto3

class SNS:

    def __init__(self) -> None:
        self.client = boto3.client('sns') # type: botostubs.SNS

    def send_message(self, topic_arn:str, message: str):
        self.client.publish(
            Message=message,
            TopicArn=topic_arn
        )