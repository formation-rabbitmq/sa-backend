## Prérequis pour tester rabbitmq et le projet sentiment analysis

---

### Démarrer le container

---

- Créer le réseau pour les containers `docker network create applications-networks`
- Construire l'image docker `docker build -t sabackend .`
- Lancer le serveur avec la commande `docker run -p 8000:8000 --network [DOCKER_NETWORK] -it sabackend sh -c "python load.py [ARGS] && python manage.py runserver 0.0.0.0:8000"` où les détails `[ARGS]` sont :

### Listes des arguments "[ARGS]" disponibles

> -u [USERNAME] : Nom d'utilisateur (Non requis - par défaut 'guest')
> 
> -p [PASSWORD] : Mot de passe (Non requis - par défaut 'guest')
> -rp [RABBITMQ_PORT] : Port du cluster rabbitmq  (Non requis - par défaut 5672)
> -rh [RABBITMQ_HOST] : Host du cluster rabbitmq (Requis)
> -fn [EXCHANGE_NOT_DURABLE_FOR_NOTIFICATIONS] : Si définie, implique que l'exchange pour les notifications n'est pas 'durable'
> -nn [EXCHANGE_NAME_FOR_NOTIFICATIONS] : Nom de l'exchange pour les notifications (Requis)
> -tn [EXCHANGE_TYPE_FOR_NOTIFICATIONS] : Type de l'exchange pour les notifications (Requis)
> -rkn [ROUTING_KEY_FOR_NOTIFICATIONS] : Routing key pour les notifications (Non requis)
> -fa [EXCHANGE_NOT_DURABLE_FOR_ANALYSES] : Si définie, implique que l'exchange pour les analyses n'est pas 'durable'
> -na [EXCHANGE_NAME_FOR_ANALYSES] : Nom de l'exchange pour les analyses (Requis)
> -ta [EXCHANGE_TYPE_FOR_ANALYSES] : Type de l'exchange pour les analyses (Requis)
> -rka [ROUTING_KEY_FOR_ANALYSES] : Routing key pour les analyses (Non requis)
