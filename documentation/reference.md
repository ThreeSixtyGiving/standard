<div id="toc"></div>

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

###Spreadsheet template

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
* Planned dates of the activity;
* Details of the recipient organisation;
* Details of the funding organisation;
* The location of beneficiaries;
* Details of the grant programme funding is from;

|Title|Description|Type|Required|
|----|----|----|----|
|Identifier|The unique identifier for this grant. Made up of your 360Giving prefix, and an identifier from your records. See the [360Giving Grant identifier guidance](http://www.threesixtygiving.org/standard/identifiers/#toc-grant-identifier) for details.|string|True|
|Title|A title for this grant activity. This should be under 140 characters long.|string|True|
|Description|A short description of this grant activity.|string|True|
|Currency|The currency used in amounts. The currency used in amounts. Use the three-letter currency code from [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) eg: GBP|string|True|
|Amount Applied For|Total amount applied for in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the application transactions for this grant.|number|False|
|Amount Awarded|Total amount awarded in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the award transactions for this grant.|number|True|
|Amount Disbursed|Total amount disbursed (paid) to this grantee when this record was last updated (in numbers: do not include commas or currency symbols such as £)). If you have provided detailed transaction information on a separate table, this should equal the sum of all the disbursement transactions for this grant.|number|False|
|Award Date|When was the decision to award this grant made. The date should be written as YYYY-MM-DD, or in full date-time format.|string|True|
|URL|A URL (Web Address) where further information about this grant can be found. This could point to the website of the recipient organisation, or might link to further details on the funders website.|uri|False|
|Planned Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD or date-time format. If the month or day are not available, these may be omitted.|string|False|
|Planned Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD or date-time format. If the month or day are not available, these may be omitted.|string|False|
|Planned Dates:Duration (months)|Events or activities lasting more than one day should have either a duration (in months) or an end date.|string|False|
|Recipient Org:Identifier|A globally unique identifier for this organisation. This is important to enable data on funders and recipients to be linked up across different grant-makers. The [Organisation Identifier Standard](http://www.threesixtygiving.org/standard/identifiers/#toc-organisation-identifier) guidance explains how to create this ID, based either on the known company or charity number, or upon identifiers held in the grant-maker's internal systems.|string|True|
|Recipient Org:Name|Organisation name|string|True|
|Recipient Org:Charity Number|Registered charity number, if applicable.|string|False|
|Recipient Org:Company Number|Registered UK company number, if applicable.|string|False|
|Recipient Org:Street Address|Building number and street name.|string|False|
|Recipient Org:City|City or town.|string|False|
|Recipient Org:County|County|string|False|
|Recipient Org:Country|Country|string|False|
|Recipient Org:Postal Code|Postal code (please try and provide a post code whenever possible)|string|False|
|Recipient Org:Description|A short description of this organisation and its area of work|string|False|
|Recipient Org:Web Address|A web address for the Organisation|uri|False|
|Beneficiary Location:Name|A name for this location.|string|False|
|Beneficiary Location:Country Code|The ISO Country Code of the location of this activity.|string|False|
|Beneficiary Location:Latitude|The latitude of a point location|string|False|
|Beneficiary Location:Longitude|The longitude of a point location|string|False|
|Beneficiary Location:Geographic Code|A code referring to a geographical area, drawn from an established gazetteer. For example, the code for a local authority ward, or parliamentary constituency.|string|False|
|Beneficiary Location:Geographic Code Type|The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the [codelist of geographic code types](https://github.com/ThreeSixtyGiving/standard/tree/master/codelists/geoCodeType.csv).|string|False|
|Funding Org:Identifier|A globally unique identifier for this organisation. This is important to enable data on funders and recipients to be linked up across different grant-makers. The [Organisation Identifier Standard](http://www.threesixtygiving.org/standard/identifiers/#toc-organisation-identifier) guidance explains how to create this ID, based either on the known company or charity number, or upon identifiers held in the grant-maker's internal systems.|string|True|
|Funding Org:Name|Organisation name|string|True|
|Funding Org:Department|The department or sub-unit of this organisation making or receiving the grant.|string|False|
|Grant Programme:Code|An identifier for this grant programme.|string|False|
|Grant Programme:Title|The title of this grant programme.|string|False|
|Grant Programme:URL|A web link to more details of this grant programme.|uri|False|
|From an open call?|Was this grant made as the result of an open call for applications? Values should be 'Yes' or 'No'|string|False|
|Related Activity|The identifiers of any related activities (e.g. other grants given as part of a multi-grant project)|array|False|
|Last modified|When was information on this grant last updated? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|
|Data Source|A web link pointing to the source of this data. This may be an original 360Giving data file, a file from which the data was converted, or an organisation website.|uri|False|


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

|Title|Description|Type|Required|
|----|----|----|----|
|Actual Dates:Title|The title of this event|string|False|
|Actual Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD or date-time format. If the month or day are not available, these may be omitted.|string|False|
|Actual Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD or date-time format. If the month or day are not available, these may be omitted.|string|False|
|Actual Dates:Duration (months)|Events or activities lasting more than one day should have either a duration (in months) or an end date.|string|False|
|Actual Dates:Description|A description of this event|string|False|
|Actual Dates:Last modified|When was information about this event last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Planned Dates

|Title|Description|Type|Required|
|----|----|----|----|
|Planned Dates:Title|The title of this event|string|False|
|Planned Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD or date-time format. If the month or day are not available, these may be omitted.|string|False|
|Planned Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD or date-time format. If the month or day are not available, these may be omitted.|string|False|
|Planned Dates:Duration (months)|Events or activities lasting more than one day should have either a duration (in months) or an end date.|string|False|
|Planned Dates:Description|A description of this event|string|False|
|Planned Dates:Last modified|When was information about this event last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Funding Org

|Title|Description|Type|Required|
|----|----|----|----|
|Funding Org:Identifier|A globally unique identifier for this organisation. This is important to enable data on funders and recipients to be linked up across different grant-makers. The [Organisation Identifier Standard](http://www.threesixtygiving.org/standard/identifiers/#toc-organisation-identifier) guidance explains how to create this ID, based either on the known company or charity number, or upon identifiers held in the grant-maker's internal systems.|string|True|
|Funding Org:Name|Organisation name|string|True|
|Funding Org:Department|The department or sub-unit of this organisation making or receiving the grant.|string|False|
|Funding Org:Contact Name|-|string|False|
|Funding Org:Charity Number|Registered charity number, if applicable.|string|False|
|Funding Org:Company Number|Registered UK company number, if applicable.|string|False|
|Funding Org:Street Address|Building number and street name.|string|False|
|Funding Org:City|City or town.|string|False|
|Funding Org:County|County|string|False|
|Funding Org:Country|Country|string|False|
|Funding Org:Postal Code|Postal code (please try and provide a post code whenever possible)|string|False|
|Funding Org:Phone Number|Contact phone number.|string|False|
|Funding Org:Alternate Name|An alternative name for this organisation (e.g. trading name)|string|False|
|Funding Org:Email|-|string|False|
|Funding Org:Description|A short description of this organisation and its area of work|string|False|
|Funding Org:Organisation Type|A description of this organisation|string|False|
|Funding Org:Web Address|A web address for the Organisation|uri|False|
|Funding Org:Last modified|When was the organisation information for this grant last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Recipient Org

|Title|Description|Type|Required|
|----|----|----|----|
|Recipient Org:Identifier|A globally unique identifier for this organisation. This is important to enable data on funders and recipients to be linked up across different grant-makers. The [Organisation Identifier Standard](http://www.threesixtygiving.org/standard/identifiers/#toc-organisation-identifier) guidance explains how to create this ID, based either on the known company or charity number, or upon identifiers held in the grant-maker's internal systems.|string|True|
|Recipient Org:Name|Organisation name|string|True|
|Recipient Org:Department|The department or sub-unit of this organisation making or receiving the grant.|string|False|
|Recipient Org:Contact Name|-|string|False|
|Recipient Org:Charity Number|Registered charity number, if applicable.|string|False|
|Recipient Org:Company Number|Registered UK company number, if applicable.|string|False|
|Recipient Org:Street Address|Building number and street name.|string|False|
|Recipient Org:City|City or town.|string|False|
|Recipient Org:County|County|string|False|
|Recipient Org:Country|Country|string|False|
|Recipient Org:Postal Code|Postal code (please try and provide a post code whenever possible)|string|False|
|Recipient Org:Phone Number|Contact phone number.|string|False|
|Recipient Org:Alternate Name|An alternative name for this organisation (e.g. trading name)|string|False|
|Recipient Org:Email|-|string|False|
|Recipient Org:Description|A short description of this organisation and its area of work|string|False|
|Recipient Org:Organisation Type|A description of this organisation|string|False|
|Recipient Org:Web Address|A web address for the Organisation|uri|False|
|Recipient Org:Last modified|When was the organisation information for this grant last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Beneficiary Location

|Title|Description|Type|Required|
|----|----|----|----|
|Beneficiary Location:Identifier|Location identifier|string|False|
|Beneficiary Location:Name|A name for this location.|string|False|
|Beneficiary Location:Country Code|The ISO Country Code of the location of this activity.|string|False|
|Beneficiary Location:Latitude|The latitude of a point location|string|False|
|Beneficiary Location:Longitude|The longitude of a point location|string|False|
|Beneficiary Location:Description|A description of this location. This could include details of the element of the activity that takes place here.|string|False|
|Beneficiary Location:Geographic Code|A code referring to a geographical area, drawn from an established gazetteer. For example, the code for a local authority ward, or parliamentary constituency.|string|False|
|Beneficiary Location:Geographic Code Type|The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the [codelist of geographic code types](https://github.com/ThreeSixtyGiving/standard/tree/master/codelists/geoCodeType.csv).|string|False|
|Beneficiary Location:Last modified|When was this location information last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Funding Org:Location

|Title|Description|Type|Required|
|----|----|----|----|
|Funding Org:Location:Identifier|Location identifier|string|False|
|Funding Org:Location:Name|A name for this location.|string|False|
|Funding Org:Location:Country Code|The ISO Country Code of the location of this activity.|string|False|
|Funding Org:Location:Latitude|The latitude of a point location|string|False|
|Funding Org:Location:Longitude|The longitude of a point location|string|False|
|Funding Org:Location:Description|A description of this location. This could include details of the element of the activity that takes place here.|string|False|
|Funding Org:Location:Geographic Code|A code referring to a geographical area, drawn from an established gazetteer. For example, the code for a local authority ward, or parliamentary constituency.|string|False|
|Funding Org:Location:Geographic Code Type|The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the [codelist of geographic code types](https://github.com/ThreeSixtyGiving/standard/tree/master/codelists/geoCodeType.csv).|string|False|
|Funding Org:Location:Last modified|When was this location information last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Recipient Org:Location

|Title|Description|Type|Required|
|----|----|----|----|
|Recipient Org:Location:Identifier|Location identifier|string|False|
|Recipient Org:Location:Name|A name for this location.|string|False|
|Recipient Org:Location:Country Code|The ISO Country Code of the location of this activity.|string|False|
|Recipient Org:Location:Latitude|The latitude of a point location|string|False|
|Recipient Org:Location:Longitude|The longitude of a point location|string|False|
|Recipient Org:Location:Description|A description of this location. This could include details of the element of the activity that takes place here.|string|False|
|Recipient Org:Location:Geographic Code|A code referring to a geographical area, drawn from an established gazetteer. For example, the code for a local authority ward, or parliamentary constituency.|string|False|
|Recipient Org:Location:Geographic Code Type|The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the [codelist of geographic code types](https://github.com/ThreeSixtyGiving/standard/tree/master/codelists/geoCodeType.csv).|string|False|
|Recipient Org:Location:Last modified|When was this location information last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Related Document

|Title|Description|Type|Required|
|----|----|----|----|
|Related Document:Identifier|An identifier for this document.|string|False|
|Related Document:Title|The document title.|string|False|
|Related Document:Web Address|The URL of the document.|uri|False|
|Related Document:Description|A description of the document.|string|False|
|Related Document:Document Type|A document category. For example, 'Application Form', 'Photo' or 'Project Report'. In future, 360Giving will provide a codelist of document types.|string|False|
|Related Document:Last modified|What was this information last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Classifications

|Title|Description|Type|Required|
|----|----|----|----|
|Classifications:Vocabulary|A vocabulary used for this classification.|string|False|
|Classifications:Code|A codelist value in the chosen vocabulary.|string|False|
|Classifications:Title|The title of this classification.|string|False|
|Classifications:Description|A description of this classification.|string|False|
|Classifications:URL|A web link to more details of this classification.|uri|False|
|Classifications:Last modified|When was this grant classification information last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Funding Type

|Title|Description|Type|Required|
|----|----|----|----|
|Funding Type:Vocabulary|A vocabulary used for this classification.|string|False|
|Funding Type:Code|A codelist value in the chosen vocabulary.|string|False|
|Funding Type:Title|The title of this classification.|string|False|
|Funding Type:Description|A description of this classification.|string|False|
|Funding Type:URL|A web link to more details of this classification.|uri|False|
|Funding Type:Last modified|When was this grant classification information last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


#### Grant Programme

|Title|Description|Type|Required|
|----|----|----|----|
|Grant Programme:Code|An identifier for this grant programme.|string|False|
|Grant Programme:Title|The title of this grant programme.|string|False|
|Grant Programme:Description|A description of this grant programme.|string|False|
|Grant Programme:URL|A web link to more details of this grant programme.|uri|False|
|Grant Programme:Last modified|When was the link between this grant and its grant programme last modified? A full date-time should be given. Usually this can be generated automatically by the software managing or exporting this data.|date-time|False|


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


### Field guidance

#### Dates and times

360Giving allows you to provide information on when a grant was awarded, when a project is taking place, and when you last updated information about aspects of the grant.

There are three different rules for validating dates

##### Award dates
The ```Award Date``` must provide a full date, including year, month and day in YYYY-MM-DD format (e.g. 2016-04-02 for the 2nd April 2016). 

In some rare cases, an award date might also need to include the time of the grant, using a date-time format (e.g. 2016-04-02T16:45:00Z for a grant made at 4.45 if the afternoon). 

**Tip**: You can set Excel to present a date column in YYYY-MM-DD format using a custom format [as described here](http://superuser.com/questions/409896/how-do-i-enter-dates-in-iso-8601-date-format-yyyy-mm-dd-in-excel-and-have-exc/409899#409899). 

##### Other events
Other events in the lifetime of a grant, such as the planned dates when the funded activity will take place may include more or less specific dates. Funders should aim to be as specific as they can be, but do not need to guess at the particular day or month when an activity will take place if they do not know. Dates should always be provided in YYYY-(MM)-(DD) format. 

For example, if an application only indicates a project will start in May 2016, then the ```Planned Dates:Start Date``` field may be '2016-05'. 

It is up to users of the data to judge how to interpret dates which only include a year, or year and month. Different applications and analysis may require different judgements. 

##### Last modified dates
All rows in a 360Giving spreadsheet, and all objects in the JSON structure, can have a ```Last Modified``` date. 

This should always be a full date-time so that if multiple updates take place on a single day, consuming applications can work out which version to use. 

**Tip**: You can set Excel to present a date column as a full date-time using the custom format of "yyyy-mm-ddThh:mm:ssZ". If you set the formula for the column to ```=Now()``` then the last updated value will be refreshed automatically everytime you save the file. 

* **Award Date** - this should be the full date 


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

|Title|Name|Type|
|----|----|----|
|Identifier|id|string|
|Title|title|string|
|Description|description|string|
|Currency|currency|string|
|Amount Applied For|amountAppliedFor|number|
|Amount Awarded|amountAwarded|number|
|Amount Disbursed|amountDisbursed|number|
|Award Date|awardDate|string|
|URL|url|uri|
|Planned Dates:Start Date|plannedDates/0/startDate|string|
|Planned Dates:End Date|plannedDates/0/endDate|string|
|Planned Dates:Duration (months)|plannedDates/0/duration|string|
|Recipient Org:Identifier|recipientOrganization/0/id|string|
|Recipient Org:Name|recipientOrganization/0/name|string|
|Recipient Org:Charity Number|recipientOrganization/0/charityNumber|string|
|Recipient Org:Company Number|recipientOrganization/0/companyNumber|string|
|Recipient Org:Street Address|recipientOrganization/0/streetAddress|string|
|Recipient Org:City|recipientOrganization/0/addressLocality|string|
|Recipient Org:County|recipientOrganization/0/addressRegion|string|
|Recipient Org:Country|recipientOrganization/0/addressCountry|string|
|Recipient Org:Postal Code|recipientOrganization/0/postalCode|string|
|Recipient Org:Description|recipientOrganization/0/description|string|
|Recipient Org:Web Address|recipientOrganization/0/url|uri|
|Beneficiary Location:Name|beneficiaryLocation/0/name|string|
|Beneficiary Location:Country Code|beneficiaryLocation/0/countryCode|string|
|Beneficiary Location:Latitude|beneficiaryLocation/0/latitude|string|
|Beneficiary Location:Longitude|beneficiaryLocation/0/longitude|string|
|Beneficiary Location:Geographic Code|beneficiaryLocation/0/geoCode|string|
|Beneficiary Location:Geographic Code Type|beneficiaryLocation/0/geoCodeType|string|
|Funding Org:Identifier|fundingOrganization/0/id|string|
|Funding Org:Name|fundingOrganization/0/name|string|
|Funding Org:Department|fundingOrganization/0/department|string|
|Grant Programme:Code|grantProgramme/0/code|string|
|Grant Programme:Title|grantProgramme/0/title|string|
|Grant Programme:URL|grantProgramme/0/url|uri|
|From an open call?|fromOpenCall|string|
|Related Activity|relatedActivity|array|
|Last modified|dateModified|date-time|
|Data Source|dataSource|uri|


### JSON

When data is being generated directly out of a database system, publishers should consider using the JSON schema to provide a JSON file.

Developers may also wish to build their applications of JSON versions of the data. 

The [360Giving Data Quality Tool](http://cove.opendataservices.coop/360/) supports round-tripping of data between the Spreadsheet Template and JSON representations. 


