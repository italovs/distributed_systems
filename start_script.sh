docker compose up -d

sleep 10s

diretorio_atual=$(pwd)

# gnome-terminal -x sh -c "cd $diretorio_atual; . ./env/bin/activate; python3 ./actuators_servers/lamp_server.py"
# gnome-terminal -x sh -c "cd $diretorio_atual; . ./env/bin/activate; python3 ./actuators_servers/humidifier_server.py"
# gnome-terminal -x sh -c "cd $diretorio_atual; . ./env/bin/activate; python3 ./actuators_servers/air_cond_server.py"
# gnome-terminal -x sh -c "cd $diretorio_atual; . ./env/bin/activate; python3 app/sensors/luminosity_sensor.py"
# gnome-terminal -x sh -c "cd $diretorio_atual; . ./env/bin/activate; python3 app/sensors/temperature_sensor.py"
# gnome-terminal -x sh -c "cd $diretorio_atual; . ./env/bin/activate; python3 app/sensors/presence_sensor.py"

osascript -e "tell application \"Terminal\" to do script \"cd $diretorio_atual; . ./env/bin/activate; python3 ./actuators_servers/lamp_server.py;\""
osascript -e "tell application \"Terminal\" to do script \"cd $diretorio_atual; . ./env/bin/activate; python3 ./actuators_servers/humidifier_server.py;\""
osascript -e "tell application \"Terminal\" to do script \"cd $diretorio_atual; . ./env/bin/activate; python3 ./actuators_servers/air_cond_server.py;\""
osascript -e "tell application \"Terminal\" to do script \"cd $diretorio_atual; . ./env/bin/activate; python3 app/sensors/luminosity_sensor.py;\""
osascript -e "tell application \"Terminal\" to do script \"cd $diretorio_atual; . ./env/bin/activate; python3 app/sensors/temperature_sensor.py;\""
osascript -e "tell application \"Terminal\" to do script \"cd $diretorio_atual; . ./env/bin/activate; python3 app/sensors/presence_sensor.py;\""

flask run