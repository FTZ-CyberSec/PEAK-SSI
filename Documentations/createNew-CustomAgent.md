# Create custom Agents
# Points to remember: use public I.P address for genesis (like http://82.165.247.238:9000/genesis) 
# rather than 0.0.0.0 or localhost

aca-py start 
--label MarketAgent  \
-e 0.0.0.0::7000 \
--genesis-url http://82.165.247.238:9000/genesis \
-it http 0.0.0.0 7001 \
-ot http \
--admin 0.0.0.0 7002 \
--admin-insecure-mode


-e is endpoint URL, -it is inbound url and -ot is outbound url

### Inbound URL
An "inbound URL" refers to the URL through which the agent receives incoming communications or messages.
This URL is used by other agents or services to connect with and send information to the agent.
It's an important part of the configuration for agents that need to be accessible over a network, 
ensuring that they can properly receive and process inbound requests or messages.
