 aca-py start \
  --label Grid_Agent \
  -it http 0.0.0.0 8001 \
  -ot http \
  --admin 0.0.0.0 11001 \
  --admin-insecure-mode \
  --genesis-url http://82.165.247.238:9000/genesis \
  --seed Grid0000000000000000000000000000 \
  --endpoint http://localhost:8001/ \
  --debug-connections \
  --public-invites \
  --auto-provision \
  --wallet-type askar \
  --wallet-name Grid_Agent \
  --wallet-key secret \
  --tails-server-base-url http://localhost:6543/