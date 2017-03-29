import re
import os
import csv
import json

def deep_access(x,keylist):
     val = x
     for key in keylist:
         val = val[key]
     return val

def cleans(string):
    return string.replace("\n"," ")

for file in os.listdir("../documentation/src/"):
    if file.endswith(".md"):
        with open("../documentation/src/" + file, 'r',encoding='utf-8') as f:
            string = str(f.read())
            for match in re.finditer("{{([a-zA-z\.]+)([|]*)([a-zA-z,]*)}}", string, flags=0):
                # If we are dealing with a CSV file, embed the table
                if ".csv" in match.group(1):
                    table = ""
                    if(match.group(3)):
                        cols = match.group(3).split(",")
                    else:
                        cols = ['Title','Name','Description','Type','Format','Required']
                    try:
                        with open("../documentation/src/tabledefs/"+match.group(1),"r",encoding='utf-8') as csvfile:
                            reader = csv.DictReader(csvfile)
                            table += "|" + "|".join(cols) + "|\n"
                            table += "|" + ("----|" * len(cols)) + "\n"
                            for row in reader:
                                for col in cols:
                                    table += "|" + cleans(row[col.lower()])
                                table += "|\n"
                    except:
                        pass
                    string = string.replace(match.group(0),table)
                # If it's not a CSV file, let's assume it is a json path in 36-giving-schema.json
                else:
                    with open("../schema/360-giving-schema.json",'r') as s:
                        schema = json.loads(s.read())
                        try:
                            schema_text = deep_access(schema,match.group(1).split('.'))
                        except:
                            schema_text = "- Documentation Error: Schema path not found -"

                    string = string.replace(match.group(0),schema_text)


            with open("../documentation/"+ file,"w",encoding='utf-8') as write:
                write.write(string)
