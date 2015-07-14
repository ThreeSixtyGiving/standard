![360 Giving Logo](http://openphilanthropy.files.wordpress.com/2014/02/cropped-360givinglogo-2010-size.jpg)

360 Giving Standard
========

360 Giving aims to help UK grant makers and philanthropists to publish their grant information online in an easy to use way.  We are motivated by a commitment to the value of open data and strategic funding.

The **360 Giving Data Standard** provides a common approach for publishing grant data. 

For more about the overall project, visit the main [360 Giving website](http://threesixtygiving.com/about/).

Full documentation of the data standard is provided at [http://threesixtygiving.github.io](http://threesixtygiving.github.io)

## Schema and tools

From Version 1.0 of the schema and onwards:

* The authoritative source of the standard is found in 360-giving-schema.json in [JSON Schema](http://json-schema.org/) format.
* Two secondary serialisation templates are generated using the [flatten-tool](https://github.com/opendataservices/flatten-tool): a summary table (CSV/XLS), and multi-table template (XLS)
* A JSON Table Schema is provided for the summary table

This repository stores the latest versions of the schema, along with tools used in generating secondary serialisations and documentation.


## Synchronising schemas

After any changes to 360-giving-schema.json the sync_schema.sh script should be run to:

* Generate CSV and XLSX templates
* Update the documentation

### Installation

To use the sync_schema.sh script you will need a virtual environment set up. 

```
git clone https://github.com/ThreeSixtyGiving/standard.git
cd standard
virtualenv pyenv
source pyenv/bin/activate
pip install -r requirements.txt
```

### Synchronising schema

With the virtual environment activated (```source pyenv/bin/activate```) run ```./sync_schema.sh```