~/indy-tails-server/docker/manage start
~/von-network/manage start
URL="http://82.165.247.238:9000/register"
PAYLOAD1='{
  "role": "ENDORSER",
  "alias": null,
  "did": null,
  "seed": "Platform000000000000000000000000"
}'
PAYLOAD2='{
  "role": "ENDORSER",
  "alias": null,
  "did": null,
  "seed": Grid0000000000000000000000000000"
  }'
PAYLOAD3='{
  "role": "ENDORSER",
  "alias": null,
  "did": null,
  "seed": Prosumer000000000000000000000001"
}'
curl -X POST \
     -H "Content-Type: application/json" \
     -d "$PAYLOAD1" \
     "$URL"
curl -X POST \
      -H "Content-Type: application/json" \
      -d "$PAYLOAD2" \
      "$URL"
curl -X POST \
      -H "Content-Type: application/json" \
      -d "$PAYLOAD3" \
      "$URL"

nohup bash platform.sh &
nohup bash grid.sh &
nohup bash 1prosumer.sh &
