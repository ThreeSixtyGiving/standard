## Convenience script for building the codelist of geographic code areas.
import json
import urllib2
import csv

def fetch_items(url):
    response = urllib2.urlopen(url)
    json_data = json.loads(response.read())
    
    rows = []
    for item in json_data['result']['items']:
        try:
            if item['status'] == 'live' and int(item.get('liveinstances',0)) > 8:
                rows.append([item['abbreviation'],item['name'],"An ONS "+item['theme'] + " codelist",item['_about'],item['firstcode']])
        except:
            pass
        
    if json_data['result'].get('next',''):  
        print json_data['result'].get('next','')
        rows = rows + fetch_items(json_data['result'].get('next',''))
    return rows

rows = fetch_items('http://statistics.data.gov.uk/doc/statistical-entity/.json?_pageSize=50&_view=full&_page=1')
with open('../codelists/geoCodeType-temp.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Code','Name','Description','Documentation (URL)','Values (URL)'])   
    for row in rows:
        writer.writerow(row)

    
            
