import xml.etree.ElementTree as ET
import glob


raw_text = []
xmls = glob.glob("text/*.xml")

for xml in xmls:
    tree = ET.parse('text/0003.xml')
    root = tree.getroot()
    section = root.find("body/section")
    for paragraph in section.findall('p'):
        raw_text.append(paragraph.text)


with open("corpus.txt", "w") as f:
    for line in raw_text:
        f.write(line+"\n")
