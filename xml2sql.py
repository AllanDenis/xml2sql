import xml.parsers.expat
import time
from sys import stdout
from pprint import pprint
from subprocess import check_output
from tqdm import tqdm

xmlFile = '../posts-head.xml'
xmlFile = '../Posts.xml'
# tag = 'posts'
lines = int(check_output(['countlines/countlines.sh', xmlFile, "10000"]))
progress = tqdm(total=lines)
progress.unit_scale = True

parsed = 0

def start_element(name, attrs):
    # pprint({name: attrs})
    pass

def end_element(name):
    global progress
    # pprint(['End element:', name])
    progress.update(1) # +1

def character_data(data):
    pprint({'Character data:': data})

parser = xml.parsers.expat.ParserCreate()
parser.StartElementHandler = start_element
parser.EndElementHandler = end_element
# parser.CharacterDataHandler = character_data
parser.buffer_text = True

with open(xmlFile, 'rb') as file:
    parser.ParseFile(file)
