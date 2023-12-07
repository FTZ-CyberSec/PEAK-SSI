# Create new custom node on von-network

Go to folder von-network/ or von-network-main/

sudo ./manage start
If no error, check the ip-address's port 9000 from your local browser (check that OpenVPN is running), 
''hostname -I'
it will give you IP address like 82.165.247.238 

docker volume create von_node5-data

docker run -ti -p 9709:9709 -p 9710:9710 --name von_node5_1 --network  von_von -v von_node5-data:/home/indy/ledger von-network-base /bin/bash

Now, open another terminal (duplicate the session). Run the following commands:
/home/indy/ledger/sandbox/pool_transactions_genesis .
/home/indy/ledger/sandbox/domain_transactions_genesis .
docker cp pool_transactions_genesis von_node5_1:/home/indy/ledger/sandbox/pool_transactions_genesis
docker cp domain_transactions_genesis von_node5_1:/home/indy/ledger/sandbox/domain_transactions_genesis

When containers have started. Copy pool_transactions_genesis and domain_transactions_genesis files from another terminal

to be continued
