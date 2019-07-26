# Sample output

Address Tokens: ['UNIT', '6', 'LEVEL', '2', 'PSMA', 'HOUSE', '113-115', 'CANBERRA', 'AVENUE', 'SOUTH', 'west', 'GRIFFITH', 'victoria', '2603']
1:{'UnitType': 'UNIT', 'UnitNumber': '6', 'LevelType': 'LEVEL', 'LevelNumber': '2', 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '113', 'StreetNumber2': '115', 'StreetName': 'CANBERRA', 'StreetType': 'AVENUE', 'StreetSuffix': 'SOUTH WEST', 'LocalityName': 'GRIFFITH', 'StateTerritory': 'VIC', 'Postcode': '2603'}


Address Tokens: ['1', 'BROAD', 'PL', 'KAMBAH', 'ACT', '2902']
2:{'UnitType': None, 'UnitNumber': None, 'LevelType': None, 'LevelNumber': None, 'BuildingName': None, 'StreetNumber1': '1', 'StreetNumber2': None, 'StreetName': 'BROAD', 'StreetType': 'PLACE', 'StreetSuffix': None, 'LocalityName': 'KAMBAH', 'StateTerritory': 'ACT', 'Postcode': '2902'}


Address Tokens: ['apt', '5', 'G', '45', 'John', 'James', 'hospital', '54', 'vilo', 'st', 'w', 'Barton', 'SA', '2603']
3:{'UnitType': 'APARTMENT', 'UnitNumber': '5', 'LevelType': 'Ground', 'LevelNumber': '45', 'BuildingName': 'JOHN JAMES HOSPITAL', 'StreetNumber1': '54', 'StreetNumber2': None, 'StreetName': 'VILO', 'StreetType': 'STREET', 'StreetSuffix': 'WEST', 'LocalityName': 'BARTON', 'StateTerritory': 'SA', 'Postcode': '2603'}


Address Tokens: ['apt', 'DD5D', 'G', '45', 'John', 'James', 'hospital', '5-4', 'vilo', 'rd', 'w', 'Acton', 'nsw', '2603']
4:{'UnitType': 'APARTMENT', 'UnitNumber': 'DD5D', 'LevelType': 'Ground', 'LevelNumber': '45', 'BuildingName': 'JOHN JAMES HOSPITAL', 'StreetNumber1': '5', 'StreetNumber2': '4', 'StreetName': 'VILO', 'StreetType': 'ROAD', 'StreetSuffix': 'WEST', 'LocalityName': 'ACTON', 'StateTerritory': 'NSW', 'Postcode': '2603'}


Address Tokens: ['apt', 'DD5D', 'G', '45', 'John', 'James', 'hospital', '5-4d', 'vilo', 'rd', 'w', 'Acton', 'ACT', '2603']
5:{'parse_error': 'Cannot be parsed. Street Number is not in required format.'}


Address Tokens: ['apt', 'DD5D', 'G', '45', 'John', 'James', 'hospital', 'dv5-4dd', 'vilo', 'rd', 'w', 'Acton', 'ACT', '2603']
6:{'parse_error': 'Cannot be parsed. Street Number is not in required format.'}


Address Tokens: ['apt', 'DD5D', 'G', '45dddd', 'John', 'James', 'hospital', 'DH5-4N', 'vilo', 'rd', 'w', 'Acton', 'ACT', '2603']
7:{'parse_error': 'Cannot be parsed. LevelNumber is missing in required format.'}


Address Tokens: ['apt', 'DD5d', 'G', '45D', 'John', 'James', 'hospital', 'DH5-4N', 'vilo', 'rd', 'north', 'west', 'Acton', 'ACT', '2603']
8:{'parse_error': 'Cannot be parsed. UnitNumber is missing in required format.'}


Address Tokens: ['DH5-4N', 'vilo', 'rd', 'north', 'west', 'watson', 'ACT', '2603']
9:{'UnitType': None, 'UnitNumber': None, 'LevelType': None, 'LevelNumber': None, 'BuildingName': None, 'StreetNumber1': 'DH5', 'StreetNumber2': '4N', 'StreetName': 'VILO', 'StreetType': 'ROAD', 'StreetSuffix': 'NORTH WEST', 'LocalityName': 'WATSON', 'StateTerritory': 'ACT', 'Postcode': '2603'}


Address Tokens: ['Dd5-4N', 'vilo', 'rd', 'w', 'watson', 'ACT', '2603']
10:{'parse_error': 'Cannot be parsed. Street Number is not in required format.'}


Address Tokens: ['vilo', 'rd', 'w', 'watson', 'ACT', '2603']
11:{'parse_error': 'Cannot be parsed. Please check Street Number, Street Name, Locality Name and Sate Territory'}


Address Tokens: ['U', '4', 'vilo', 'rd', 'w', 'watson', 'ACT', '2603']
12:{'parse_error': 'Cannot be parsed. Please check Street Number, Street Name, Locality Name and Sate Territory'}


