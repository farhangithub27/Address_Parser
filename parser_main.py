
import json
from Address_Parser import parser

def main():
    address = "UNIT 6 LEVEL 2 COMPLEX HOUSE 201-200 CANBERRA AVENUE SOUTH west, Woden victoria 2603"
    parser_object = parser.AddressParser()
    response = parser_object.parse(address)
    print("1:"+str(json.loads(response)))
    print('\n')
    address = "1 BROAD PL KAMBAH ACT 2902"
    response = parser_object.parse(address)
    print("2:"+str(json.loads(response)))
    print('\n')
    address = "apt 5 G 45 John James hospital 54 vilo st w,Barton SA 2603"
    response = parser_object.parse(address)
    print("3:"+str(json.loads(response)))
    print('\n')
    address = "apt DD5D G 45 John James hospital 5-4 vilo rd w Acton nsw 2603"
    response = parser_object.parse(address)
    print("4:"+str(json.loads(response)))
    print('\n')
    address = "apt DD5D G 45 John James hospital 5-4d vilo rd w,Acton ACT 2603"
    response = parser_object.parse(address)
    print("5:"+str(json.loads(response)))
    print('\n')
    address = "apt DD5D G 45 John James hospital dv5-4dd vilo rd w,Acton ACT 2603"
    response = parser_object.parse(address)
    print("6:" + str(json.loads(response)))
    print('\n')
    address = "apt DD5D G 45dddd John James hospital DH5-4N vilo rd w,Acton ACT 2603"
    response = parser_object.parse(address)
    print("7:" + str(json.loads(response)))
    print('\n')
    address = "apt DD5d G 45D John James hospital DH5-4N vilo rd north west,Acton ACT 2603"
    response = parser_object.parse(address)
    print("8:" + str(json.loads(response)))
    print('\n')
    address = "DH5-4N vilo rd north west,watson ACT 2603"
    response = parser_object.parse(address)
    print("9:" + str(json.loads(response)))
    print('\n')
    address = "Dd5-4N vilo rd w,watson ACT 2603"
    response = parser_object.parse(address)
    print("10:" + str(json.loads(response)))
    print('\n')
    address = "vilo rd w,watson ACT 2603"
    response = parser_object.parse(address)
    print("11:" + str(json.loads(response)))
    print('\n')
    address = "U 4 vilo rd w,watson ACT 2603"
    response = parser_object.parse(address)
    print("12:" + str(json.loads(response)))
    print('\n')
    address = "U 5 4 vilo main highway south east,watson ACT 2603"
    response = parser_object.parse(address)
    print("13:" + str(json.loads(response)))
    print('\n')
    address = "U 5 FL 4 vilo main highway w,watson ACT 2603"
    response = parser_object.parse(address)
    print("14:" + str(json.loads(response)))
    print('\n')
    address = "FL DD4 COMPLEX HOUSE 6D vilo main highway w,watson ACT 2603"
    response = parser_object.parse(address)
    print("15:" + str(json.loads(response)))
    print('\n')
    address = "House DD4 COMPLEX HOUSE 6D vilo main st south,watson ACT 2603"
    response = parser_object.parse(address)
    print("16:" + str(json.loads(response)))
    print('\n')
    address = "House DD4 COMPLEX HOUSE 6D vilo main st south,acton tasmania  2603"
    response = parser_object.parse(address)
    print("17:" + str(json.loads(response)))
    print('\n')
    address = "House DD4 L 7Y COMPLEX HOUSE 6D vilo main st south east,watson victoria 2603"
    response = parser_object.parse(address)
    print("18:" + str(json.loads(response)))
    print('\n')
    address = "House DD4 6D-5 the vilo main st south east, deakin Australian Antarctic Territory 2603"
    response = parser_object.parse(address)
    print("19:" + str(json.loads(response)))
    print('\n')
    address = "House DD4 L 7Y COMPLEX HOUSE 6D-5 the vilo main st south,watson vic 2603"
    response = parser_object.parse(address)
    print("20:" + str(json.loads(response)))
    print('\n')
    address = "House DD4 L 7Y COMPLEX HOUSE 6D-5 the vilo main st south,watson south australia 2603"
    response = parser_object.parse(address)
    print("21:" + str(json.loads(response)))
    print('\n')



if __name__== "__main__":

    main()