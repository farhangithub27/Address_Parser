# Assumptions


- No spelling mistake while entering fields except Building Name, Street Name and Suburb(LocalityName).
- Each field is provided in the same order as provided in examples below,
  + UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603
  + 1 BROAD PL KAMBAH ACT 2902
- Parsed address will be disregarded if any of the mandatory fields are missing.
  + StreetNumber1
  + StreetName
  + LocalityName
  + StateTerritory
- Address string will not contain special characters other than mentioned in input format.
- Unit can be abbreviated as U followed by unit number in allowed formats.
- If UnitTpe is given then LevelType must be given as well and vice vera. Only exception is BuildingName that may or may not be given.
- If UnitType and LevelType are given then corresponding numbers are provided for sure. 
- If building name is not given then space or allowed characters will be present between level number and street number.