import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--username", type=str, default="guest")
	parser.add_argument("-p", "--password", type=str, default="guest")
	parser.add_argument("-rp", "--port", type=int, default=5672)  # rabbitmq port
	parser.add_argument("-rh", "--host", type=str, required=True)  # rabbitmq host

	# notifications
	parser.add_argument("-rkn", "--routing_key_notifications", type=str, default="")  # routing key
	parser.add_argument("-fn", "--not_durable_notifications", action="store_true")
	parser.add_argument("-nn", "--exchange_notifications", type=str, required=True)  # exchange name
	parser.add_argument(
		"-tn", "--type_notifications", type=str, choices=["direct", 'topic', 'headers', 'fanout'], required=True
	)  # exchange type

	# analyses
	parser.add_argument("-rka", "--routing_key_analyses", type=str, default="")  # routing key
	parser.add_argument("-fa", "--not_durable_analyses", action="store_true")
	parser.add_argument("-na", "--exchange_analyses", type=str, required=True)  # exchange name
	parser.add_argument(
		"-ta", "--type_analyses", type=str, choices=["direct", 'topic', 'headers', 'fanout'], required=True
	)  # exchange type

	args: argparse.Namespace = parser.parse_args()

	with open("conf.env", "w") as file:
		file.write("\n".join([
			f"RABBITMQ_HOST={args.host}",
			f"RABBITMQ_PORT={args.port}",
			f"RABBITMQ_USERNAME={args.username}",
			f"RABBITMQ_PASSWORD={args.password}",
			f"RABBITMQ_EXCHANGE_NAME_NOTIFICATIONS={args.exchange_notifications}",
			f"RABBITMQ_EXCHANGE_NAME_ANALYSES={args.exchange_analyses}",
			f"RABBITMQ_EXCHANGE_TYPE_NOTIFICATIONS={args.type_notifications}",
			f"RABBITMQ_EXCHANGE_TYPE_ANALYSES={args.type_analyses}",
			f"RABBITMQ_EXCHANGE_ROUTING_NOTIFICATIONS={args.routing_key_notifications}",
			f"RABBITMQ_EXCHANGE_ROUTING_ANALYSES={args.routing_key_analyses}",
			f"RABBITMQ_EXCHANGE_DURABLE_NOTIFICATIONS={'false' if args.not_durable_notifications else 'true'}",
			f"RABBITMQ_EXCHANGE_DURABLE_ANALYSES={'false' if args.not_durable_analyses else 'true'}",
		]))
		file.close()
