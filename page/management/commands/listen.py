from django.core.management.base import BaseCommand
from pika import BasicProperties

from page.rabbitmq import receive_message
from rich import print


def callback(ch, method, properties: BasicProperties, body: bytes):
    print("HEADERS", properties.headers, type(properties.headers))


class Command(BaseCommand):
    help = 'Listen for messages from RabbitMQ'

    def add_arguments(self, parser):
        parser.add_argument("-u", "--username", type=str, default="guest")
        parser.add_argument("-p", "--password", type=str, default="guest")
        parser.add_argument("-rp", "--port", type=int, default=5672)  # rabbitmq port
        parser.add_argument("-f", "--not_durable", action="store_true")
        parser.add_argument("-q", "--is_quorum", action="store_true")

        parser.add_argument("-rh", "--host", type=str, required=True)  # rabbitmq host
        parser.add_argument("-n", "--queue", type=str, required=True)  # queue name

    def handle(self, *args, **options):
        receive_message(
            host=options["host"],
            port=options["port"],
            username=options["username"],
            password=options["password"],
            queue_name=options["queue"],
            message_callback=callback,
            durable=False if options.get("not_durable", "fake") != "fake" else True,
            arguments={"x-queue-type": "quorum"} if options.get("is_quorum", "fake") != "fake" else None
        )
