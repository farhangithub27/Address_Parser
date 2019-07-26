
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

        print("Address Tokens:" , tokens)
        # \s* matches zero or more of spaces (\s) after , and \s inside square brackets
        # or
        # tokens = address.split()# Only works with one argument. Default is space (\s)
        for t in range(0, len(tokens)):
            token = tokens[t]
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
                if hyphened_street_number or token.isalpha() or not re.fullmatch(r'[^a-z]{0,2}\d+[^a-z]{0,2}', token):
                    return json.dumps({"parse_error": "Cannot be parsed. LevelNumber is missing in required format."})
                    #print("Cannot be parsed. LevelNumber is missing in required format.")
                    #break
                else:
                    result['LevelNumber'] = token

            # Finding Street Number
            elif hyphened_street_number and result['StreetNumber1'] is None:
                StreetNumber1 = re.split(r'[\-]',token)[0]
                StreetNumber2 = re.split(r'[\-]',token)[1]
                if re.fullmatch(r'[^a-z]{0,2}\d+[^a-z]{0,2}', StreetNumber1) and re.fullmatch(r'[^a-z]{0,2}\d+[^a-z]{0,2}', StreetNumber2):
                    result['StreetNumber1'] = re.split(r'[\-]',token)[0]
                    result['StreetNumber2'] = re.split(r'[\-]',token)[1]
                else:
                    return json.dumps({"parse_error": "Cannot be parsed. Street Number is not in required format."})
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
            elif token.upper() in self.road_suffix or token.lower() in [x.lower() for x in list(self.road_suffix.values())]\
                    and tokens[t+2]!='south':
                #print(token + "suf")
                if token.upper() in self.road_suffix:
                    result['StreetSuffix'] = self.road_suffix[token.upper()].upper()
                if  result['StreetSuffix'] is None and token.lower() in [x.lower() for x in list(self.road_suffix.values())]: #\
                        #and (tokens[t+1] in self.road_suffix
                        #or tokens[t+1].lower() in [x.lower() for x in list(self.road_suffix.values())]):# \
                        #and (token=='EAST' or token=='WEST'):
                    result['StreetSuffix'] = token.upper()
                if  result['StreetSuffix'] is not None and token.lower() in [x.lower() for x in list(self.road_suffix.values())] \
                        and (tokens[t+1] not in self.road_suffix or tokens[t+1].lower() not in [x.lower() for x in list(self.road_suffix.values())]) \
                        and (token.upper()=='EAST' or token.upper()=='WEST'):
                    result['StreetSuffix'] = result['StreetSuffix']+" "+token.upper()

            # Finding Sate Territory
            elif token.upper() in self.state or token.lower() in [x.lower() for x in list(self.state.values())] \
                    or list(filter(re.compile(r"\b%s\b" %token.lower()).search,[x.lower() for x in self.state.values()])) \
                    and tokens[t+1].lower() not in [x.lower() for x in list(self.road_suffix.values())]:
                #print(token+"tuff")
                if token.upper() in self.state:
                    result['StateTerritory'] = token.upper()
                elif list(filter(re.compile(r"\b%s\b" %token.lower()).search,[x.lower() for x in self.state.values()])) \
                        and result['StateTerritory'] is None: ##and [key for key,value in self.state.items() if value.lower() != token.lower()][0] \
                    result['StateTerritory'] = token.upper()
                elif list(filter(re.compile(r"\b%s\b" %token.lower()).search,[x.lower() for x in self.state.values()])) \
                        and result['StateTerritory'] is not None:# and [key for key,value in self.state.items() if value.lower() != token.lower()][0]:
                    result['StateTerritory'] = result['StateTerritory']+" "+token.upper()

                else:
                    result['StateTerritory'] = [key for key,value in self.state.items() if value.lower() == token.lower()][0]


            # Finding Building Name
            elif token.isalpha() and result['BuildingName'] is None and result['StreetNumber1'] is None:
                result['BuildingName'] = token.upper()

            elif result['BuildingName'] is not None and token.isalpha()and result['StreetNumber1'] is None:
                result['BuildingName'] = result['BuildingName']+" "+token.upper()

            # Finding Street Name
            elif result['StreetNumber1'] is not None and token.isalpha() and result['StreetName'] is None \
                    and token.upper() not in self.street and token.lower() not in [x.lower() for x in list(self.street.values())] \
                    and token.upper() not in self.road_suffix and token.lower() not in [x.lower() for x in list(self.road_suffix.values())] \
                    and token.upper() not in self.state and tokens[t+1].upper() not in self.state \
                    and token.lower() not in [x.lower() for x in list(self.state.values())] \
                    and tokens[t+1].lower() not in [x.lower() for x in list(self.state.values())]:
                result['StreetName'] = token.upper()

            elif result['StreetName'] is not None and token.isalpha() and result['StreetType'] is None \
                    and token.upper() not in self.street and token.lower() not in [x.lower() for x in list(self.street.values())] \
                    and token.upper() not in self.road_suffix and token.lower() not in [x.lower() for x in list(self.road_suffix.values())] \
                    and token.upper() not in self.state and tokens[t+1].upper() not in self.state \
                    and token.lower() not in [x.lower() for x in list(self.state.values())] \
                    and tokens[t+1].lower() not in [x.lower() for x in list(self.state.values())]:
                result['StreetName'] = result['StreetName'] + " " + token.upper()

            # Finding Suburb (Locality Name)
            elif token.isalpha() and result['LocalityName'] is None and (tokens[t+1].upper() in self.state
                    or tokens[t+1].lower() in [x.lower() for x in list(self.state.values())]
                    or [key for key,value in self.state.items() if value.lower() != tokens[t+1].lower()][0]
                    or not list(filter(re.compile(r"\b%s\b" %token.lower()).search,[x.lower() for x in self.state.values()]))):
                result['LocalityName'] = token.upper()


            else:
                if token.isnumeric():
                    result['Postcode'] = token

        if result['StreetNumber1'] is None or result['StreetName'] is None or result['LocalityName'] is None \
            or result['StateTerritory'] is None:
            return json.dumps({"parse_error": "Cannot be parsed. Please check Street Number, Street Name, Locality Name and Sate Territory"})
            #print ("Cannot be parsed. Please check Street Number, Street Name and Locality Name and State Territory")
            #break

        else:

            if re.search(r'(?:^|\W)THE(?:$|\W)',result['StreetName']):
                #print("The found")
                if result['StreetName'] is not None and result['StreetType'] is not None and result['StreetSuffix'] is not None:
                    result['StreetName'] = result['StreetName'] + " "+ result['StreetType'] +" "+ result['StreetSuffix']
                    result['StreetType'] = None
                    result['StreetSuffix'] = None
            if result['StateTerritory'].lower() in [x.lower() for x in list(self.state.values())]:
                result['StateTerritory'] = [key for key, value in self.state.items() if value.lower() == result['StateTerritory'].lower()][0]

            #print(result)
            return json.dumps(result)



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


#if __name__== "__main__":
#    parser = AddressParser()
#    parser.parse("House DD4 L 7Y PSMA HOUSE 6D-5 the vilo main st south,watson south australia 2603")
