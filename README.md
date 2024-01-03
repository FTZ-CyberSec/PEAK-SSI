# PEAK-SSI
=======
### Moritz-Volkmann and Shashank-Tripathi for HAW Hamburg

### PEAK Project link - https://www.haw-hamburg.de/forschung/forschungsprojekte-detail/project/project/show/peak/

This repository for SSI side of the peak project. Main objectives are:
* Agents can issue, manage and revoke identities of users and a category of agents
* Create a schema for the verifiable credentials (VC)
* Docker based local indy network serving as framework for the management of identities
* Steps to register new DIDs

### This is a collection of scripts for the SSI authorization function in the PEAK project.
Eventually they are all supposed to be connected into a cohesive program.

### List of Scripts:

1. Connect.py -> connects two agents with each other
2. IssueCredential.py -> Creates DIDs for Agent A and B and Issues a non-Blockchain credential from Agent A to Agent B
3. IssuePersoCert.py -> Issues a persoCert type blockchain VC to an agent with user input of name, address, and date of birth
### To-Do / Next Steps

1. Blockchain Credential Issueing -> other types of Credentials(assetCert, ownerCert, warrantCert)
2. Presentation of Credential
3. Revocation of Credential
4. Creating Agents and Logic Specific to PEAK
5. Combining Scripts and exchanging hard coded stuff to inputs
6. UI?
