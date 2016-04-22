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

To provide classifications of grants, more than one location, or additional documents related to the grant, you will need to publish information in sub-tables. 

|Title|Description|Type|Required|
|----|----|----|----|
|Identifier|The unique identifier for this grant. Made up of your 360Giving prefix, and an identifier from your records. See the [360Giving Grant identifier guidance](http://www.threesixtygiving.org/standard/identifiers/#toc-grant-identifier) for details.|string|True|
|Title|A title for this grant activity. This should be under 140 characters long.|string|True|
|Description|A short description of this grant activity.|string|True|
|Currency|The currency used in amounts. The currency used in amounts. Use the three-letter currency code from [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) eg: GBP|string|True|
|Amount Applied For|Total amount applied for in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the application transactions for this grant.|number|False|
|Amount Awarded|Total amount awarded in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the award transactions for this grant.|number|True|
|Amount Disbursed|Total amount disbursed (paid) to this grantee when this record was last updated (in numbers: do not include commas or currency symbols such as £)). If you have provided detailed transaction information on a separate table, this should equal the sum of all the disbursement transactions for this grant.|number|False|
|Award Date|When was the decision to award this grant made. Dates should be in YYYY-MM-DD format.|date-time|True|
|URL|A URL (Web Address) where further information about this grant can be found. This could point to the website of the recipient organisation, or might link to further details on the funders website.|uri|False|
|Planned Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
|Planned Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
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
|Last modified|The date when information on this grant was last updated|date-time|False|
|Data Source|A web link pointing to the source of this data. This may be an original 360Giving data file, a file from which the data was converted, or an organisation website.|uri|False|


### Additional tables

The grants sheet can only accommodate one-to-one relationships. For example, one classification or location per grant. It also only includes common information.

To provide details of additional classifications, locations, events, documents, organization and transaction information you can use the other tabs of the spreadsheet. 

In the first column of each tab you would enter the identifier of the grant to which the additional information relates, as recorded in the id column of the grant sheet. 

|Title|Description|Type|Required|
|----|----|----|----|
|Actual Dates:Title|-|string|False|
|Actual Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
|Actual Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
|Actual Dates:Duration (months)|Events or activities lasting more than one day should have either a duration (in months) or an end date.|string|False|
|Actual Dates:Description|-|string|False|
|Actual Dates:Last modified|-|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
||Identifier|string|False|
||When did this transaction take place? Please use YYYY-MM-DD format.|date-time|False|
||The currency used in amounts. The currency used in amounts. Use the three-letter currency code from [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) eg: GBP|string|False|
||The total value of this transaction.|integer|False|
||The date that this value was set (to allow historical currency conversion). The date must be in ISO 8601 format (YYYY-MM-DD).|date-time|False|
||A description of this transaction.|string|False|
||The organisation identifier of the provider of transaction funds.|string|False|
||The organisation identifier of the recipient of transaction funds.|string|False|
||When information about this transaction was last updated.|date-time|False|

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
|Beneficiary Location:Last modified|The date when location information was last modified.|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
|Classifications:Vocabulary|A vocabulary used for this classification.|string|False|
|Classifications:Code|A codelist value in the chosen vocabulary.|string|False|
|Classifications:Title|The title of this classification.|string|False|
|Classifications:Description|A description of this classification.|string|False|
|Classifications:URL|A web link to more details of this classification.|uri|False|
|Classifications:Last modified|-|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
||Identifier|string|False|
||When did this transaction take place? Please use YYYY-MM-DD format.|date-time|False|
||The currency used in amounts. The currency used in amounts. Use the three-letter currency code from [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) eg: GBP|string|False|
||The total value of this transaction.|integer|False|
||The date that this value was set (to allow historical currency conversion). The date must be in ISO 8601 format (YYYY-MM-DD).|date-time|False|
||A description of this transaction.|string|False|
||The organisation identifier of the provider of transaction funds.|string|False|
||The organisation identifier of the recipient of transaction funds.|string|False|
||When information about this transaction was last updated.|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
||Identifier|string|False|
||When did this transaction take place? Please use YYYY-MM-DD format.|date-time|False|
||The currency used in amounts. The currency used in amounts. Use the three-letter currency code from [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) eg: GBP|string|False|
||The total value of this transaction.|integer|False|
||The date that this value was set (to allow historical currency conversion). The date must be in ISO 8601 format (YYYY-MM-DD).|date-time|False|
||A description of this transaction.|string|False|
||The organisation identifier of the provider of transaction funds.|string|False|
||The organisation identifier of the recipient of transaction funds.|string|False|
||When information about this transaction was last updated.|date-time|False|

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
|Funding Org:Last modified|-|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
|Funding Type:Vocabulary|A vocabulary used for this classification.|string|False|
|Funding Type:Code|A codelist value in the chosen vocabulary.|string|False|
|Funding Type:Title|The title of this classification.|string|False|
|Funding Type:Description|A description of this classification.|string|False|
|Funding Type:URL|A web link to more details of this classification.|uri|False|
|Funding Type:Last modified|-|date-time|False|

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
|Funding Org:Location:Last modified|The date when location information was last modified.|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
|Grant Programme:Code|An identifier for this grant programme.|string|False|
|Grant Programme:Title|The title of this grant programme.|string|False|
|Grant Programme:Description|A description of this grant programme.|string|False|
|Grant Programme:URL|A web link to more details of this grant programme.|uri|False|
|Grant Programme:Last modified|-|date-time|False|

