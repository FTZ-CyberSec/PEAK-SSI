from connect import connect_agents
from config import *
from exchangeVC import *
from authenticate import new_prosumer
from delete_connections import delete_all_connections
from tests.test_createVC import TestNew_Prosumer
from tests.test_authenticate import TestNew_Prosumer as TestNew_Prosumer2
from tests.test_connect import TestConnectAgents
from tests.test_exchangeVC import TestExchangeVC
import unittest

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
# At the moment, there are 8 prosumers from port 11002 to 11009
unittest.main()

