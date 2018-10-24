import xml.etree.ElementTree as ET
import os
data = ET.Element('results')
for directory in next(os.walk('towns'))[1]:
    town_element = ET.SubElement(data, directory)
    print("creating xml element for: " + directory)
    for town in os.listdir('towns/' + directory):
        print('towns/' + directory + "/" + town)
        file = ET.parse('towns/' + directory + "/" + town).getroot()
        town_element.append(file)
print (ET.tostring(data))
mydata = ET.ElementTree(data)
mydata.write("results.xml")
