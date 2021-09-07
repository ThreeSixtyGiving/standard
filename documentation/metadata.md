# 360Giving guide to metadata
The 360Giving Data Standard allows funders to describe information about their grants, and provide information about the related organisations, programmes and activities.

It is also possible to publish data about the data itself, called metadata.

This guide explains what metadata is, why it is useful and how you can add metadata to new or existing 360Giving data files.

## What is Metadata?
Metadata is data about the data, such as the size of a file, how many grants it contains and when it was published. Metadata is useful to both people and computers, and helps them to build a picture of the contents of a dataset to understand whether it might be useful in a particular case, and how to use it.

There are two main types of metadata:
- **Authoritative metadata**: This is what the file declares about itself, such as who the publisher is, or where the file can be found.
- **Derived metadata**: This is what can be found out from a file, such as the total value of the grants, or which fields from the 360Giving Data Standard are used. This type of data is not included in the information that is published, instead it can be calculated by tools that use a file, such as the 360Giving Data Registry. 

## Why include metadata in 360Giving files?
Including metadata is one of the features of good quality open data.

360Giving Data Standard enables publication of **authoritative** metadata, which is information you can provide to help users to understand your data better.

This means you can:
- Provide additional information about your organisation or the grants data in the file
- Include links to further guidance
- Include details about how the data is openly licensed

As the metadata is included in the file itself, it means relevant information is provided directly to users of the data, so that the grants and their context can be understood together.

Including metadata in the 360Giving Data Standard means we are better able to serve the needs of publishers and data users.

### Including metadata in JSON files
For publishers sharing their data in JSON file format, the metadata is declared using the fields of the Package Schema (except for 'grants' which is a list of grant data). See our guidance on the Package schema for further details.

### Publishers using CSV (.csv) files
Currently it is not possible to include a Meta in CSV files. This is because the file format does not allow for separate sheets within the same file. Please contact 360Giving Helpdesk if you use CSV file format to publish 360Giving data and want to include metadata.
 
### Including metadata in spreadsheet files
For publishers sharing data in spreadsheets, the metadata fields are included in a Meta sheet. This means your file would have a sheet for the grant data and one for the metadata.

If you are publishing using Excel or OpenDocument formatted spreadsheets you can add the Meta tab to your data by following these steps:
1. Add a new sheet to the spreadsheet and rename it Meta.

Note that it is important to name the sheet accurately to ensure that the data is recognised by 360Giving tools as metadata.

2. In the first column (usually ‘A’) put the names of the metadata fields you wish to include.

You can find the names by looking at the Meta sheet Table.

3. In the second column (usually ‘B’) you should fill out these with the appropriate values.

Some fields require different types of values such as URLs or dates. The information about data format is also provided in the Meta sheet Table.

4. Once you have filled out the details you can check whether the formatting is correct by uploading the file into the Data Quality Tool. Follow the feedback to make any changes needed to the metadata before publishing the file.

If the Meta sheet is not named correctly the Data Quality Tool will not recognise the metadata and give error messages.

5. Publish the file how you normally do.
 
### Metadata Templates
There is a version of the 360Giving Spreadsheet Template which includes the Meta sheet.

## Field guidance
This guidance provides further information about the fields in Meta sheet and the kind of data that is expected or appropriate for each.

**Version**

This is for the version of the 360Giving Data Standard being used, so not the version of the file that is being published. For example the version that introduced metadata into the 360Giving Data Standard is 1.1.
Find the details of the current version in the Releases changelog 

**Title and Description**

These are text fields that can be used to provide information about the name of the file and its contents, and provide further contextual information is appropriate.

**Issued**

This is the date the file was first published. This means the date should remain the same even if the contents of the file are changed. This must be a full date in YYYY-MM-DD or date-time format. 

**Modified**

This is the date when the file was last modified. This means the date should be updated each time the contents of the file are changed. This is important because if a user has several copies of the file, an accurate Modified date will quickly tell them which is the most recent one.

This must be a full date in date-time format. See the Dates and Times section for further guidance on date and date-time formats.

**Identifier**

This is a unique identifier for the file. This can be 

**Publisher:Identifier and Publisher:Name**

The Publisher identifier is a globally unique identifier for this organisation. The Organisation Identifier Standard guidance explains how to create this Org ID. 

If the publisher is also the funding organisation described in the 360Giving grant data, the Org ID used will be the same.

**Publisher:Website and Publisher:Logo**

These are links to a relevant website and where a logo can be viewed. 

All website links must start with http:// or https:// to be recognised as a valid URI. For example example.com is incorrect but http://example.com is valid.

**Download URL and Access URL**

These are links to where the data can be downloaded and webpage where the data can be found.

If it is not possible to know this information before the data is published, these fields can be left blank.

**License**

This is the canonical URI of the license that applies to the data in the file or package. This should be a Public Domain Dedication or Open Definition Conformant license. For further details see the 360Giving guide to open licensing.

### How to handle blank fields

The inclusion of metadata in 360Giving data is recommended but optional, and all of the fields in the Meta sheet themselves are optional. This means if they are not being used they should be either left blank or removed from the Meta sheet. 
Only the relevant information using the correct data formatting should be included in Metadata fields. Do not fill blank fields with dashes, N/A or other content as it will cause errors. 

### How to include additional information in Meta sheet
In both the 360Giving Data Standard and Meta sheet, alongside the official fields is it possible to include additional information.

This could be contact information, disclaimer text or anything else you want users to know about your data.

Be aware to avoid special characters in the field names and use appropriate data formats. See guidance on adding Additional fields for further details of what to consider when adding your own fields.

As well as adding extra fields of data to the Meta sheet it is also possible to include more extensive information in extra sheets. This is done by including ‘Hash Comments’ in the file which tell 360Giving tools to ignore the contents when processing the file.

These ‘Hash Comments’ should be placed in the first row of the sheet and also in front of the sheet name. For further guidance on how to use Hash Comments’ in your 360Giving file contact 360Giving Helpdesk.

### Making updates to metadata
Some 360Giving data files are published and remain unchanged from that date. However, many publishers share files that are updated to add new grants data on a regular basis and in some cases to make amendments to information that has already been published.

Similarly the metadata originally published in a file may need to be updated if and when the contents of the data changes.

The contents of some fields are expected to remain unchanged even when the grant data is updated or changed. These are the publisher details, issue date, file identifier and license.

The contents of other fields are expected to be more dynamic. The Modified date should be updated each time the file contents are changed, to provide users with an accurate understanding of when changes have happened.

The title and description of files may change as the contents are updated. If the urls to the file and access page change over time, these fields should also be updated to point to the right locations.

Maintaining accurate and up to date metadata is as important as the accuracy of the 360Giving data.

### Other ways to include metadata in 360Giving data
As well as being able to include metadata using the Meta sheet, there are also two fields in the main 360Giving Data Standard intended for sharing of metadata, alongside the grant information.

**Last Modified**

This is to indicate when the information about a grant was last updated. This is often generated automatically by the software managing or exporting this data, however it can also be used to show when the data in the file was last changed.

**Data Source**

This is a web link pointing to the source of this data, which can be the 360Giving data file, a file from which the data was converted, or an organisation website.

### Get more help with Metadata

Contact 360Giving support for further guidance on including Metadata in your 360Giving data.
