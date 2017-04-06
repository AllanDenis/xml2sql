import xml.parsers.expat
from sys import stdout
from pprint import pprint

xmlFile = '../Posts.xml'
xmlFile = '../posts-head.xml'
# tag = 'posts'

i = 0

def start_element(name, attrs):
    pprint(['Start element:', name, attrs])
    pass

def end_element(name):
    global i
    i += 1
    pprint(['End element:', name])
    # stdout.write('.')
    # stdout.write("%.2f%%\r" % (1e2 * (i / 50e6)))

def character_data(data):
    pprint(['Character data:', data])

parser = xml.parsers.expat.ParserCreate()
parser.StartElementHandler = start_element
parser.EndElementHandler = end_element
parser.buffer_text = True
parser.buffer_size = 2 ** 16
# parser.CharacterDataHandler = character_data

with open(xmlFile, 'rb') as file:
    parser.ParseFile(file)
