# Code Challenge

This stage of the interview requires you to solve ONE of the following challenges. These small challenges are designed to enable us to assess a sample of your software development skills (e.g. documentation, software design, coding proficiency, version control usage).

Please read the instructions carefully. We will review only ONE solution.

## Considerations

- You are free to make reasonable assumptions or design decisions to complete the challenge. Please document all assumptions, decisions and rationale. 
- We request that you use Python. This is the primary programming language we use. 
- We expect to see professional-quality code (e.g. testable, maintainable, extensible). 
- We encourage you to ONLY implement the requested features. 
- We encourage you to include evidence that your solution is correct (e.g. correctly handles the sample inputs). 
- We will review your version control commit history to assess your usage of version control. 
- We commit to a fair interview process for everyone. Please help us by not sharing or publishing these challenges. 

## Submission requirements:

1. We must be able to build and run your source code. Please include detailed build and run instructions.
2. Please commit all required source code and supporting documentation (including a brief explanation of your design and assumptions).
3. The algorithms that deliver the required functionality must be your code; not an external library.  
   *Note*: You may use external libraries to test your solution or to implement the supporting infrastructure (e.g. flask, graphql, pytest).  
4. Please do not email your submission. Our system blocks certain file types for security purposes, and we want to avoid delays to your application.  
5. Please submit your solution to ONE of the following options:  

# OPTION ONE: 
PSMA wishes to receive feedback about addresses from our flagship address product: the Geocoded National Address File (or G-NAF). However, customers have been sending us information using an address string instead of our identifiers.

To make use of this feedback, we need to build an address parser that separates an address string into its constituent address fields. Using bolding of the example address: UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603 (not a real address): 

Field|example|vocabulary|Mandatory?
-----|-------|----------|----------
UnitType|**UNIT** 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603|UNIT, APARTMENT, etc., full list [here](https://meteor.aihw.gov.au/content/index.phtml/itemId/429004)|No  
UnitNumber|UNIT **6** LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603| |No. Only present when a UnitType is  
LevelType|UNIT 6 **LEVEL** 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603|LEVEL, FLOOR, etc., full list [here](https://meteor.aihw.gov.au/content/index.phtml/itemId/429016/meteorItemView/long)|No  
LevelNumber|UNIT 6 LEVEL **2** PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603| |No. Only present when LevelType is  
BuildingName|UNIT 6 LEVEL 2 **PSMA HOUSE** 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603| |No  
StreetNumber1|UNIT 6 LEVEL 2 PSMA HOUSE **113**-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603| |Yes  
StreetNumber2|UNIT 6 LEVEL 2 PSMA HOUSE 113-**115** CANBERRA AVENUE SOUTH, GRIFFITH ACT 2603| |No. Only present when StreetNumber1 is  
StreetName|UNIT 6 LEVEL 2 PSMA HOUSE 113-115 **CANBERRA** AVENUE SOUTH, GRIFFITH ACT 2603| |Yes  
StreetType|UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA **AVENUE** SOUTH, GRIFFITH ACT 2603|AVENUE, STREET, etc., full list [here](https://meteor.aihw.gov.au/content/index.phtml/itemId/429840)|No  
StreetSuffix|UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE **SOUTH**, GRIFFITH ACT 2603|SOUTH, CENTRAL, etc., full list [here](https://meteor.aihw.gov.au/content/index.phtml/itemId/429869)|No  
LocalityName|UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, **GRIFFITH** ACT 2603| |Yes  
StateTerritory|UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH **ACT** 2603|ACT, NSW, etc., full list [here](https://meteor.aihw.gov.au/content/index.phtml/itemId/430134)|Yes  
Postcode|UNIT 6 LEVEL 2 PSMA HOUSE 113-115 CANBERRA AVENUE SOUTH, GRIFFITH ACT **2603**| |No  

*Note:*

- UnitNumber, LevelNumber, StreetNumber1 and StreetNumber2 can all contain prefixes and suffixes of one to two uppercase letters. For example A21B.  
- UnitType, LevelType, StreetType, StreetSuffix, and StateTerritory can all either be abbreviated or expanded. The output should be expanded for all of them, except StateTerritory which should be abbreviated. 
- When THE is used in the position of StreetName, then the remaining street components (i.e., StreetType and StreetSuffix) should be shifted into the StreetName field: i.e., 1 THE CRESCENT SOUTH, KAMBAH ACT 2902 should result in StreetName: THE CRESCENT SOUTH, StreetType: None, StreetSuffix: None 
 
**YOUR TASK:** Your task is to write the parser. 

**Input Format:**  
A single line of input containing the string S.  
Note: The string S can contain upper and lower case characters, numbers, commas, spaces, and hyphens.  

**Output Format:**  
A dictionary containing keys for each of the address fields described above.  
If the string cannot be parsed, print “Cannot be parsed.”  
  
**Sample Input:**  
1 BROAD PL KAMBAH ACT 2902  

**Expected Output:**  
{ “UnitType”: None, “UnitNumber”: None, “LevelType”: None, “LevelNumber”: None, “BuildingName”: None, ”StreetNumber1”: “1”, “StreetNumber2”: None, “StreetName”: “BROAD”, “StreetType”: “PLACE”, “StreetSuffix”: None, “LocalityName”: “KAMBAH”, “StateTerritory”: “ACT”, “Postcode”: “2902” } 
 
# OPTION TWO: 
We receive movie reviews from a variety of critics. In return our suppliers can request from us a movie review from any critic (including their own). Currently this is a manual process. We would like to automate this by serving the data via an API. 

The trouble is we don’t know how to build a good API. For example: What the interface ought to be. What protocol to use (SOAP? REST? GraphQL?). How to store the data so the API can serve it. 

**YOUR TASK:** Your task is to create a suitable system that our suppliers can easily query over the internet to get movie reviews. 

**Expected Inputs:**

- Movie Name 
- Provider 

**Expected Output:**

- The movie review. (At the moment we only get movie ratings.) 

**Sample Data:** 

movie|provider|rating
-----|--------|------ 
RAMBO|ROTTEN TOMATOES|8.80 
RAMBO|IMDB|7.70 
RAMBO|METACRITIC|6.10 
RAMBO II|IMDB|6.50 
RAMBO II|ROTTEN TOMATOES|3.80 
RAMBO II|METACRITIC|4.70 
RAMBO III|IMDB|5.80 
RAMBO III|ROTTEN TOMATOES|3.90 
LOVE ACTUALLY|IMDB|7.60 
LOVE ACTUALLY|ROTTEN TOMATOES|6.30 
LOVE ACTUALLY|METACRITIC|5.50 
LOVE IS ALL YOU NEED|IMDB|6.50 
LOVE IS ALL YOU NEED|ROTTEN TOMATOES|7.50 
JAWS|IMDB|8.00 
JAWS|ROTTEN TOMATOES|9.80 
WHAT DREAMS MAY COME|IMDB|7.00 
WHAT DREAMS MAY COME|ROTTEN TOMATOES|5.40 
KILLING ME SOFTLY|IMDB|5.50 
THE WHOLE NINE YARDS|ROTTEN TOMATOES|4.50 
THE SHINING|IMDB|8.40 
THE SHINING|ROTTEN TOMATOES|8.70 
THE SIMPSONS|METACRITIC|8.00 
AMELIE|ROTTEN TOMATOES|8.90 
AMELIE|METACRITIC|6.90 
CHOCOLAT|IMDB|7.30 
CHOCOLAT|METACRITIC|6.40 
 
**Sample Request:**  
GET movie=Rambo&provider=IMDB 

**Expected Output:**  
7.7
