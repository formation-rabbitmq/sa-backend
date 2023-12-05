
## 0. Construction de l'image

> ```docker build -t sabackend .```


## 1. Lancement du serveur

> ```docker run -p 8000:8000 --network applications-networks sabackend```


## 2. Écouter les messages depuis rabbitMQ

> ```docker exec -it --network applications-networks sabackend sh 'python manage.py listen_messages' ```
