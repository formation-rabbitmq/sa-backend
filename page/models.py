import os
from django.db import models

from .rabbitmq import send_message


class Sentiment(models.Model):
	message = models.CharField(max_length=255)
	sentiment = models.CharField(max_length=255, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		# rabbitMQ
		send_message(
			host=os.getenv("RABBITMQ_HOST"),
			port=int(os.getenv("RABBITMQ_PORT")),
			username=os.getenv("RABBITMQ_USERNAME"),
			password=os.getenv("RABBITMQ_PASSWORD"),
			exchange_name=os.getenv("RABBITMQ_EXCHANGE_NAME_NOTIFICATIONS"),
			exchange_type=os.getenv("RABBITMQ_EXCHANGE_TYPE_NOTIFICATIONS"),
			message=str(self.message),
			routing_key=os.getenv("RABBITMQ_EXCHANGE_ROUTING_NOTIFICATIONS"),
			durable=True if os.getenv("RABBITMQ_EXCHANGE_DURABLE_NOTIFICATIONS") == "true" else False
		)
		send_message(
			host=os.getenv("RABBITMQ_HOST"),
			port=int(os.getenv("RABBITMQ_PORT")),
			username=os.getenv("RABBITMQ_USERNAME"),
			password=os.getenv("RABBITMQ_PASSWORD"),
			exchange_name=os.getenv("RABBITMQ_EXCHANGE_NAME_ANALYSES"),
			exchange_type=os.getenv("RABBITMQ_EXCHANGE_TYPE_ANALYSES"),
			message=str(self.message),
			routing_key=os.getenv("RABBITMQ_EXCHANGE_ROUTING_ANALYSES"),
			durable=True if os.getenv("RABBITMQ_EXCHANGE_DURABLE_ANALYSES") == "true" else False
		)
