# PEAK-SSI
=======
### Moritz-Volkmann and Shashank-Tripathi for HAW Hamburg

### PEAK Project link - https://www.haw-hamburg.de/forschung/forschungsprojekte-detail/project/project/show/peak/

This repository for SSI side of the peak project. Main objectives are:
* Agents can issue :heavy_check_mark:, present :heavy_check_mark: and revoke identities of users and a category of agents
* Create a schema for the verifiable credentials (VC) :heavy_check_mark:
* Docker based local indy network serving as framework for the management of identities :heavy_check_mark:
* Steps to register new DIDs :heavy_check_mark:

### This is a collection of scripts for the SSI authorization function in the PEAK project.
Eventually they are all supposed to be connected into a cohesive program.

### List of Scripts:

1. connect.py -> connects two agents with each other
2. exchangeVC.py -> includes functions to define, issue and present the defined VCs
3. createVC.py -> helper functions to create VCs
4. config.py -> configuration file for the project, where the server url and ports are defined

### To-Do / Next Steps

1. Revocation of Credential
2. Creating Agents and Logic Specific to PEAK
3. UI?

### Requires at least Python 3.10!