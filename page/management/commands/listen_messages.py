from django.core.management.base import BaseCommand

from page.rabbitmq import receive_message


class Command(BaseCommand):
    help = 'Listen for messages from RabbitMQ'

    def handle(self, *args, **options):
        receive_message(
            queue_name="sa.message.queues.direct.logic"
        )
