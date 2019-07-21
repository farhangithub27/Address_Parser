
import re
import json
from Address_Parser import environment

class AddressParser:
    def __init__(self):

        self.unit = get_unit_codes() # Unit, Apartment, House
        self.level = get_level_codes() # ALso called  Floor
        self.street = get_street_codes() # Road, Alley, Bypass etc
        self.road_suffix = get_road_suffix_codes() # direction e.g North, South, South-East etc
        self.state = get_states_codes()

    def parse(self,string_address):
        address = string_address.strip()
        result = {
            'UnitType': None,
            'UnitNumber': None,
            'LevelType': None,
            'LevelNumber': None,
            'BuildingName': None,
            'StreetNumber1': None,
            'StreetNumber2': None,
            'StreetName': None,
            'StreetType': None,
            'StreetSuffix': None,
            'LocalityName': None,
            'StateTerritory': None,
            'Postcode':None}

        tokens = re.split(r'[,\s]\s*',address)

        print("Address Tokens are: " , tokens)
        # \s* matches zero or more of spaces (\s) after , and \s inside square brackets
        # or
        # tokens = address.split()# Only works with one argument. Default is space (\s)
        for t in range(0, len(tokens)):
            token = tokens[t].upper()
            hyphened_street_number = re.search(r'(\d*)-',token)

            # Finding Unit Type
            if token.upper() in self.unit or token.lower() in [x.lower() for x in list(self.unit.values())] \
                    and result['BuildingName'] is None:
                if token.upper() in self.unit:
                    result['UnitType']=self.unit[token.upper()].upper()
                else:
                    result['UnitType'] = token.upper()

            elif result['UnitType'] is not None and result['UnitNumber'] is None:
                if token.upper() in self.level or token.lower() in [x.lower() for x in list(self.level.values())] or hyphened_street_number \
                        or not re.fullmatch(r'[^a-z]{0,2}\d+[^a-z]{0,2}', token):
                    #print("Cannot be parsed. UnitNumber is missing in required format.")
                    return json.dumps({"parse_error":"Cannot be parsed. UnitNumber is missing in required format."})
                else:
                    result['UnitNumber'] = token

            # Finding Level Type
            elif token.upper() in self.level or token.lower() in [x.lower() for x in list(self.level.values())]:
                if token.upper() in self.level:
                    result['LevelType'] = self.level[token.upper()]
                else:
                    result['LevelType'] = token.upper()

            elif result['LevelType'] is not None and result['LevelNumber'] is None:
                if hyphened_street_number or token.isalpha() or not re.search(r'([a-zA-Z]{0,2}\d+[a-zA-Z]{0,2})', token):
                    return json.dumps({"parse_error": "Cannot be parsed. LevelNumber is missing in required format."})
                    #print("Cannot be parsed. LevelNumber is missing in required format.")
                    #break
                else:
                    result['LevelNumber'] = token

            # Finding Street Number
            elif hyphened_street_number and result['StreetNumber1'] is None:
                result['StreetNumber1'] = re.split(r'[\-]',token)[0]
                result['StreetNumber2'] = re.split(r'[\-]',token)[1]
            elif  (re.fullmatch(r'[^a-z]{0,2}\d+[^a-z]{0,2}', token) or token.isnumeric()) and result['StreetNumber1'] is None:
                #if result['BuildingName'] is not None:
                #    print("Cannot be parsed. Please check street number.")
                #else:
                result['StreetNumber1'] = token.upper()

            # Finding Street Type
            elif token.upper() in self.street or token.lower() in [x.lower() for x in list(self.street.values())] \
                and result['StreetNumber1'] is not None and result['StreetName'] is not None:
                if token.upper() in self.street:
                    result['StreetType'] = self.street[token.upper()].upper()
                else:
                    result['StreetType'] = token.upper()

            # Finding Street Suffix
            elif token.upper() in self.road_suffix or token.lower() in [x.lower() for x in list(self.road_suffix.values())]:
                if token.upper() in self.road_suffix:
                    result['StreetSuffix'] = self.road_suffix[token.upper()]
                else:
                    result['StreetSuffix'] = token.upper()

            # Finding Sate Territory
            elif token.upper() in self.state:
                result['StateTerritory'] = token.upper()
                print(token)

            # Finding Building Name
            elif token.isalpha() and result['BuildingName'] is None and result['StreetNumber1'] is None:# \
                    #and result['UnitType'] is not None and result['LevelType'] is not None:
                result['BuildingName'] = token.upper()

            elif result['BuildingName'] is not None and token.isalpha()and result['StreetNumber1'] is None:
                result['BuildingName'] = result['BuildingName']+" "+token.upper()

            # Finding Street Name
            elif result['StreetNumber1'] is not None and token.isalpha() and result['StreetName'] is None \
                    and token.upper() not in self.street and token.lower() not in [x.lower() for x in list(self.street.values())] \
                    and token.upper() not in self.road_suffix and token.lower() not in [x.lower() for x in list(self.road_suffix.values())] \
                    and token.upper() not in self.state and tokens[t+1].upper() not in self.state:
                result['StreetName'] = token.upper()

            elif result['StreetName'] is not None and token.isalpha() and result['StreetType'] is None \
                    and token.upper() not in self.street and token.lower() not in [x.lower() for x in list(self.street.values())] \
                    and token.upper() not in self.road_suffix and token.lower() not in [x.lower() for x in list(self.road_suffix.values())] \
                    and token.upper() not in self.state and tokens[t+1].upper() not in self.state:
                result['StreetName'] = result['StreetName'] + " " + token.upper()

            # Finding Suburb (Locality Name)
            elif token.isalpha() and result['LocalityName'] is None \
                    and tokens[t+1].upper() in self.state:
                result['LocalityName'] = token.upper()

            else:
                if token.isnumeric():
                    result['Postcode'] = token

        if result['StreetNumber1'] is None or result['StreetName'] is None or result['LocalityName'] is None \
            or result['StateTerritory'] is None:
            #return json.dumps({"parse_error": "Cannot be parsed. Please check Street Number, Street Name and Locality Name"})
            print ("Cannot be parsed. Please check Street Number, Street Name and Locality Name")
            #break

        else:
            print(result)
            #return json.dumps(result)



def get_unit_codes():
    return environment.AU_Unit_CODES

def get_level_codes():
    return environment.AU_LEVEL_CODES

def get_street_codes():
    return environment.AU_STRRET_CODES

def get_road_suffix_codes():
    return environment.AU_ROAD_SUFFIX_CODES

def get_states_codes():
    return environment.AU_STATES_CODES


if __name__== "__main__":
    parser = AddressParser()
    parser.parse("apt DD5D G 45 John James hospital 5-4 vilo rd w Acton nsw 2603")
