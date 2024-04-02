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
2. createVC.py -> creates a verifiable credential of the defined types
3. getVC.py -> takes care of the credential exchange between agents
### To-Do / Next Steps

1. Presentation of Credential
2. Revocation of Credential
3. Creating Agents and Logic Specific to PEAK
4. Combining Scripts and exchanging hard coded stuff to inputs (Currently worked on)
5. UI?

### Requires at least Python 3.10!