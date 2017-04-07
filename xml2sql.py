import xml.parsers.expat
from pprint import pprint
from subprocess import check_output
from tqdm import tqdm
from time import time

start = time()
tag = 'posts'
xmlFile = '../posts-head.xml'
xmlFile = '../Posts.xml'
sqlFile = tag + '.sql'
lines = int(check_output(['countlines/countlines.sh', xmlFile, "10000"]))
parsed = 0
progress_bar = tqdm(total=lines,
                    unit=tag,
                    unit_scale=True)

sqlHeader = "CREATE TABLE {table} ({fields});"
sqlFields = [
    'AcceptedAnswerId INT UNSIGNED',
    'AnswerCount INT UNSIGNED',
    'Body TEXT',
    'ClosedDate DATETIME',
    'CommentCount INT UNSIGNED',
    'CommunityOwnedDate DATETIME',
    'CreationDate DATETIME',
    'FavoriteCount INT UNSIGNED',
    'Id INT UNSIGNED',
    'LastActivityDate DATETIME',
    'LastEditDate DATETIME',
    'LastEditorDisplayName VARCHAR(255)',
    'LastEditorUserId INT UNSIGNED',
    'OwnerDisplayName VARCHAR(255)',
    'OwnerUserId INT UNSIGNED',
    'ParentId INT UNSIGNED',
    'PostTypeId INT UNSIGNED',
    'Score INT UNSIGNED',
    'Tags VARCHAR(255)',
    'Title VARCHAR(255)',
    'ViewCount INT UNSIGNED'
    'PRIMARY KEY (Id)']

sql = sqlHeader.format(**{
                        'table': tag,
                        'fields': ',\n'.join(sqlFields),
                    })

print(sql); exit()

def startElement(name, attrs):
    # ppr'INT UNSIGNED'({name: attrs})
    global sqlFields
    if name == 'row':
        newFields = set(attrs.keys())
        if not newFields.issubset(sqlFields):
            sqlFields.update(newFields)
            pprint(sqlFields)
    elif name == tag:
        pass


    pass

def endElement(name):
    global progress_bar, parsed
    parsed += 1
    # ppr'INT UNSIGNED'(['End element:', name])
    progress_bar.update(1) # +1

def characterData(data):
    pprint({'Character data:': data})

parser = xml.parsers.expat.ParserCreate()
parser.StartElementHandler = startElement
parser.EndElementHandler = endElement
# parser.CharacterDataHandler = character_data
parser.buffer_text = True

with open(xmlFile, 'rb') as file:
    parser.ParseFile(file)