Address Tokens: ['U', '5', '4', 'vilo', 'main', 'highway', 'south', 'east', 'watson', 'ACT', '2603']
13:{'UnitType': 'UNIT', 'UnitNumber': '5', 'LevelType': None, 'LevelNumber': None, 'BuildingName': None, 'StreetNumber1': '4', 'StreetNumber2': None, 'StreetName': 'VILO MAIN', 'StreetType': 'HIGHWAY', 'StreetSuffix': 'SOUTH EAST', 'LocalityName': 'WATSON', 'StateTerritory': 'ACT', 'Postcode': '2603'}


Address Tokens: ['U', '5', 'FL', '4', 'vilo', 'main', 'highway', 'w', 'watson', 'ACT', '2603']
14:{'parse_error': 'Cannot be parsed. Please check Street Number, Street Name, Locality Name and Sate Territory'}


Address Tokens: ['FL', 'DD4', 'PSMA', 'HOUSE', '6D', 'vilo', 'main', 'highway', 'w', 'watson', 'ACT', '2603']
15:{'UnitType': None, 'UnitNumber': None, 'LevelType': 'Floor', 'LevelNumber': 'DD4', 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '6D', 'StreetNumber2': None, 'StreetName': 'VILO MAIN', 'StreetType': 'HIGHWAY', 'StreetSuffix': 'WEST', 'LocalityName': 'WATSON', 'StateTerritory': 'ACT', 'Postcode': '2603'}


Address Tokens: ['House', 'DD4', 'PSMA', 'HOUSE', '6D', 'vilo', 'main', 'st', 'south', 'watson', 'ACT', '2603']
16:{'UnitType': 'HOUSE', 'UnitNumber': 'DD4', 'LevelType': None, 'LevelNumber': None, 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '6D', 'StreetNumber2': None, 'StreetName': 'VILO MAIN', 'StreetType': 'STREET', 'StreetSuffix': 'SOUTH', 'LocalityName': 'WATSON', 'StateTerritory': 'ACT', 'Postcode': '2603'}


Address Tokens: ['House', 'DD4', 'PSMA', 'HOUSE', '6D', 'vilo', 'main', 'st', 'south', 'acton', 'tasmania', '2603']
17:{'UnitType': 'HOUSE', 'UnitNumber': 'DD4', 'LevelType': None, 'LevelNumber': None, 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '6D', 'StreetNumber2': None, 'StreetName': 'VILO MAIN', 'StreetType': 'STREET', 'StreetSuffix': 'SOUTH', 'LocalityName': 'ACTON', 'StateTerritory': 'TAS', 'Postcode': '2603'}


Address Tokens: ['House', 'DD4', 'L', '7Y', 'PSMA', 'HOUSE', '6D', 'vilo', 'main', 'st', 'south', 'east', 'watson', 'victoria', '2603']
18:{'UnitType': 'HOUSE', 'UnitNumber': 'DD4', 'LevelType': 'Level', 'LevelNumber': '7Y', 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '6D', 'StreetNumber2': None, 'StreetName': 'VILO MAIN', 'StreetType': 'STREET', 'StreetSuffix': 'SOUTH EAST', 'LocalityName': 'WATSON', 'StateTerritory': 'VIC', 'Postcode': '2603'}


Address Tokens: ['House', 'DD4', '6D-5', 'the', 'vilo', 'main', 'st', 'south', 'east', 'deakin', 'Australian', 'Antarctic', 'Territory', '2603']
19:{'UnitType': 'HOUSE', 'UnitNumber': 'DD4', 'LevelType': None, 'LevelNumber': None, 'BuildingName': None, 'StreetNumber1': '6D', 'StreetNumber2': '5', 'StreetName': 'THE VILO MAIN STREET SOUTH EAST', 'StreetType': None, 'StreetSuffix': None, 'LocalityName': 'DEAKIN', 'StateTerritory': 'AAT', 'Postcode': '2603'}


Address Tokens: ['House', 'DD4', 'L', '7Y', 'PSMA', 'HOUSE', '6D-5', 'the', 'vilo', 'main', 'st', 'south', 'watson', 'vic', '2603']
20:{'UnitType': 'HOUSE', 'UnitNumber': 'DD4', 'LevelType': 'Level', 'LevelNumber': '7Y', 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '6D', 'StreetNumber2': '5', 'StreetName': 'THE VILO MAIN STREET SOUTH', 'StreetType': None, 'StreetSuffix': None, 'LocalityName': 'WATSON', 'StateTerritory': 'VIC', 'Postcode': '2603'}


Address Tokens: ['House', 'DD4', 'L', '7Y', 'PSMA', 'HOUSE', '6D-5', 'the', 'vilo', 'main', 'st', 'south', 'watson', 'south', 'australia', '2603']
21:{'UnitType': 'HOUSE', 'UnitNumber': 'DD4', 'LevelType': 'Level', 'LevelNumber': '7Y', 'BuildingName': 'PSMA HOUSE', 'StreetNumber1': '6D', 'StreetNumber2': '5', 'StreetName': 'THE VILO MAIN STREET SOUTH', 'StreetType': None, 'StreetSuffix': None, 'LocalityName': 'WATSON', 'StateTerritory': 'SA', 'Postcode': '2603'}