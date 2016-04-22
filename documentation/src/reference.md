<div id="toc"></div>

## Standard Reference

This page provides reference information on publishing to the 360Giving Data Standard.

It assumes some technical knowledge.

If you are just getting started with the 360Giving data standard, consult the [start publishing](/get-involved/publish-your-data/) pages.

## Data formats

There are two main formats available for representing 360Giving data.

1. **Spreadsheet**: provided with user-friendly **column titles**, and for recording one grant per row. This is the most common template that publishers choose.
2. **JSON Schema**: for providing a structured representation of your data direct from your internal databases or via an API. Ideal for direct use by developers building visualisations and web apps.

In future, [a CSV Data Package](http://data.okfn.org/doc/data-package) serialisation will be available. Contact us if you need this.

The [CoVE](http://cove.opendataservices.coop/360/) (Convert, Validate and Explore) tool can be used to round-trip data between these formats, providing structured data for developers, and spreadsheet simplicity if you want to browse, sort and filter data on your desktop. 

## Spreadsheet format

The 360Giving Spreadsheet format consists of a 'grants' sheet which contains the most common data fields, and a series of additional tabs which can be used to provide more details about individual grants.

### Grants Sheet

The default grants sheet includes sections for:

* Basic information about the grant;
* Planned and actual dates of activity;
* Details of the recipient organisation;
* Details of the funding organisation;
* The location of beneficiaries;
* Details of the grant programme funding is from;

{{grants.csv|Title,Description,Type,Required}}

### Additional fields

The default grants sheet only includes common information. Other fields can be added to the Grants sheet with the column headings described below.

#### Actual Dates

{{actualDates.csv|Title,Description,Type,Required}}

#### Planned Dates

{{plannedDates.csv|Title,Description,Type,Required}}

#### Funding Org

{{fundingOrganization.csv|Title,Description,Type,Required}}

#### Recipient Org

{{recipientOrganization.csv|Title,Description,Type,Required}}

#### Beneficiary Location

{{beneficiaryLocation.csv|Title,Description,Type,Required}}

#### Funding Org:Location

{{fun_location.csv|Title,Description,Type,Required}}

#### Recipient Org:Location

{{rec_location.csv|Title,Description,Type,Required}}

#### Related Document

{{relatedDocument.csv|Title,Description,Type,Required}}

#### Classifications

{{classifications.csv|Title,Description,Type,Required}}

#### Funding Type

{{fundingType.csv|Title,Description,Type,Required}}

#### Grant Programme

{{grantProgramme.csv|Title,Description,Type,Required}}

#### commitmentTransaction

{{commitmentTransaction.csv|Title,Description,Type,Required}}

#### disbursementTransaction

{{disbursementTransaction.csv|Title,Description,Type,Required}}

#### applicationTransaction

{{applicationTransaction.csv|Title,Description,Type,Required}}

### Many to one relationships

Each of the sections of additional fields above can have multiple occurrences for one grant. There are two ways of describing this in a spreadsheet.

#### Additional tabs

Use the other tabs in the spreadsheet template. These have the columns described above, plus an extra column at the start for the Identifier of the relevant grant.

For the funding org location and recipient org location there is also an extra column for the identifier of the relevant funding/recipient org.

#### Numbering

You can describe multiple occurrences within the Grants sheet by having multiple columns. Use `:<num>:` instead of a `:`. This immitates json pointer's approach.

e.g. to have two related documents with their own title and web address:

|Related Document:0:Title|Related Document:0:Web Address|Related Document:1:Title|Related Document:1:Web Address    |
|------------------------|------------------------------|------------------------|----------------------------------|
|A Document              |http://example.com/adocument  |Another Document        |http://example.com/anotherdocument|


### Conformance

In order to conform with the spreadsheet standard:

You must:

* **Read the column definitions carefully and follow the format they request** - for example, formatting identifiers and dates according to the standard. Full reference information is provided below.
* **Provide an identifier** for each grant
* **Update the last modified date** whenever the status of a grant changes

You can:

* **Remove or hide non-required columns that you are not using** - although make sure you check any [hidden columns](#hidden-columns) before publishing your data, and always remove rather than hide sensitive information.
* **Re-order the columns** so that information is arranged in the way you want
* **Add extra columns** to include information you want to share, but that is not covered by the standard. 

You must not:

* **Add extra rows at the top of the table**
* **Change the field names provided by the standard**

## JSON data model

The 360Giving standard is defined by a modified [JSON Schema](http://json-schema.org/). This details the entities that can be described using the standard, and the properties it recognises. 

At the root of the data model is a grant. Grants have a number of direct properties (e.g. Title, Description, Currency, Amount Awarded etc.) and then a number of related entities, including Organisations (Funder and Recipient), Locations (Recipient, Beneficiary), Classifications, Grant Programmes, and Transactions. 

### 360Giving JSON Schemas
The 360Giving JSON Schemas are the authoritative source of information about the standard, and it should always be possible to transform 360Giving data into structured JSON data according to these schema. 

The [360Giving Grant Schema](/wp-content/plugins/threesixty_docs/standard/schema/360-giving-schema.json) defines the structure of an individual 'grant' and the documentation from this is displayed below, or [fullscreen here](/wp-content/plugins/threesixty_docs/docson/index.html#/wp-content/plugins/threesixty_docs/standard/schema/360-giving-schema.json).

When exchanging data about a single grant or any number of grants, those grants need to be packaged into a single JSON file. The [360Giving Package  Schema](/wp-content/plugins/threesixty_docs/standard/schema/360-giving-package-schema.json) describes how grants are packaged into one file.

In general, most publishers will initially only use a sub-set of the possible features of the standard, but it is designed to accommodate comprehensive data about all stages of a grant process: for a full 360-degree view.

<div style="height:400px; overflow:auto; border:1px solid grey;">
<script src="/wp-content/plugins/threesixty_docs/docson/widget.js" 
        data-schema="/wp-content/plugins/threesixty_docs/standard/schema/360-giving-schema.json">      
</script>
</div>

### Field names and titles

Each entity, property and relationship in the schema has both a machine-readable field name and an English language title.

The English language titles are important for humans working to make sense of the data in everyday desktop software, and so the default Summary Template makes use of titles as opposed to field names. 

The field names are important for computers reading the data, and even if other language titles are provided in future, the underlying field names will remain constant.

A mapping between column titles and field names for the Summary Table is given below:

{{grants.csv|Title,Name,Type}}

### JSON

When data is being generated directly out of a database system, publishers should consider using the JSON schema to provide a JSON file.

Developers may also wish to build their applications of JSON versions of the data. 

The [CoVE](http://cove.opendataservices.coop/360/) (Convert, Validate and Explore) tool supports round-tripping of data between Summary spreadsheet, multi-table datapackage and JSON representations. 


## Schema documentation

Identifiers are documented on the [identifiers](/identifiers/) pages.


