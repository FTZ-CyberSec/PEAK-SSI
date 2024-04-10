from connect import connect_agents
from config import *
from exchangeVC import *

# Run on first startup of SSI Network
"""
for type in vc_types:
    define_credential(type)
"""

present_credential("persoCert")
perform_credential_exchange("ownerCert")
present_credential("ownerCert")