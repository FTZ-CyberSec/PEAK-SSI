~/indy-tails-server/docker/manage start
~/von-network/manage start
echo "If this is your first startup, go to the server-adress port 9000 and register the relevant DIDs"
nohup bash platform.sh &
nohup bash grid.sh &
nohup bash 1prosumer.sh &
