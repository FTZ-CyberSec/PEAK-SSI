from connect import connect_agents
from config import vc_types
from exchangeVC import perform_credential_exchange, define_credential, present_credential

# Run on first startup of SSI Network
"""
for type in vc_types:
    define_credential(type)
"""

present_credential("persoCert")
