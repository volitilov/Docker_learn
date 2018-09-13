# cli.py

# Сдесь хронится командной интерфейс

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

$ docker [опция] [команда] [аргументы]

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

$ docker
# Для просмотра всех доступных подкоманд

$ docker docker-subcommand --help
# Для просмотра подробностей использования каждой из подкоманд

$ docker info
# Для просмотра общей справки Docker



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Options:

--config string
# Располажение кофигурационных файлов клиента (default "/home/x/.docker")

-D, --debug
# Включение DEBUG режима

--help
# Показать как пользование

-H, --host list          
Daemon socket(s) to connect to

-l, --log-level string   
Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")

--tls
Use TLS; implied by --tlsverify

--tlscacert string
Trust certs signed only by this CA (default "/home/x/.docker/ca.pem")

--tlscert string
Path to TLS certificate file (default "/home/x/.docker/cert.pem")

--tlskey string
Path to TLS key file (default "/home/x/.docker/key.pem")

--tlsverify
Use TLS and verify the remote

-v, --version
# Показать информацию о версии и выйти



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Management Commands:

container
# Показывает интерфейс к containers

image
# Показывает интерфейс к images
  
network
# Показывает интерфейс к networks

node
# Показывает интерфейс к Swarm nodes

plugin 
# Показывает интерфейс к plugins
  
secret
# Показывает интерфейс к Docker secrets

service
# Показывает интерфейс к services

stack
# Показывает интерфейс к Docker stacks

swarm
# Показывает интерфейс к Swarm

system
# Показывает интерфейс к Docker

volume
# Показывает интерфейс к volumes



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Commands:

attach
Attach local standard input, output, and error streams to a running container

build
# Если в директории с Dockerfile выполнить команду docker build, то мы 
# получим образ на основе Dockerfile

commit
# Когда вы делаете коммит образа, новый образ сохраняется локально, то есть 
# на вашей машине.

cp
Copy files/folders between a container and the local filesystem
  
create
# Создание нового контейнера

diff
Inspect changes to files or directories on a container's filesystem

events
Get real time events from the server

exec
Run a command in a running container

export
Export a container's filesystem as a tar archive

history
# Показать историю image

images
# Просмотр образов, загруженных на вашу машину

import
Import the contents from a tarball to create a filesystem image

info
Display system-wide information

inspect
Return low-level information on Docker objects

kill
# Убить один или несколько работающих containers

load
Load an image from a tar archive or STDIN

login
# Войти в Docker registry

logout
# Выйти из Docker registry

logs
Fetch the logs of a container

pause
Pause all processes within one or more containers

port
List port mappings or a specific mapping for the container

ps
# Список работающих контейнеров

pull
# Загружает image или repository из registry

push
# Отправить image или repository в registry

rename
# Переименование контейнера

restart
# Рестарт один или несколько контейнеров

rm
# Удаляляет один или несколко контейнеров

rmi
# Удаляет один или несколько images

run
# Запустить контейнер с загруженным образом.
# Если на момент выполнения подкоманды run образ ещё не был загружен, клиент 
# Docker сперва загрузит образ, а затем запустит контейнер с этим образом

save
Save one or more images to a tar archive (streamed to STDOUT by default)

search
# Исчет образы, доступные в Docker Hub

start
# Запуск одного или нескольких остановленных котейнеров

stats
Display a live stream of container(s) resource usage statistics

stop идентификатор-контейнера
# Остановка одного или несколько запущенных containers
# Идентификатор-контейнера можно найти с помощью команды docker ps

tag
Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

top
Display the running processes of a container

unpause
Unpause all processes within one or more containers

update
# Обновить конфигурацию у одного или нескольких containers

version
# Показывает версию Docker

wait
Block until one or more containers stop, then print their exit codes
