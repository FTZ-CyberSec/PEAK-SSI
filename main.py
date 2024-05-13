from connect import connect_agents
from config import *
from exchangeVC import *
from authenticate import new_prosumer

# Run on first startup of SSI Network
"""
for type in vc_types:
    define_credential(type)
"""
# In case of new agent, the following steps are necessary:
# Connect agent to platform and grid agent (Replace 11002 with the port of the new agent)
"""
connect_agents(11002, "platform")
connect_agents(11002, "grid")
"""
# Test with one prosumer
new_prosumer(11003)

