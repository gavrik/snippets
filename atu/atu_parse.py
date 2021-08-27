import io
import xml.etree.ElementTree as ET
import html
import codecs
import time
import argparse
import pathlib
import sys

parser = argparse.ArgumentParser(description="Ukraine ATU XML to CSV parser")
parser.add_argument('--input', type=pathlib.Path, required=True, help='Input XML file path')
parser.add_argument('--output', type=pathlib.Path, required=True, help='Output CSV file path')

args = parser.parse_args()

START_TAG = '<RECORD>'
END_TAG = '</RECORD>'

def chunks(filename, buffer_size=300):
        with codecs.open(filename, 'r', 'cp1251') as fp:
            chunk = fp.read(buffer_size)
            while chunk:
                yield chunk
                chunk = fp.read(buffer_size)

def findSubstring(chunk, subString):
    return chunk.find(subString)

def parseXML(XmlStr):
    if len(XmlStr) == 0:
        return ''
    line = ""
    f = io.StringIO(XmlStr)
    tree = ET.parse(f)
    root = tree.getroot()
    for child in root:
        if child.text is not None and child.text != ' ':
            line = line + '"' + html.unescape(' '.join(child.text.split()))\
                                            .replace('"','\\"')\
                                            .replace('`',"'") + '"|'
        else:
            line = line + '"None"' + '|'
    return line[0:-1]

def removeBadLines(xml):
    return xml[findSubstring(xml, START_TAG):findSubstring(xml,END_TAG)+len(END_TAG)]

def main(inputPath, buffer_size):
    i = 0
    xml = ''

    try:
        wfp = open(str(args.output) + '_' + str(time.time()), 'w')
    except:
        print('Can''t open file for output')
        sys.exit(1)

    for chunk in chunks(inputPath, buffer_size):
        xml = xml + chunk
        index = findSubstring(xml,END_TAG)
        if index > 0:
            wfp.write(parseXML(removeBadLines(xml)))
            wfp.write('\n')
            xml = xml[findSubstring(xml,END_TAG)+len(END_TAG):len(xml)]
        i = i + 1
    print('Result File: ', wfp)
    

if __name__ == "__main__":
    XmlStr = '''
    <DATA FORMAT_VERSION="1.0">g="windows-1251"?><RECORD>
        <OBL_NAME>Автономна Республіка Крим</OBL_NAME>
        <REGION_NAME></REGION_NAME>
        <CITY_NAME>м.Сімферополь</CITY_NAME>
        <CITY_REGION_NAME></CITY_REGION_NAME>
        <STREET_NAME>вул.Генічеська</STREET_NAME>
    </RECORD>
    '''

    print(args.input)
    print(args.output)

    if not args.input.exists:
        print('Input Path does not exists')
        sys.exit(1)

    #print(parseXML(removeBadLines(XmlStr)))

    main(str(args.input), 9)
