# Preparing DEI Extension data

## Overview of the steps

In order to publish DEI Data Standard data using the 360Giving Data Standard DEI Extension, you will need to do the following:

* Ensure that you have implemented DEI Data Standard in your grants process following the [guidance provided by the DEI Data Group](https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard).
* Decide whether to publish a spreadsheet or a JSON file. If you're an existing 360Giving publisher you will have already made this decision.
* Ensure the grant information linked to the DEI data you intend to publish meets the requirements of the 360Giving Data Standard.
* Add the appropriate fields, rows, and/or sheets required by the DEI Extension to your file

The following sections cover these steps in more detail, providing guidance for publishing data in [spreadsheet](#dei-extension-field-guidance) and [JSON file formats](#json-format-guidance-for-developers).

<div class="box box--teal">
    <h2 class="box__heading">Not sure what file format to use?</h2>
    <p>
      Read our <a href = "../../../guidance/prepare-data#choosing-your-file-format">guidance on choosing a file format</a>
       </p>
</div>



## DEI Extension field guidance

The data collected through the application of the DEI Data Standard can be complex because there are multiple questions that can be asked in a range of ways, and multiple answers can be provided in response to some questions.

The DEI Extension has been designed to be as straightforward as possible however it is more complicated than the commonly used parts of the 360Giving Data Standard.

```eval_rst
.. contents::
   :local:
   :depth:
```
### **DEI Details**

For publishers sharing data using spreadsheets, the DEI Extension data sits within the main **grants** sheet of the [360Giving Data Standard](../../technical/reference). All DEI Extension fields used in spreadsheets are prefixed with DEI Details, followed by the specific field name.

There are two fields which appear once for each grant record.

* **DEI Details:DEI Data Standard Version** is for declaring which version of the DEI Data Standard being used by the DEI data you have collected. This information can be found in DEI Data Standard documentation provided by the [DEI Data Group](https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard).
* **DEI Details:Purposes** is a free text field for describing why your organisation is collecting DEI Data Standard data.

There are seven other fields which appear under each of the application areas, Project, Mission and Leadership. 

* Four of these fields make use of **codelists**, which means that the values that can be included in those fields can only be taken from a specific codelist – **Asked Status**, **Reply Status**, **Available Options** and **Taxonomy Codes**.
* The remaining three fields are free text which means any text value can be included – **Additional Details, Lived Experience** and **Geography**.

#### Field list

This means that fully populated DEI Extension data will include 23 fields of information.

General fields
* DEI Details:DEI Data Standard Version
* DEI Details:Purposes

Fields which apply to Project
* DEI Details:Project:Asked Status
* DEI Details:Project:Reply Status
* DEI Details:Project:Available Options
* DEI Details:Project:Additional Details
* DEI Details:Project:DEI Response:Taxonomy Codes
* DEI Details:Project:DEI Response:Lived Experience
* DEI Details:Project:DEI Response:Geography

Fields which apply to Mission
* DEI Details:Mission:Asked Status
* DEI Details:Mission:Reply Status
* DEI Details:Mission:Available Options
* DEI Details:Mission:Additional Details
* DEI Details:Mission:DEI Response:Taxonomy Codes
* DEI Details:Mission:DEI Response:Lived Experience
* DEI Details:Mission:DEI Response:Geography

Fields which apply to Leadership
* DEI Details:Leadership:Asked Status
* DEI Details:Leadership:Reply Status
* DEI Details:Leadership:Available Options
* DEI Details:Leadership:Additional Details
* DEI Details:Leadership:DEI Response:Taxonomy Codes
* DEI Details:Leadership:DEI Response:Lived Experience
* DEI Details:Leadership:DEI Response:Geography

### **Required fields**

In the extension, including **DEI Details** fields is _optional_ for each grant. However, when any DEI Details field is included, the **Asked Status** field becomes required for each of the three areas: Project, Mission and Leadership.

For a publisher of data using the DEI Extension, this means that:

* If there is no DEI Data Standard information for the grant, you can omit the entire DEI Details set of fields.
* If there is DEI Data Standard information for the grant, you must include at least a value in **Asked Status** for each Project, Mission and Leadership. This requirement ensures a minimum level of context required for a user to interpret the data correctly.

### **Additional Details**

In addition to contextual information provided using codelist fields in Asked Status, Reply Status and Available Options fields, there is also a free text field for sharing **additional details**. This allows for providing extra context and explanation of the way data was collected not found elsewhere.

These are three free text fields available for the Project, Mission and Leadership Applications areas.

* DEI Details:Additional Details

### **Lived Experience and Geography fields**

In the DEI Data Standard approach, in addition to collecting responses using the taxonomy which classifies population groups, funders can include open questions for respondents to provide information about **Geographical/residential** context and other relevant **lived experience**. This allows for groups that don’t fall into the DEI Data Standard categories to provide responses where relevant.

These are three free text fields available for the Project, Mission and Leadership Applications areas.

* DEI Response:Lived Experience
* DEI Response:Geography

## Codelists

The extension includes several codelists to promote consistency and interoperability between datasets. These are all closed codelists, meaning only values from the codelists may be used in these fields.

### **What are codelists?**

Codelists are a list of values. Each value has three elements:

- a short name, which is designed for humans to read and understand
- a description, which explains to humans the meaning behind the code so that we can interpret it
- and the code, which is included in the data

If you have ever used a web form and selected a value from a drop-down list, this is very similar to how codelists function. They are a preset list of options to choose from.

The reason for using codes instead of names is because it avoids issues caused by typos, spaces or different cases. It also means the accompanying name and description can be amended or translated without the codes needing to be changed.

### **Codelists used in the DEI Extension**

There are four codelists available for use in the DEI Extension.

```eval_rst
.. contents::
   :local:
   :depth: 3
```

#### Asked Status

A codelist to declare whether DEI Data Standard questions were asked for this grant, and how.

There are four codes on this codelist which can be published in three fields:
* DEI Details:**Project**:Asked Status
* DEI Details:**Mission**:Asked Status
* DEI Details:**Leadership**:Asked Status

Each of these fields can only be included once with a single code per grant, which means you must pick one code to use.

There are two options for showing that the **questions were not asked** for the specific grant:

* The questions **were not applicable** (AS100). For example, this code would be used by funders asking questions about one or two of the application areas but not all three.
* The data is **historical** (AS101). This code would be used by funders on grants that were awarded (or where the data was collected) before the DEI Data Standard process was adopted.

For grants where the **questions were asked** there are two options:

* The questions were asked **during** the application process (AS200). This code would be used by funders asking for DEI Data Standard questions at any point before the decision to make the award was made. Whether the DEI questions are asked via a separate form or as part of the assessment process, you would still use this code.
* The questions were asked **after** the application process (AS201). This code would be used for any grants where the DEI questions were asked to grant recipients after the award decision.

```eval_rst
.. csv-table::
   :file: ../../extras/extensions/dei/codelists/askedStatus.csv
   :header-rows: 1
   :widths: auto
```

#### Available Options

A codelist to declare which answer options were available to the respondents.

There are seven codes in this codelist which can be published in three fields:

* DEI Details:**Project**:Available Options
* DEI Details:**Mission**:Available Options
* DEI Details:**Leadership**:Available Options

This field is an array which means multiple codes can be included in this field, separated by a semi-colon.

There are three codes which are used to show which taxonomy values were available for respondents: **Population Group**, **Category** and **Subcategory**. 

* Funders providing respondents with the option to select **Subcategory** values from the taxonomy, all three codes must be declared (AO100;AO101;AO102).
* Funders providing **Population Group** and **Category** values to select from should declare the two relevant codes (AO100;AO101).
* Funder providing only **Population Group** values to select from should only declare this code (AO100). 

There are also two codes to indicate if respondents were given the opportunity to provide a free text answer to share other **lived experience** not included in the taxonomy (AO201), or a free text answer related to **geography** (AO200).

There is a code to indicate if the respondents were able to state that their Project, Mission or Leadership are **general** not aimed at or consisting of a specific group (AO300).

Finally there is a code to indicate if respondents were given the option to answer ‘**Prefer not to say**’ (AO301).

It is possible that, depending on the range of options available to respondents, all seven codes could be included in this field (AO100;AO101;AO102;AO200;AO201;AO300;AO301).

```eval_rst
.. csv-table::
   :file: ../../extras/extensions/dei/codelists/availableOptions.csv
   :header-rows: 1
   :widths: auto
```

#### Reply Status

A codelist to declare whether a reply to DEI Data Standard questions was received or not.

There are five codes on this codelist which can be published in three fields:

* DEI Details:**Project**:Reply Status
* DEI Details:**Mission**:Reply Status
* DEI Details:**Leadership**:Reply Status

Each of these fields can only be included once with a single code per grant, which means you must pick one code to use.

* There is one code to indicate that there was **no reply** (RS100).
* The other four codes represent types of reply that were received:
  * the reply was **got** (RS200)
  * the reply was **general** (RS201)
  * the reply was **prefer not to say** (RS202)
  * there is **no permission** to publish the reply (RS203)

Note that the values declared in the Available Options are expected to align with the values declared in the Reply Status field for each application. If the codes **General** (AO300) and **Prefer Not To Say** (AO301) have been declared in the Available Options field, it will be possible to declare Reply Status codes **Reply was General** (RS201) or **Reply was Prefer not to say** (RS202) when appropriate. However, if these were not declared as being available options, it is expected that the range of valid responses in the Reply Status field would be either **No Reply** (RS100), **Reply Got** (RS200) or **Reply Got but no permissions** (RS203).

```eval_rst
.. csv-table::
   :file: ../../extras/extensions/dei/codelists/replyStatus.csv
   :header-rows: 1
   :widths: auto
```

#### Taxonomy Codes

The Taxonomy Codes selected from the DEI Taxonomies. The value for these codes should be drawn from the Taxonomy Codes codelist. 

There are 73 codes on this codelist which can be published in three fields:

* DEI Details:**Project**:DEI Response:Taxonomy Codes
* DEI Details:**Mission**:DEI Response:Taxonomy Codes
* DEI Details:**Leadership**:DEI Response:Taxonomy Codes

This field is an array which means multiple codes can be included in this field, separated by a semi-colon.

These fields are used to provide the answers provided by organisations in response to DEI Data Standard questions.

Note that the DEI Data Standard criteria for each application area require that a population group be represented by a majority of the project/service users or the leadership of an organisation. This means that responses may be taken from multiple different population groups but it is not possible for there to be multiple categories or sub-categories answers taken from the same population group.

``` eval_rst
.. admonition:: \

 For further guidance on the criteria and definitions for each application area see the DEI Data Standard documentation on the `DEI Data Standard section of the Funders Collaborative Hub`_.

.. _DEI Data Standard section of the Funders Collaborative Hub: https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard
```

```eval_rst
.. csv-table::
   :file: ../../extras/extensions/dei/codelists/taxonomyCodes.csv
   :header-rows: 1
   :widths: auto
```

## How to include DEI Extension data in a 360Giving data file

A key step to using the DEI Extension is declaring that you are using it in a **Meta sheet** included in your file. 

This Meta sheet is the way 360Giving data publishers include metadata about their grants data in their files. It is separate and different from the metadata fields in the DEI Extension itself which are usually included in the main grants sheet. For further information read our guidance on 360Giving Data Standard [Metadata](../../../technical/metadata/#guide-to-including-metadata-in-spreadsheet-files).

It is only once you have declared that you are using the DEI Extension in the Meta sheet that your data can be checked and validated by the 360Giving [Data Quality Tool](https://dataquality.threesixtygiving.org/) and used by GrantNav and 360Insights. If you miss this crucial step, the Data Quality Tool will not recognise the fields for the DEI Extension and treat them as non-Standard [Additional Fields](../../../technical/reference/#additional-fields).

Once you have a Meta sheet in your file, you can declare the extension by adding the Metadata field with the title \`Extensions\`. Usually this is in column A. In the next column (usually column B), add the value **dei**

You should also fill in the Version, which should be **1.4** or higher, as extensions were not available before version 1.4 of 360Giving Data Standard.

We recommend adding other useful pieces of metadata to your file, following the [Metadata guidance](../../../technical/metadata/#guide-to-including-metadata-in-spreadsheet-files) provided.

## Spreadsheet templates

A <a href="../../../_static/360-giving-schema-titles-with-dei-extension-2024.xlsx">blank spreadsheet template</a> including all 360Giving Data Standard fields and a sheet including DEI Extension fields is available for download for reference.

360Giving is developing a DEI Extension mapping template to make it easier for publishers to select the correct metadata values appropriate for their implementation of the DEI Data Standard, and support adding the appropriate Taxonomy codes that must be used.

Please contact 360Giving Helpdesk to find out about more tailored templates and guidance for your organisation via <support@threesixtygiving.org> putting **DEI template** in the email subject line.

## JSON Format Guidance for Developers

The 360Giving Data Standard is defined by a JSON Schema, which details the entities that can be described using the Standard, and the properties it recognises. The DEI Extension, which is also defined by a JSON Schema, is an optional extension designed to be added to the [360Giving JSON Schema](../../../technical/reference/#json-format), and makes use of 360Giving’s extension mechanism to allow you to validate the fields and codes used in your data.

The normative reference for the fields and codes added by the DEI Extension JSON Schema can be found alongside documentation in the [Technical Reference](../reference) section.

It is straightforward to implement the DEI Extension into an existing JSON format file of 360Giving data:

1. Ensure that the **version** field in your package data has a value greater than **1.4**, since extensions were not available prior to this.

    If you're updating an existing publication and your current version is **1.0** or greater, you can declare **1.4** without any problems related to backwards incompatibility (see also: our [Versioning and Upgrade Process](../../../about/governance/#versioning-and-upgrade-process)). 

    If you don’t have a **version** field currently, it is safe to add this with the value of **1.4** unless your data isn’t conformant to Version **1.0** or later. You can verify this by checking the 360Giving Data Standard data in your file in the [Data Quality Tool (DQT)](https://dataquality.threesixtygiving.org/), as all data that passes the tool’s validation checks is conformant with Version 1.0 or later.

2. Create the **extensions** field in your package data if you have not already done so, and add the string **dei**. This declares the extension to tooling such as the Data Quality Tool so you can validate the contents of the extension fields.
3. For each grant that will contain DEI information, add a **grants.deiDetails** property.

    1. When a grant has a **deiDetails** property, **deiDetails.leadership**, **deiDetails.mission**, and **deiDetails.project** become required for that grant.
    2. For each **deiDetails.leadership**, **deiDetails.mission**, and **deiDetails.project**; the **askedStatus** property is required. Values for **askedStatus** must draw from the Asked Status codelist.
    3. Each other property is optional, but should be filled out in accordance with the DEIApplicationArea and DEIResponse object schemas when present.


## Support Available

360Giving Helpdesk provides pro-bono support to help funders navigate the steps to publish DEI Data Standard data alongside their 360Giving grant data.

Visit our website to find out [ways to get support with publishing](https://www.threesixtygiving.org/publishing/). It is recommended to book a [publisher 1-1 support call](https://www.threesixtygiving.org/support/1-1-publisher-support/) to discuss your plans to prepare and publish DEI data alongside 360Giving data, making sure to mention that you would like to discuss DEI data preparation in the booking form.
