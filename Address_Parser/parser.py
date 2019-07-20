
import re
from Address_Parser import environment

class AddressParser():
    def __init__(self):

        self.unit = get_unit_codes() # Unit, Apartment, House
        self.level = get_level_codes() # ALso called  Floor
        self.street = get_street_codes() # Road, Alley, Bypass etc
        self.road_suffix = get_road_suffix_codes() # direction e.g North, South, South-East etc
        self.state = get_states_codes()

        self.unit_set = set(self.unit.keys()) | set(self.unit.values())


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
        print(tokens)
        # \s* matches zero or more of spaces (\s) after , and \s inside square brackets

        # or
        # tokens = address.split()# Only works with one argument. Default is space (\s)
        for t in range(0, len(tokens)):
            token = tokens[t]
            #print(token)
            hyphened_street_number = re.search(r'(\d*)-',token)
            #nonhyphened_street_number = re.search(r'(\d)\d*', token)

            if token.upper() in self.unit or token.lower() in [x.lower() for x in list(self.unit.values())] \
                    and result['BuildingName'] is None:
                if token.upper() in self.unit:
                    result['UnitType']=self.unit[token.upper()].upper()
                else:
                    result['UnitType'] = token.upper()
                result['UnitNumber'] = tokens[t + 1]
            elif token.upper() in self.level or token.lower() in [x.lower() for x in list(self.level.values())]:
                if token.upper() in self.level:
                    result['LevelType'] = self.level[token.upper()]
                else:
                    result['LevelType'] = token.upper()
                result['LevelNumber'] = tokens[t+1]
            elif result['UnitType'] is not None and result['LevelType'] is not None and token.isalpha() \
                    and result['BuildingName'] is None and result['StreetNumber1'] is None:
                result['BuildingName'] = token.upper()
                test = 1
            elif result['BuildingName'] is not None and token.isalpha()and result['StreetNumber1'] is None:
                result['BuildingName'] = result['BuildingName']+" "+token.upper()
                test =1
            elif hyphened_street_number and result['StreetNumber1'] is None:
                result['StreetNumber1'] = re.split(r'[\-]',token)[0]
                result['StreetNumber2'] = re.split(r'[\-]',token)[1]
                test =1
            elif t==0 and (token.isalnum() or token.isnumeric()):
                result['StreetNumber1'] = token
            elif result['StreetNumber1'] is not None and token.isalpha() and result['StreetName'] is None:
                result['StreetName'] = token.upper()
                test = 1
            elif result['StreetName'] is not None and token.isalpha() and result['StreetType'] is None \
                    and token.upper() not in self.street and token.lower() not in [x.lower() for x in list(self.street.values())]:
                result['StreetName'] = result['StreetName'] + " " + token.upper()
                test =1
            elif token.upper() in self.street or token.lower() in [x.lower() for x in list(self.street.values())] \
                and result['StreetNumber1'] is not None and result['StreetName'] is not None:
                if token.upper() in self.street:
                    result['StreetType'] = self.street[token.upper()].upper()
                else:
                    result['StreetType'] = token.upper()
                test = 1
            elif token.upper() in self.road_suffix or token.lower() in [x.lower() for x in list(self.road_suffix.values())]:
                if token.upper() in self.road_suffix:
                    result['StreetSuffix'] = self.road_suffix[token.upper()]
                else:
                    result['StreetSuffix'] = token.upper()
            elif result['StreetName'] is not None and token.isalpha() and result['LocalityName'] is None:
                result['LocalityName'] = token.upper()
                test = 1
            elif token.upper() in self.state or token.lower() in [x.lower() for x in list(self.state.values())]:
                if token.upper() in self.state:
                    result['StateTerritory'] = self.state[token.upper()].upper()
                else:
                    result['StateTerritory']= token.upper()
                test = 1
            else:
                result['Postcode'] =token
                test =1

        print(result)


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
    parser.parse("U Ab89NNN L B99N B113A-C78D saint John st N, GRIFFITH ACT 2603")
