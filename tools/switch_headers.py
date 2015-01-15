## Simple utility to replace names with titles, or titles with names, in a CSV file - based on a JSON Table schema
import json
import csv
from collections import OrderedDict

def detect_header():
    pass
    
def switch_to_title():
    pass
    
def switch_to_name(header,schema):
    print schema
    for col in header:
        print col
        ## https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
        print (item for item in schema['fields'] if item["name"] == col).next()
        
    pass



schemapath = "../schema/summary-table/360-summary-table-schema.json"
csvpath = "../demo.csv"
skip = 1

with open(schemapath) as schema_file:
    schema = json.load(schema_file,object_pairs_hook=OrderedDict)

with open(csvpath, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # Skip rows if required
    for _ in xrange(skip):
        csvreader.next()

    header = csvreader.next()
    switch_to_name(header,schema)
