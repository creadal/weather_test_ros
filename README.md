# Инструкция по запуску
## Настройка
Для работы необходима **Ubuntu 16.04** с установленным **ROS Kinetic** (desktop-full)

Создаем директорию для catkin:
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
Создаем ROS-пакет:
```
$ cd ~/catkin_ws/src
$ catkin_create_pkg weather_test std_msgs rospy roscpp
```
Создаем папку `/scripts` в `~/catkin_ws/src/weather_test` и добавляем туда оба скрипта наших узлов.
Затем из `~/catkin_ws` вызываем команду `$ catkin_make` чтобы собрать проект.

## Запуск
Сперва необходимо запустить **roscore** одноименной командой.
Узлы будем запускать в отдельных терминалах.
В каждом из таких терминалов предварительно необходимо прописывать: 
```
$ source catkin_ws/devel/setup.bash
```
Можем запустить узел паблишера командой 
```
rosrun weather_test talker.py LAT LON
``` 
где на месте LAT и LON подставляем широту и долготу. 
Например, чтобы отслеживать погоду в Петергофе пишем: 
```
$ rosrun weather_test talker.py 59.8845 29.8852
```
Для запуска подписчика пишем: 
```
$ rosrun weather_test listener.py
```
