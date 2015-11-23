import re
import os
import csv

def cleans(string):
    return string.replace("\n"," ")

for file in os.listdir("../documentation/src/"):
    if file.endswith(".md"):
        with open("../documentation/src/" + file, 'r',encoding='utf-8') as f:
            string = str(f.read())
            for match in re.finditer("{{([a-zA-z\.]+)([|]*)([a-zA-z,]*)}}", string, flags=0):
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
            with open("../documentation/"+ file,"w",encoding='utf-8') as write:
                write.write(string)
