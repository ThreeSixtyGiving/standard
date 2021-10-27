# Prepare and format your grant data
<div class="box box--teal">
    <h3 class="box__heading">Key tasks</h3>
    <p><ol>
      <li>Decide whether to publish using spreadsheet or JSON file format.</li>
      <li>Prepare your data.</li>
      <li>Check that this file passes the tests in the Data Quality Tool, so that it is compatible with other 360Giving data.</li>
      </ol></p></div>

By the end of this stage you will have prepared your grant data ready for publishing, and have tested that the file is formatted correctly in the 360Giving Data Quality tool. How you prepare your data will be influenced by how you collect and store information about your grants.

For many publishers preparing data is a manual process which involves exporting data from a grants management system and converting it into a spreadsheet. However, some grants management systems have some or all of the steps needed to convert the information into 360Giving data built-in to the system. 

## Register to become a 360Giving data publisher
Once you have decided to publish your grants data, please let us know by emailing the 360Giving Helpdesk: <support@threesixtygiving.org>. 

You will be provided with a 360Giving Publisher prefix, which identifies your organisation and will be used in your 360Giving data to provide a unique identifier for each grant.

See our guidance for further details about [grant Identifiers.](https://standard.threesixtygiving.org/en/new-docs-style/identifiers/#identifiers)

360Giving Helpdesk can also answer your questions and provide guidance on your next steps.

## Publishing using spreadsheets
### Spreadsheet format
Spreadsheets are the most common way for publishers to share their data – the majority of 360Giving data files are spreadsheets. Acceptable file formats are CSV (.csv), Excel Workbook (.xlsx) or Open Document (.ods). Is it not possible to publish in older Excel file formats (.xls).

You do not need specialist technical knowledge or specialist software to use spreadsheet file formats to publish. 

#### Publishing without a grants management system
There are 360Giving publishers without a database or grants management system who collect their grants information in simple spreadsheets. The steps to prepare your data will be similar to most other publishers.

However if you don’t currently collect information about your grants, you will need to start gathering that data in order to publish it using the 360Giving Data Standard. 

Depending on what range of information you want to start collecting, you can set up your own spreadsheet, fill out an adapted version of the 360Giving Spreadsheet Template or collect your data in a 360Giving Conversion Tool template. For further details see the options for publishing using a spreadsheet section [below.](https://standard.threesixtygiving.org/en/new-docs-style/prepare-data/#options-for-publishing-using-a-spreadsheet)

#### Publishing with a grants management system
If you use a grants management system provided by a software company it is unlikely that you will be able to build in 360Giving publishing into the system itself. However you should be able to set up and save a report to export the source information for your 360Giving data and convert it into the right formats in a spreadsheet.

Funders using a range of proprietary grants management systems have shared 360Giving data, including:
- Blackbaud Grantmaking
- Flexi-grant
- Benefactor
- CC Grant Tracker
- SmartSimple

#### Options for publishing using a spreadsheet
For most publishers, whether you are using grants management software or you hold your grants data in spreadsheets, the practical steps to get your data ready will be similar and involve making changes to the data in the file.

- You can start with an empty file and construct the column titles by referring to the 360Giving Data Standard documentation. 
- You can also use the ‘360Giving Spreadsheet Template’ and adapt this to your needs.
- Another method that is used by many publishers is to configure and use a 360Giving Data Conversion Tool Template.

#### Using the 360Giving Spreadsheet Template
This multi-sheet spreadsheet template consists of all the fields in the 360Giving Data Standard. 

There is a main ‘grants’ sheet which includes the 10 core fields and other common data fields. Additional sheets allow for the sharing of further information. 

You can download the 360Giving Spreadsheet Template [here.](https://standard.threesixtygiving.org/en/latest/reference/#spreadsheet-format)

#### Making changes to the 360Giving Spreadsheet Template
You can adapt the template to suit your needs and make changes to:
- Remove non-required columns that you are not using.
- Reorder the columns so that information is arranged in the way you want.
- Move columns in the template between sheets.
- Add extra columns to include information you want to share that is not covered by the 360Giving Data Standard fields. See our guidance on Additional fields for further details.

However, all the columns in your adapted template must use the correct headings and data formatting to ensure your data conforms to the 360Giving Data Standard. It must also include all of the 10 core fields

#### Filling out the template
The 10 core fields must be filled in so that there is no missing information. 

For all other columns, if information is not available the field should be left blank. Do not use dashes (-) zeros (0) or N/A to fill in blank fields as this will make your data harder to use.

#### Working with more complex information
The majority of publishers using spreadsheets will detail all the information about each grant on one row of a spreadsheet. 

However it is possible to include more complexly structured data if needed. For example if a single grant has multiple beneficiary locations, it is possible to represent this by creating ‘One to many relationships’.

See our guidance for further information about [One to many relationships.](https://standard.threesixtygiving.org/en/new-docs-style/reference/#one-to-many-relationships)

#### 360Giving Conversion Tool Template
A 360Giving Conversion Tool is an Excel file designed to make the technical steps of formatting grant information into 360Giving data more straightforward. The tool can be set up to work with the range of data you choose to share with support from the 360Giving Helpdesk. 

#### About the 360Giving Conversion Tool Template
Although each tool is tailored to each funders’ data and needs, they are all set up in the same way.  

The spreadsheet has three sheets:
- **source_data**
This sheet is for the grant information that needs to be formatted as 360Giving data. The source data is copied and pasted from a file exported from your grants management system or an existing file that holds your data.

- **fixed_data**
This sheet is for the ‘fixed’ information that is needed to create your 360Giving data. These are unlikely to be in your source data, such as the currency, your own organisation name, organisation identifier and Publisher prefix – eg 360G-ExampleFunder.

- **360_data**
In the top row of this sheet are the 360Giving headers that align with the data you intend to publish.
From the second row down, there are a range of formulas which combine the source data and fixed data from the first two sheets to create 360Giving formatted data. 

Any changes in content of the data in the **source_data** or **fixed_data** sheets will automatically be picked up in the 360_data sheet.

The tool is colour coded so the **10 core fields** in the 360Giving Data Standard are green, and the **recommended** fields are yellow.

#### How the formulas work
The formulas in the 360_data sheet perform one or more of these actions to convert the data.

- Map the source data to the appropriate 360Giving header leaving the content unchanged.
- Change the format of the data. For example changing the date from 27/08/2021 to 2021-08-27 which is the date format required by the 360Giving Data Standard.
- Combine data. 

For example to create an **Identifier** which is a unique grant ID from your system with your publisher prefix.

**Recipient Org:Identifier** are also created using a formula which provides the correct prefix depending on whether there is charity, company or other type of register number available. If there is no register number, the formula can instead create an organisation identifier using a unique ID for the recipient from your system or the recipient organisation name. 

See our guidance for further details about [Organisation Identifiers.](https://standard.threesixtygiving.org/en/new-docs-style/identifiers/#organisation-identifier)

For further guidance about setting up and using a conversion tool, please contact the 360Giving Helpdesk via <support@threesixtygiving.org>.

### Building 360Giving publishing into grants management systems
If you use Salesforce as a grants management system, it is possible to build-in 360Giving publishing. Many funding organisations who use Salesforce have set up their system to make sharing 360Giving data more straightforward.

It can be possible to build-in 360Giving publishing into other types of configurable CRM systems - such as Microsoft Dynamics - so please contact the 360Giving Helpdesk via <support@threesixtygiving.org> to find out what might be possible in your situation. 

#### Publishing using JSON format
JSON format is used for exporting the data directly from a grants management system or database, using the 360Giving JSON schemas. Some specialist technical knowledge is needed to use JSON to publish 360Giving data.

Check the technical documentation for further details and look at examples of JSON files available via the 360Giving Data Registry. Please note that using JSON format involves publishing the data in a JSON file; there is no API. 

If you decide to use the JSON file format to publish your data you will likely need support from a developer to set this up. Contact the 360Giving Helpdesk via <support@threesixtygiving.org> to discuss your next steps for using JSON as your publishing format. 

#### Setting up Salesforce for 360Giving data publishing
Some Salesforce grantmaking systems that are managed by consultants and have basic 360Giving data exporting functions built-in, so check with your Salesforce administrator or technical support provider to find out if this is the case for your organisation. Even with this built-in functionality there will be extra steps to customise your system to allow you to export the full range of fields you have decided to publish.

If you manage your own Salesforce system, you can either get support from a Salesforce consultant or set up a custom 360Giving report yourself. 360Giving has step-by-step guidance on how to set up a custom 360Giving report and can provide practical assistance to help you configure your system. 

Contact the 360Giving Helpdesk via <support@threesixtygiving.org> to discuss your options for setting up your Salesforce grants management system for 360Giving publishing.

#### Guidance for community foundations using Digits2 Salesforce system
If you are a community foundation using the Digits2 grants management system, please refer to our special guidance about the built-in 360Giving data extract to publishing 360Giving data <a href="https://threesixtygiving.org/communityfoundations/cf-publishing-guide" target="_blank">here.</a>

The guide includes a video walk-through and instructions on how to export 360Giving-formatted data from your Digits2 system. The step-by-step instructions for using the extract tool are also available to download in a PDF version.

Each community foundation needs to be set up with access to this 360Giving data extract. If you cannot find the 360Giving report folder or 360Giving export tool in your Digits2 system, please contact the 360Giving Helpdesk via <support@threesixtygiving.org> to request this to be set up. 

<div class="box box--teal">
    <h3 class="box__heading">Getting further help</h3>
    <p>If you can't find the information you need or you have further questions please email <a href="mailto:support@threesixtygiving.org">360Giving Helpdesk</a> or fill out our <a href="https://docs.google.com/document/d/1LitLsFnMRXRZKXeEZqw8Dw1tbR9AMDpHj0446y8l6WY/edit?usp=sharing" target="_blank">feedback form</a>.</p>
</div>
