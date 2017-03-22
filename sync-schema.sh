# source venv/bin/activate

cd schema/multi-table
rm -rf 360-giving-schema-fields.csv
flatten-tool create-template --root-id='' --output-format all --output-name 360-giving-schema-fields -s ../360-giving-schema.json --main-sheet-name=grants
mv 360-giving-schema-fields 360-giving-schema-fields.csv

cd ../summary-table
mv 360-giving-schema-titles.csv/README.md .
rm -rf 360-giving-schema-titles.csv
flatten-tool create-template --root-id='' --output-format all --output-name 360-giving-schema-titles --schema ../360-giving-schema.json --main-sheet-name=grants --rollup --use-titles
mv 360-giving-schema-titles 360-giving-schema-titles.csv
mv README.md 360-giving-schema-titles.csv/

cd ../../documentation
flatten-tool create-template --root-id='' --output-format csv --output-name tabledefs --schema ../schema/360-giving-schema.json --main-sheet-name=grants --rollup --use-titles --create-reference-tables
