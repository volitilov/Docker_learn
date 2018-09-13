# install.py

# Сдесь хронится информация о том как установить Docker

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

$ sudo apt-get update
# Для начала обновим базу данных пакетов

$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
# Добавьте ключ GPG официального репозитория Docker в вашу систему

$ sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
# Добавим репозиторий Docker в список источников пакетов утилиты APT

$ sudo apt-get update
# Обновим базу данных пакетов информацией о пакетах Docker из вновь 
# добавленного репозитория

$ sudo apt-get install -y docker-engine
# Далее, наконец-то, установим Docker

$ sudo systemctl status docker
# Проверим, что процесс запущен
