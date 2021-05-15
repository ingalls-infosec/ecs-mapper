from pandas.io.json import json_normalize
import json
import csv

kibana_export_path = '/Users/efoster/Downloads/export(2).ndjson'
index_name = 'suricata'

csv_file = f"implementation/mapping_csv/{index_name}_fields.csv"
csv_columns = ['source_field','copy_action','format_action','timestamp_format','destination_field','Notes']

with open(kibana_export_path) as data_file:    
    d= json.load(data_file)  

fields = json.loads(d['attributes']['fields'])

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for r in fields:
            if '@' in r['name'] or r['name'].startswith('_'):
                continue
            if 'esTypes' not in r.keys():
                r['esTypes'] = ''
            writer.writerow({
                'source_field' : r['name'],
                'copy_action' : '',
                'format_action' : '',
                'timestamp_format' : '',
                'destination_field' : '',
                'Notes' : f"{r['esTypes']}"
                })
except IOError:
    print("I/O error")
