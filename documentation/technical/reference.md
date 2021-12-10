# Reference

This page provides reference information on publishing to the 360Giving Data Standard.

It assumes some technical knowledge.

If you are just getting started with the 360Giving Data Standard, consult the <a href="https://www.threesixtygiving.org/data/publish-data/" target="_blank"> Publishing your data</a> pages.


## Data formats

There are two main formats available for representing 360Giving data.

1. **Spreadsheet**

   Data placed in a spreadsheet can make use of easy to read, user-friendly **column titles**, and is ideal for recording one grant per row. This is the most common format that publishers choose. More complex representations of data can also be reported if required.

2. **JSON**

   Data in JSON format is ideal for direct use by developers building visualisations and web apps. The JSON should conform to the [360Giving JSON Schemas](360giving-json-schemas). Anyone automating the publication of their data from their internal databases or via an API may favour this format. The column titles used in spreadsheet representations of data are derived directly from the [360Giving JSON Schemas](360giving-json-schemas).

You can use the <a href="https://dataquality.threesixtygiving.org/" target="_blank"> 360Giving Data Quality Tool</a> to convert data between these formats, providing structured data for developers, and spreadsheet simplicity if you want to browse, sort and filter data on your desktop.

## Spreadsheet format

To produce 360Giving data in a spreadsheet, it is possible to start with an empty spreadsheet and construct the column titles (and any additional sheets), using the information given below. However, for many people, the starting point is the spreadsheet template described below.

### Spreadsheet template

For convenience we provide a <a href="../_static/summary-table/360-giving-schema-titles.xlsx">360Giving Spreadsheet Template</a> that can be used directly, or adapted to your needs. The spreadsheet template provided is Excel Workbook file type (.xlsx) but may be converted into OpenDocument Spreadsheet file type (.ods) for publication and use if preferred. [Comma-separated value file](/templates-csv) (.csv) versions are also available.

The Excel template is a multi-sheet spreadsheet, and each sheet is described below. The Comma-separated value (CSV) templates correspond to each sheet of the Excel template.

Many data producers will be able to fit all the information about a single grant on one row of a spreadsheet. In fact most data producers do exactly that, and provide a single sheet with many individual grants.

Where data producers have more complex information, for example where a grant has many beneficiary locations, we call this a 'one to many relationship'.
Information about how to create data with [One to many relationships](one-to-many-relationships) is described below.

The 360Giving Spreadsheet template consists of a 'grants' sheet which contains the most common data fields and fourteen sheets which cover the Additional fields sections.

The [Additional fields](additional-fields) section provides details of all other possible fields that can be reported. (These are derived from the [360Giving JSON Schemas](360giving-json-schemas)).

### Meta Sheet
We also provide a version of the <a href="../_static/360-giving-schema-titles-with-meta-tab.xlsx">360Giving Spreadsheet Template with the Metadata template included</a>. The 'Meta' sheet may be used to publish authoritative metadata about the publisher, the file or dataset. The term we use for this is a 'data package'. The 'Meta' sheet includes sections for:

* The version of the 360Giving Schema used for the file
* The title and description of the file
* The dates when the file was first issued and last modified
* Information about the publisher such as name, logo, website and identifier
* Links to access and download the file
* A link for the open license that applies to the file

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-package-schema.json
```

### Grants Sheet

The main 'grants' sheet includes sections for:

* Basic information about the grant;
* Planned dates for the grant;
* Details of the recipient organisation;
* Details of the funding organisation;
* The location of beneficiaries;
* Details of the grant programme funding is from;

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
```

```eval_rst
.. _additional-fields:
```

### Additional fields

The main 'grants' sheet only includes the most common information used by most data publishers. For many people this is enough.

The other sheets in the <a href="../_static/summary-table/360-giving-schema-titles.xlsx">360Giving Spreadsheet Template</a> provide the details of all the possible fields that can be reported. These sheets serve a dual purpose:

1. As a way to add more information about the grants

   The column titles in the extra sheets provide a handy mapping from the JSON Schema to a more human readable form, showing us all of the possible fields available in the 360Giving Data Standard.

   You can use any of these column titles on your main 'grants' sheet if you wish.

2. As a way of providing information about [One to many relationships](one-to-many-relationships)

If, when creating your data, you only need a few additional fields from the additional sheets, you can copy them from one sheet to the main 'grants' sheet. Any additional sheets that aren't used can be deleted.

If you have additional data to report that does not fit any of the columns provided in the spreadsheet, it is okay to create your own column titles in order to report it.

```eval_rst
.. hint:: **Naming your own columns.**

  If you are adding your own column titles it is best to use simple titles and to avoid special characters which could cause problems in data reuse.

  Using only lowercase and uppercase alphabetical characters (``a-z`` and ``A-Z``), numerical digits (``0-9``), colons (``:``), parentheses (``(`` and ``)``) and single spaces will help to avoid problems. Full-stops (``.``) are known to cause issues and should be avoided. Other characters could be used, but haven't been fully tested in all possible situations. `Contact 360Giving support <mailto:support@threesixtygiving.org>`_ with further queries about naming your own columns.
```

