import json
from collections import OrderedDict
import jsonref
import sys 
import unicodecsv

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

def generate_table(path):    
    table_schema = []
    for name, defs in path.iteritems():
        field = {}
    
        if name in data['required']:
            required = True
        else:
            required = False
    
        if 'array' in defs['type'] or 'object' in defs['type']:
            try: # If we have rollUp properties, then include these in the summary table 
                for item in defs['rollUp']:
                    subfield = {}
                    subdefs = defs['items']['properties'][item]
                
                    try:
                        if item in defs['items'].get('required',False):
                            sub_required = True
                        else:
                            sub_required = False
                    except Exception as a:
                        sub_required = False             
                
                    field_info = get_field_info(subdefs)

                    subfield.update({"name":name + "[]/"+ item + field_info['suffix'],'title':defs['title'] + ":" + subdefs['title'],'description':subdefs.get('description','-'),"type":field_info["type"],"format":field_info["format"],"required":sub_required})
                    table_schema.append(subfield)

            except Exception as a:
                if defs['items'] == 'string':
                    field.update({"name":name,'title':defs['title'],'description':defs.get('description','-'),'type':'array','format':'string',"required":required})
        else:
            field_info = get_field_info(defs)
            field.update({'name':name,'title':defs['title'],'description':defs.get('description','-'),"type":field_info["type"],"format":field_info["format"],"required":required})
            if field_info['validation']:
                field.update({"allowed_values":field_info['validation']})
    
            table_schema.append(field)

    return table_schema

print "Writing updated schema"

for key in data['definitions']:
    try:
        table = generate_table(data['definitions'][key]['properties'])
        with open('../documentation/src/tabledefs/'+key+'.csv', 'wb') as output_file:
            dict_writer = unicodecsv.DictWriter(output_file,  fieldnames=['title','name','description', 'type', 'format', 'allowed_values', 'required'])
            dict_writer.writeheader()
            dict_writer.writerows(table)
        with open('../documentation/src/tabledefs/'+key+'.json', 'w') as outfile:
            json.dump({"fields":table}, outfile,indent=True)
    except KeyError:
        pass
    
table = generate_table(data['properties'])

with open('../documentation/src/tabledefs/grant.json', 'w') as outfile:
    json.dump({"fields":table}, outfile,indent=True)

with open('../documentation/src/tabledefs/grant.csv', 'wb') as output_file:
    dict_writer = unicodecsv.DictWriter(output_file,  fieldnames=['title','name','description', 'type', 'format', 'allowed_values', 'required'])
    dict_writer.writeheader()
    dict_writer.writerows(table)
        


