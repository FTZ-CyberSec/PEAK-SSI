from exchangeVC import *
from connect import connect_agents
import time

def new_prosumer(port: int = 11002):
    step = 0
    while step < 6 or step == 99:
        match step:
            case 0:
                # Connect agent to platform and grid agent (Replace 11002 with the port of the new agent)
                connect_agents(port, "platform")
                connect_agents(port, "grid")
                step += 1
            case 1:
                # Issue persoCert
                issue_credential("persoCert", port)
                print("persoCert is issued")
                step += 1
            case 2:
                # Issue gridCert
                # TODO: Debug
                presentation = present_credential("persoCert", port)
                print(presentation)
                if presentation is not None and presentation['verified'] == 'true':
                    print("persoCert is verified, here is the data: \n")
                    print("Name: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['name']['raw'])
                    print("Adresse: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['adress']['raw'])
                    print("Geburtsdatum: ", presentation['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['birthdate']['raw'])
                    issue_credential("gridCert", port)
                    step += 1
                else:
                    print("persoCert could not be verified")
                    step = 99
            case 3:
                # Issue ownerCert
                issue_credential("ownerCert", port)
                step += 1
            case 4:
                # Issue assetCert
                presentation_owner = present_credential("ownerCert", port)
                presentation_grid = present_credential("gridCert", port)
                if presentation_owner is not None and presentation_grid is not None and presentation_owner['verified'] == 'true' and presentation_grid['verified'] == 'true':
                    print("ownerCert is verified, here is the data: \n")
                    print("Lizenznummer: ", presentation_owner['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['lizenznummer']['raw'])
                    print("gridCert is verified, here is the data: \n")
                    print("ZaehlerID: ", presentation_grid['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['zaehlerID']['raw'])
                    print("SmartMeterID: ", presentation_grid['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['smartMeterID']['raw'])
                    print("Marktlokation: ", presentation_grid['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['marktlokation']['raw'])
                    print("HEMS: ", presentation_grid['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['HEMS']['raw'])
                    print("Steuerbox: ", presentation_grid['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['steuerbox']['raw'])
                    print("VerbrauchpA: ", presentation_grid['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['verbrauchpA']['raw'] + "kWh")
                    issue_credential("assetCert", port)
                    step += 1
                else:
                    print("ownerCert could not be verified")
                    step = 99
            case 5:
                # Issue warrantCert
                presentation = present_credential("persoCert", port)
                presentation_asset = present_credential("assetCert", port)
                presentation_owner = present_credential("ownerCert", port)
                presentation_grid = present_credential("gridCert", port)
                if presentation_asset is not None and presentation_owner is not None and presentation_grid is not None and presentation is not None and presentation_asset['verified'] == 'true' and presentation_owner['verified'] == 'true' and presentation_grid['verified'] == 'true' and presentation['verified'] == 'true':
                    print("assetCert is verified, here is the data: \n")
                    print("AnlagenTyp: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['anlagenTyp']['raw'])
                    print("StellschritteP: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['stellschritteP']['raw'])
                    print("Pmax: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['Pmax']['raw'])
                    print("Pmin: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['Pmin']['raw'])
                    print("EnergieArt: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['energieArt']['raw'])
                    print("Steuerbarkeit: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['steuerbarkeit']['raw'])
                    print("SpeicherKapa: ", presentation_asset['by_format']['pres']['indy']['requested_proof']['revealed_attrs']['speicherKapa']['raw'])
                    issue_credential("warrantCert", port)
                    print("Success! You can now trade on the platform")
                    return 1
                else:
                    print("assetCert could not be verified")
                    step = 99
            case 99:
                print("Error, some of your credentials could not be verified")
                return 0


