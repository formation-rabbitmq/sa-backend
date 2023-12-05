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
			exchange_name="sa.message.queues.direct.notifications",
			exchange_type="direct",
			message=str(self.message),
			routing_key="notification"
		)
		send_message(
			exchange_name="sa.message.queues.direct.analyses",
			exchange_type="direct",
			message=str(self.message),
			routing_key="analyse"
		)
