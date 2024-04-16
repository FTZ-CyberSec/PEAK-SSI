# usr/bin/bash

 aca-py start \
  --label Platform_Agent \
  -it http 0.0.0.0 8000 \
  -ot http \
  --admin 0.0.0.0 11000 \
  --admin-insecure-mode \
  --genesis-url http://82.165.247.238:9000/genesis \
  --seed Platform000000000000000000000000 \
  --endpoint http://localhost:8000/ \
  --debug-connections \
  --public-invites \
  --auto-provision \
  --wallet-type askar \
  --wallet-name Platform_Agent \
  --wallet-key secret \
  --tails-server-base-url http://localhost:6543/
