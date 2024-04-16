from connect import connect_agents
from config import *
from exchangeVC import *

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

presentation = present_credential("persoCert")
# extract the values of "raw" for name, adress, and birthdate from present_credential("persoCert")
if presentation['verified'] == 'true':
    print("persoCert is verified, here is the data: \n")
    print("Name: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['name']['raw'])
    print("Adresse: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['adress']['raw'])
    print("Geburtsdatum: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['birthdate']['raw'])
else:
    print("persoCert could not be verified")
# if input("Please input 'y' if the VC data is correct: ") == 'y':
if True:
    print("VC data is correct")
    # issue_credential("ownerCert")
    presentation = present_credential("ownerCert")
    if presentation['verified'] == 'true':
        print("ownerCert is verified, here is the data: \n")
        print("Lizenznummer: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['lizenznummer']['raw'])
    else:
        print("ownerCert could not be verified")
    # issue_credential("gridCert")
    presentation1 = present_credential("gridCert")
    print(presentation1)
    if presentation1['verified'] == 'true':
        print("gridCert is verified, here is the data: \n")
        print("ZaehlerID: ", presentation1['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['zaehlerID']['raw'])
    else:
        print("gridCert could not be verified")
else:
    print("persoCert data is not eligible for ownerCert issuance")

