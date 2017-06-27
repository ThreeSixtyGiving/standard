![360Giving Logo](http://openphilanthropy.files.wordpress.com/2014/02/cropped-360givinglogo-2010-size.jpg)

360Giving Standard
========

360Giving aims to help UK grant makers and philanthropists to publish their grant information online in an easy to use way.  We are motivated by a commitment to the value of open data and strategic funding.

The **360Giving Data Standard** provides a common approach for publishing grant data. 

For more about the overall project, visit the main [360Giving website](http://threesixtygiving.com/about/).

Full documentation of the data standard is provided at [http://www.threesixtygiving.org/standard](http://www.threesixtygiving.org/standard/)

## Schema and tools

From Version 1.0 of the schema and onwards:

* The authoritative source of the standard is found in [360-giving-schema.json](schema/360-giving-schema.json) and [360-giving-package-schema.json](schema/360-giving-package-schema.sjon) in [JSON Schema](http://json-schema.org/) format (the former describes what a grant should look like, the second describes how to package up multiple grants into a single JSON file).
* Two secondary serialisation templates are generated using the [flatten-tool](https://github.com/opendataservices/flatten-tool): a summary table (CSV/XLS), and multi-table template (XLS)
* A JSON Table Schema is provided for the summary table

This repository stores the latest versions of the schema, along with tools used in generating secondary serialisations and documentation.

## Editing documentation

Edit the documentation in the [documentation/src](documentation/src) directory, and then run `sync-schema.sh` (described below) to pull information from the schema into the compiled docs in the [documentation](documentation) directory.

## Synchronising schemas

After any changes to the schemas, or to the [source documentation](documentation/src),  `sync-schema.sh` script should be run to:

* Generate CSV and XLSX templates
* Update the documentation

### Installation

To use the sync_schema.sh script you will need a virtual environment set up. 

```
git clone https://github.com/ThreeSixtyGiving/standard.git
cd standard
git submodule init
git submodule update
python3 -m virtualenv -p $(which python3) .ve
source .ve/bin/activate
pip install -r requirements.txt
```
In Windows, instead of `source .ve/bin/activate` run `pyenv\Scripts\activate.bat`

### Build the docs

```
cd documentation
make html
```

Then open `_build/html/index.html` in your browser.

### Synchronising schema

With the virtual environment activated (```source pyenv/bin/activate```) run ```./sync-schema.sh```
