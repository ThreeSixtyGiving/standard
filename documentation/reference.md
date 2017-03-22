# Reference

This page provides reference information on publishing to the 360Giving Data Standard.

It assumes some technical knowledge.

If you are just getting started with the 360Giving data standard, consult the [Publish Your Data](/get-involved/publish-your-data/) pages.

## Data formats

There are two main formats available for representing 360Giving data.

1. **Spreadsheet**

   Data placed in a spreadsheet can make use of easy to read, user-friendly **column titles**, and is ideal for recording one grant per row. This is the most common format that publishers choose. More complex representations of data can also be reported if required.
 
2. **JSON**
   
   Data in JSON format is ideal for direct use by developers building visualisations and web apps. The JSON should conform to the [360Giving JSON Schema](/standard/reference/#toc-360giving-json-schemas). Anyone automating the publication of their data from their internal databases or via an API may favour this format. The column titles used in spreadsheet representations of data are derived directly from the [360Giving JSON Schema](/standard/reference/#toc-360giving-json-schemas).

The [360Giving Data Quality Tool](http://cove.opendataservices.coop/360/) can be used to convert data between these formats, providing structured data for developers, and spreadsheet simplicity if you want to browse, sort and filter data on your desktop. 

## Spreadsheet format

To produce 360Giving data in a spreadsheet, it is possible to start with an empty spreadsheet and construct the column titles (and any additional sheets), using the information given below. However, for many people, the starting point is the spreadsheet template described below.

### Spreadsheet template

For convenience we provide a [360Giving Spreadsheet Template](https://github.com/ThreeSixtyGiving/standard/raw/master/schema/summary-table/360-giving-schema-titles.xlsx) that can be used directly, or adapted to your needs.

The template is a multi-sheet spreadsheet, and each sheet is described below.

Many data producers will be able to fit all the information about a single grant on one row of a spreadsheet. In fact most data producers do exactly that, and provide a single sheet with many individual grants.

Where data producers have more complex information, for example where a grant has many beneficiary locations, we call this a [One to many relationship](/#toc-one-to-many-relationships).
Information about how to create data with [One to many relationships](/#toc-one-to-many-relationships) is described below.

The 360Giving Spreadsheet template consists of a 'grants' sheet which contains the most common data fields. 

The [Additional fields](/#toc-additional-fields) section provides details of all other possible fields that can be reported. (These are derived from the [360Giving JSON Schema](/standard/reference/#toc-360giving-json-schemas) ).


### Grants Sheet

The main 'grants' sheet includes sections for:

* Basic information about the grant;
* Planned dates for the grant;
* Details of the recipient organisation;
* Details of the funding organisation;
* The location of beneficiaries;
* Details of the grant programme funding is from;

```eval_rst
.. csv-table::
    :file: tabledefs/grants.csv
    :header-rows: 1
```

### Additional fields

The main 'grants' sheet only includes the most common information used by most data publishers. For many people this is enough.

The other sheets in the [360Giving Spreadsheet Template](https://github.com/ThreeSixtyGiving/standard/raw/master/schema/summary-table/360-giving-schema-titles.xlsx) provide the details of all the possible fields that can be reported. These sheets serve a dual purpose:

1. As a way to add more information to our 'grants' sheet
   
   The column titles in the extra sheets provide a handy mapping from the JSON Schema to a more human readable form, showing us all of the possible fields available in the 360Giving Data Standard. 
   
   You can use any of these column titles on your main 'grants' sheet if you wish.  

2. As a way of providing information about [Many to one relationships](/#toc-many-to-one-relationships)

If, when creating your data, you only need a few additional fields from the additional sheets, you can simply copy them from one sheet to another.

If you have additional data to report that does not fit any of the columns provided in the spreadsheet, it is okay to create your own column titles in order to report it.


#### Actual Dates

```eval_rst

.. schemavalue:: properties.actualDates.description

```

```eval_rst

.. csv-table::
    :file: tabledefs/actualDates.csv
    :header-rows: 1
```

#### Planned Dates

{{properties.plannedDates.description}}

{{plannedDates.csv|Title,Description,Type,Required}}

#### Funding Org

{{properties.fundingOrganization.description}}

{{fundingOrganization.csv|Title,Description,Type,Required}}

#### Recipient Org

{{properties.recipientOrganization.description}}

{{recipientOrganization.csv|Title,Description,Type,Required}}

#### Beneficiary Location

{{properties.beneficiaryLocation.description}}

{{beneficiaryLocation.csv|Title,Description,Type,Required}}

#### Funding Org:Location

{{definitions.Organization.properties.location.description}}

{{fun_location.csv|Title,Description,Type,Required}}

#### Recipient Org:Location

{{definitions.Organization.properties.location.description}}

{{rec_location.csv|Title,Description,Type,Required}}

#### Related Document

{{properties.relatedDocument.description}}

{{relatedDocument.csv|Title,Description,Type,Required}}

#### Classifications

{{properties.classifications.description}}

{{classifications.csv|Title,Description,Type,Required}}

#### Funding Type

{{properties.fundingType.description}}

{{fundingType.csv|Title,Description,Type,Required}}

#### Grant Programme

{{properties.grantProgramme.description}}

{{grantProgramme.csv|Title,Description,Type,Required}}

#### Transactions

The 360Giving Data Standard also allows for the reporting of three types of transactions:

* commitmentTransaction
* disbursementTransaction
* applicationTransaction

These do not currently have nice human readable titles, but can still be added as spreadsheet columns if needed.

To create the column titles, refer to the 360Giving JSON Schema and use the JSON pointer paths as column titles. e.g. commitmentTransaction/0/id

### One to many relationships

Each of the sections of additional fields above can have multiple occurrences for one grant. There are three ways of describing this in a spreadsheet.

##### Additional sheets

Use the other sheets in the [360Giving Spreadsheet Template](https://github.com/ThreeSixtyGiving/standard/raw/master/schema/summary-table/360-giving-schema-titles.xlsx). These have the columns described above, plus an extra column at the start for the Identifier of the relevant grant.

For the Funding Org: Location and Recipient Org: Location there is also an extra column for the Identifier of the relevant Funding/Recipient Org.

##### Numbering

You can describe multiple occurrences within the Grants sheet by having multiple columns. Use `:<num>:` instead of a `:`. This imitates JSON Pointer's approach.

e.g. to have two related documents with their own title and web address:

|Related Document:0:Title|Related Document:0:Web Address|Related Document:1:Title|Related Document:1:Web Address    |
|------------------------|------------------------------|------------------------|----------------------------------|
|A Document              |http://example.com/adocument  |Another Document        |http://example.com/anotherdocument|

##### Multiple Rows

You can place the additional information about a grant in an additional row. Use the same Identifier for the grant, and place the additional information in the relevant columns. Consuming applications will then be able to try to merge the information into a single record, so be careful not to place contradictory information in fields that cannot have more than one value (e.g. a title or description)


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
* Move columns in the [360Giving Spreadsheet Template](https://github.com/ThreeSixtyGiving/standard/raw/master/schema/summary-table/360-giving-schema-titles.xlsx) between sheets.

You must not:

* **Add extra rows at the top of the table**
* **Change the field names provided by the standard**

## JSON format

The 360Giving standard is defined by a [JSON Schema](http://json-schema.org/), which details the entities that can be described using the standard, and the properties it recognises. 

At the root of the data model is a 'grant'. Grants have a number of direct properties (e.g. Title, Description, Currency, Amount Awarded etc.) and then a number of related entities, including Organisations (Funder and Recipient), Locations (Recipient, Beneficiary), Classifications, Grant Programmes, and Transactions. 

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

Each entity, property and relationship in the schema has both a machine-readable field name and an English language title (apart from Transactions).

The English language titles are important for humans working to make sense of the data in everyday desktop software, and so the Spreadsheet Template and the documentation above makes use of titles as opposed to field names. 

The field names are important for computers reading the data, and even if other language titles are provided in future, the underlying field names will remain constant.

A mapping between column titles and field names for the Grants sheet is given below:

{{grants.csv|Title,Name,Type}}

### JSON

When data is being generated directly out of a database system, publishers should consider using the JSON schema to provide a JSON file.

Developers may also wish to build their applications of JSON versions of the data. 

The [360Giving Data Quality Tool](http://cove.opendataservices.coop/360/) supports round-tripping of data between the Spreadsheet Template and JSON representations. 


