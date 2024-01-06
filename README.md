# -road_to_nowhere
a repository where my progress will be, or maybe it won’t be

### Веб Приложение

С использованием технологий:

- Docker 
- Compose 
- Flask 
- Gunicorn 
- PostgreSQL 
- pgamin
- nginx (reverse proxy) 



```
# Билд
sudo docker-compose -f docker-compose.dev.yml build
# Запуск
sudo docker-compose -f docker-compose.dev.yml up
# Запуск в фоне
sudo docker-compose -f docker-compose.dev.yml up -d
# Остановка
sudo docker-compose -f docker-compose.dev.yml stop
```
Чтобы обращаться к домену описанному в nginx.conf нужно или проделегировать домен (но это отдельная тема),
либо прописать в hosts соотв. IP домену. Если запуск предполагается только локально, то можно просто удалить server_name azzrael_code.yt;
из nginx.conf. 


## Внешние тома

База и приложение пробрасываются на хост! На деве - это норм, на проде - нужно спрятать внутрь!