#### Actual Dates

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: actualDates
```

#### Planned Dates

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: plannedDates
```

#### Funding Org

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: fundingOrganization
```

#### Recipient Org

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: recipientOrganization
```

#### Beneficiary Location

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: beneficiaryLocation
```

#### Funding Org:Location

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: fundingOrganization/0/location
```

#### Recipient Org:Location

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: recipientOrganization/0/location
```

#### Related Document

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: relatedDocument
```

#### Classifications

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: classifications
```

#### Funding Type

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: fundingType
```

#### Grant Programme

```eval_rst
.. jsonschema-titles:: ../../schema/360-giving-schema.json
    :child: grantProgramme
```

#### Transactions

The 360Giving Data Standard also allows for the reporting of three types of transactions:

* commitmentTransaction
* disbursementTransaction
* applicationTransaction

These do not currently have the more user friendly human readable titles, but can still be added as spreadsheet columns if needed.

To create the column titles, refer to the [360Giving JSON Schema](#giving-json-schemas) and use the JSON pointer paths as column titles. e.g. commitmentTransaction/0/id

```eval_rst
.. _one-to-many-relationships:
```

### One to many relationships

Each of the sections of additional fields above can have multiple occurrences for one grant. There are three ways of describing this in a spreadsheet.

##### Additional sheets

Use the other sheets in the <a href="../_static/summary-table/360-giving-schema-titles.xlsx">360Giving Spreadsheet Template</a>. These have the columns described above, plus an extra column at the start for the Identifier of the relevant grant.

For the Funding Org: Location and Recipient Org: Location there is also an extra column for the Identifier of the relevant Funding or Recipient Org.

##### Numbering

You can describe multiple occurrences within the Grants sheet by having multiple columns. Use `:<num>:` instead of a `:`. This imitates JSON Pointer's approach.

e.g. to have two related documents with their own title and web address:

```eval_rst

+------------------------+------------------------------+------------------------+----------------------------------+
|Related Document:0:Title|Related Document:0:Web Address|Related Document:1:Title|Related:Document:1:Web Address    |
+------------------------+------------------------------+------------------------+----------------------------------+
|------------------------|------------------------------|------------------------|----------------------------------|
|A Document              |http://example.com/adocument  |Another Document        |http://example.com/anotherdocument|
+------------------------+------------------------------+------------------------+----------------------------------+
```

##### Multiple Rows

There may be cases where you need to release additional information about a grant in a new row, or you can’t update the row where the grant is originally described. In these cases, use the same `Identifier` for the grant, and place the additional information in a new row under the relevant columns. You should only add new information, because consuming applications may try to merge the information into a single record. So placing contradictory information in fields that cannot have more than one value will result in a validation error.

Original row:

```eval_rst
+-----------------+----------------------+-----------------+----------------+
|Identifier       |Title                 |… (other columns)|Amount Disbursed|
+-----------------+----------------------+-----------------+----------------+
|360G-xyztrust-123|An example grant title|…                |                |
+-----------------+----------------------+-----------------+----------------+

```

The new row:

```eval_rst
+-----------------+----------------------+-----------------+----------------+
|Identifier       |Title                 |… (other columns)|Amount Disbursed|
+-----------------+----------------------+-----------------+----------------+
|360G-xyztrust-123|                      |…                |2500            |
+-----------------+----------------------+-----------------+----------------+
```

In the second row, the fields which were originally populated with information are left blank so as to avoid conflicts, and the additional information is added to the "Amount Disbursed" column. This means the multiple rows method can only be used to add new data, and it is not suitable for amending data that has already been published.


### Field guidance

Field guidance provides further useful information about fields in the 360Giving Data Standard. It provides guidance about the correct data formatting to use and some examples of how to apply the formatting when using spreadsheets.

#### Dates and times

The 360Giving Data Standard requires you to provide information on when a grant was awarded, and allows you to add details of when a project is taking place, and when you last updated information about aspects of the grant.

There are three different rules for validating dates:

##### Full dates (Award Dates and Transaction Dates)
The ```Award Date``` **must** provide a full date, including year, month and day in YYYY-MM-DD format (e.g. 2017-04-02 for the 2nd April 2017).

In some cases, award date data exported from grant systems includes the time of the grant, using a date-time format (e.g. 2017-04-02T16:45:00Z - a grant made at 4.45pm).


**Note** - The time component is never significant in Award Dates or Transaction Dates. Applications should ignore the time component when processing grants data.


```eval_rst

.. hint::
  You can set Excel to present a date column in YYYY-MM-DD format using a custom format `as described here`_.

.. _as described here: https://superuser.com/questions/409896/how-do-i-enter-dates-in-iso-8601-date-format-yyyy-mm-dd-in-excel-and-have-exc/409899#409899

```

##### Uncertain dates (Planned Dates and Actual Dates)

Other events in the lifetime of a grant, such as for when the funded activity will take place, may include less specific date information. Funders should aim to be as specific as they can be, but do not need to guess at the particular day or month when an activity will take place if they are not certain or do not yet know.

Dates in the ```Planned Dates``` and ```Actual Dates``` groups should be provided in YYYY-MM-DD format, but the day or the day can be dropped or on the year provided (e.g. YYYY-MM or YYYY).

For example, if an application only indicates that a project will start in May 2019, then the ```Planned Dates:Start Date``` value may be '2019-05'.

It is up to users of the data to judge how to interpret dates which only include a year, or year and month. Different applications and analysis may require different judgements.

##### Date-time (Last Modified dates)
All rows in a 360Giving spreadsheet, and all objects in the JSON structure, can have a ```Last Modified``` date.

If used, this must always be in full date-time format so that if multiple updates take place on a single day, consuming applications can work out which version to use.

``` eval_rst

.. hint::
  You can set Excel to present a date column as a full date-time using the custom format of "yyyy-mm-ddThh:mm:ssZ". If you also set the formula for the entire column to ```=Now()``` then this value will be refreshed automatically every time you save the file.
```

### Conformance

In order to conform with the spreadsheet standard:

You must:

* **Read the column definitions carefully and follow the format they request** - for example, formatting identifiers and dates according to the standard. Full reference information is provided below.
* **Provide an Identifier** for each grant
* **Update the Last Modified date** whenever the status of a grant changes

You can:

* **Remove or hide non-required columns that you are not using** - although make sure you check for any [hidden columns](#hidden-columns) before publishing your data, and always remove rather than hide sensitive information.
* **Re-order the columns** so that information is arranged in the way you want
* **Add extra columns** to include information you want to share, but that is not covered by the standard. (See [additional fields](additional-fields)).
* **Move columns** in the <a href="../_static/summary-table/360-giving-schema-titles.xlsx">360Giving Spreadsheet Template</a> between sheets.

You must not:

* **Add extra rows at the top of the table**
* **Change the field names provided by the 360Giving Data Standard**

## JSON format

The 360Giving Data Standard is defined by a <a href="https://json-schema.org/" target="_blank"> JSON Schema</a>, which details the entities that can be described using the standard, and the properties it recognises.

At the root of the data model is a 'grant'. Grants have a number of direct properties (e.g. Title, Description, Currency, Amount Awarded etc.) and then a number of related entities, including Organisations (Funder and Recipient), Locations (Recipient, Beneficiary), Classifications, Grant Programmes, and Transactions.

```eval_rst
.. _360giving-json-schemas:
```

### 360Giving JSON Schemas
The 360Giving JSON Schemas are the authoritative source of information about the 360Giving Data Standard, and it should always be possible to transform 360Giving data into structured JSON data according to these schemas.

The <a href="../_static/360-giving-schema.json">360Giving Grant Schema</a> defines the structure of an individual 'grant' and the documentation from this is displayed below, or <a href="../_static/docson/index.html#../360-giving-schema.json">fullscreen here</a>.

When exchanging data about a single grant or any number of grants, those grants need to be packaged into a single JSON file. This is to ensure that the way the grant data may be consumed remains consistent regardless of whether there are 10 grants or 10,000 grants. The <a href="../_static/360-giving-package-schema.json">360Giving Package  Schema</a> describes how grants are packaged into one file and may be used to publish authoritative metadata about the publisher, the file or dataset (not a grant). Metadata is declared using the fields in the package schema (except for grants which is a list of grant data).

In general, most publishers will use a subset of the possible features of the 360Giving Data Standard, but it is designed to accommodate comprehensive data about all stages of a grant process: for a full 360-degree view.

<div style="height:400px; overflow:auto; border:1px solid grey;">
<script src="../_static/docson/widget.js"
data-schema="../360-giving-package-schema.json">
</script>
</div>

<div id="custom-docson-container">
  <script src="../_static/docson/widget.js"
        data-schema="../360-giving-schema.json">
  </script>
</div>


### Field names and titles

Each entity, property and relationship in the 360Giving Data Standard Schema and 360Giving Package Schema has both a machine-readable field name and an English language title (apart from Transactions in the 360Giving Data Standard Schema).

The English language titles are important for humans working to make sense of the data in everyday desktop software, and so the Spreadsheet Template and the documentation above makes use of titles as opposed to field names.

The field names are important for computers reading the data, and if other language titles are provided in future, the underlying field names will remain constant.

A mapping between column titles and field names for each schema is given below:

#### 360Giving Package Schema (incorporating Metadata)
```eval_rst
.. jsonschema-title-fieldname-map:: ../../schema/360-giving-package-schema.json
```

#### 360Giving Data Standard Schema
```eval_rst
.. jsonschema-title-fieldname-map:: ../../schema/360-giving-schema.json
```

### JSON

When data is being generated directly out of a database system, publishers should consider using the JSON schema to provide a JSON file.

Developers may also wish to build their applications of JSON versions of the data.

The <a href="https://dataquality.threesixtygiving.org/" target="_blank"> 360Giving Data Quality Tool</a> supports conversion of data between the Spreadsheet Template and JSON representations.
