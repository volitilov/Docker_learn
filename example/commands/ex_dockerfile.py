# ex_dockerfile.py

# Примеры Dockerfile

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER volitilov <volitilov@gmail.com>
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
        >/usr/share/nginx/html/index.html
EXPOSE 80
# Первая инструкция в Dockerfile всегда должна быть FROM, указывающая, из 
# какого образа нужно построить образ. В нашем примере мы строим образ из 
# базового образа ubuntu версии 14:04. 
# Далее мы указываем инструкцию MAINTAINER, сообщающую Docker автора образа 
# и его email. Это полезно, чтобы пользователи образа могли связаться с 
# автором при необходимости. 
# Инструкция RUN исполняет команду в конкретном образе. В нашем примере с 
# помощью ее мы обновляем APT репозитории и устанавливаем пакет с NGINX, 
# затем создаем файл /usr/share/nginx/html/index.html.
# По-умолчанию инструкция RUN исполняется внутри оболочки с использованием 
# обертки команд /bin/sh -c. Если вы запускаете инструкцию на платформе 
# без оболочки или просто хотите выполнить инструкцию без оболочки, вы 
# можете указать формат исполнения:
    RUN ["apt-get", "install", "-y", "nginx"]
# Мы используем этот формат для указания массива, содержащего команду для 
# исполнения и параметры команды.
# Далее мы указываем инструкцию EXPOSE, которая говорит Docker, что приложение 
# в контейнере должно использовать определенный порт в контейнере. Это не 
# означает, что вы можете автоматически получать доступ к сервису, запущенному 
# на порту контейнера (в нашем примере порт 80). По соображениям безопасности 
# Docker не открывает порт автоматически, но ожидает, когда это сделает 
# пользователь в команде docker run. Вы можете указать множество инструкций 
# EXPOSE для указания, какие порты должны быть открыты. Также инструкция 
# EXPOSE полезна для проброса портов между контейнерами.


FROM ubuntu:14.04
MAINTAINER volitilov <volitilov@infoboxcloud.com>
ENV REFRESHED_AT 2014–10–16
RUN apt-get -qq update
# Используя кеш сборок можно строить образы из Dockerfile в форме простых 
# шаблонов. Например шаблон для обновления APT-кеша в Ubuntu
# Инструкция ENV устанавливает переменные окружения в образе. В данном случае 
# мы указываем, когда шаблон был обновлен. Когда необходимо обновить 
# построенный образ, просто нужно изменить дату в ENV. Docker сбросит кеш и 
# версии пакетов в образе будут последними.


ADD latest.tar.gz /var/www/wordpress/
# архив tar.gz будет распакован в /var/www/wordpress. Если путь назначения не 
# указан — будет использован полный путь включая директории.