|Title|Description|Type|Required|
|----|----|----|----|
|Identifier|The unique identifier for this grant. Made up of your 360Giving prefix, and an identifier from your records. See the [360Giving Grant identifier guidance](http://www.threesixtygiving.org/standard/identifiers/#toc-grant-identifier) for details.|string|True|
|Title|A title for this grant activity. This should be under 140 characters long.|string|True|
|Description|A short description of this grant activity.|string|True|
|Currency|The currency used in amounts. The currency used in amounts. Use the three-letter currency code from [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) eg: GBP|string|True|
|Amount Applied For|Total amount applied for in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the application transactions for this grant.|number|False|
|Amount Awarded|Total amount awarded in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the award transactions for this grant.|number|True|
|Amount Disbursed|Total amount disbursed (paid) to this grantee when this record was last updated (in numbers: do not include commas or currency symbols such as £)). If you have provided detailed transaction information on a separate table, this should equal the sum of all the disbursement transactions for this grant.|number|False|
|Award Date|When was the decision to award this grant made. Dates should be in YYYY-MM-DD format.|date-time|True|
|URL|A URL (Web Address) where further information about this grant can be found. This could point to the website of the recipient organisation, or might link to further details on the funders website.|uri|False|
|Planned Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
|Planned Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
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
|Last modified|The date when information on this grant was last updated|date-time|False|
|Data Source|A web link pointing to the source of this data. This may be an original 360Giving data file, a file from which the data was converted, or an organisation website.|uri|False|

|Title|Description|Type|Required|
|----|----|----|----|
|Planned Dates:Title|-|string|False|
|Planned Dates:Start Date|All events should have a start date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
|Planned Dates:End Date|Events or activities lasting more than one day should have either a duration (in months) or an end date. Dates should be in YYYY-MM-DD format. If the month or day are not available, these may be omitted.|date-time|False|
|Planned Dates:Duration (months)|Events or activities lasting more than one day should have either a duration (in months) or an end date.|string|False|
|Planned Dates:Description|-|string|False|
|Planned Dates:Last modified|-|date-time|False|

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
|Recipient Org:Last modified|-|date-time|False|

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
|Recipient Org:Location:Last modified|The date when location information was last modified.|date-time|False|


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

|Title|Name|Type|
|----|----|----|
|Identifier|id|string|
|Title|title|string|
|Description|description|string|
|Currency|currency|string|
|Amount Applied For|amountAppliedFor|number|
|Amount Awarded|amountAwarded|number|
|Amount Disbursed|amountDisbursed|number|
|Award Date|awardDate|date-time|
|URL|url|uri|
|Planned Dates:Start Date|plannedDates/0/startDate|date-time|
|Planned Dates:End Date|plannedDates/0/endDate|date-time|
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



## Extending the summary table
The default summary table template is defined by use of special ‘rollUp’ properties in the [underlying JSON Schema file](/wp-content/plugins/threesixty_docs/standard/schema/360-giving-schema.json). There is a [Flatten Tool](https://github.com/OpenDataServices/flatten-tool) that uses these properties when creating templates. However, it is possible, following the same naming convention for fields, to bring most properties into the Grants table if a particular use-case requires. 

For example, the structure:

* grants
  * relatedDocument
    * url

can by represented in the `Grants` table under the column name:

* ```relatedDocument/0/url``` 

or the column title

* ```Related Document:URL```

The naming convention for field names is to:

* If the relationship can be a one-to-many relationship, append ```/0``` to the relationship property name
* Concatenate the relationship and property names using /

The naming convention for field titles is to:

* Concatenate the relationship and property titles using a ```:```.

In the event that a value for a property is given in both a sub-table, and the summary table, flatten-tool will issue a warning if the values are not the same.

### JSON

When data is being generated directly out of a database system, publishers should consider using the JSON schema to provide a JSON file.

Developers may also wish to build their applications of JSON versions of the data. 

The [CoVE](http://cove.opendataservices.coop/360/) (Convert, Validate and Explore) tool supports round-tripping of data between Summary spreadsheet, multi-table datapackage and JSON representations. 


## Schema documentation

Identifiers are documented on the [identifiers](/identifiers/) pages.


