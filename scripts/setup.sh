pip install aries-cloudagent
git clone https://github.com/bcgov/indy-tails-server.git
git clone https://github.com/bcgov/von-network.git
sudo groupadd docker
sudo usermod -aG docker $USER
indy-tails-server/docker/manage up
von-network/manage up
