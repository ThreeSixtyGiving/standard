import json
from collections import OrderedDict
import jsonref
import sys 

table_schema = []

with open("../schema/360-giving-schema.json") as schema_file:
    data = jsonref.load(schema_file,object_pairs_hook=OrderedDict)

def get_field_info(field_def):
    validation = ''
    if 'string' in field_def['type']:
        suffix = ''
        field_format = ''
        if 'date-time' in field_def.get('format',''):
            field_type = 'datetime'
        else:
            field_type = 'string'

        if field_def.get('enum',False):
            validation = ",".join(field_def.get('enum'))
        
    elif 'number' in field_def['type']:
        suffix = ':number'
        field_type = 'number'
        field_format = ''
    elif 'integer' in field_def['type']:
        suffix = ':integer'
        field_type = 'integer'
        field_format = ''
    elif 'boolean' in field_def['type']:
        suffix = ':boolean'
        field_type = 'boolean'
        field_format = ''
    
    return {"suffix":suffix,"type":field_type,"format":field_format,"validation":validation}
    
    
for name, defs in data['properties'].iteritems():
    field = {}
    
    if 'array' in defs['type'] or 'object' in defs['type']:
        try: # If we have rollUp properties, then include these in the summary table 
            for item in defs['rollUp']:
                subfield = {}
                subdefs = defs['items']['properties'][item]
                field_info = get_field_info(subdefs)
                subfield.update({"name":name + "[]/"+ item + field_info['suffix'],'title':defs['title'] + ":" + subdefs['title'],'description':subdefs.get('description','-'),"type":field_info["type"],"format":field_info["format"]})
                table_schema.append(subfield)
        except Exception as a:
            if defs['items'] == 'string':
                field.update({"name":name,'title':defs['title'],'description':defs.get('description','-'),'type':'array','format':'string'})
    else:
        field_info = get_field_info(defs)
        field.update({'name':name,'title':defs['title'],'description':defs.get('description','-'),"type":field_info["type"],"format":field_info["format"]})
        if field_info['validation']:
            field.update({"allowed_values":field_info['validation']})
    
        table_schema.append(field)

print "Writing updated schema"

with open('../schema/summary-table/360-summary-table-schema.json', 'w') as outfile:
    json.dump({"fields":table_schema}, outfile,indent=True)
    

