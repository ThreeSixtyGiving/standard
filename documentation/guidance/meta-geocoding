# Metadata: making your data more usable
The 360Giving Data Standard allows funders to describe information about their grants, and provide information about the organisations and programmes related to these awards.

It is also possible to publish data about the data itself. This is called **metadata**.

## About metadata
Metadata is data about the data, such as the size of a file, how many grants it contains and when it was published. Metadata is important to help understand more about the data and how it might be useful in a particular case.

There are two main types of metadata:
- **Authoritative metadata**: This is what the file declares about itself, such as who the publisher is, or where the file can be found.
- **Derived metadata**: This is what can be found out from a file, such as the total value of the grants, or which fields from the 360Giving Data Standard are used. This type of data is not included in the information you publish but instead it will be calculated by tools that use your file, such as the <a href="https://data.threesixtygiving.org/" target="_blank">360Giving Data Registry.</a> 

## Including metadata in your 360Giving file
The metadata fields in the 360Giving Data Standard allow for the publication of authoritative metadata. This is information you provide to help users understand your data better.

For publishers sharing their data in JSON file format, the metadata is included in the Package Schema. See our guidance on [the Package schema](https://standard.threesixtygiving.org/en/new-docs-style/reference/#giving-json-schemas) for further details.

For publishers sharing their data in spreadsheet file format, the metadata fields are included in a special Metadata sheet. This means your file would have one sheet for the grant data and one for the metadata.

Including metadata allows you as the publisher to ensure key information is provided to the users of your data. It is especially useful if you need to provide additional context or add disclaimers about your organisation or the grant data in the file. 

As with the main 360Giving Data Standard, alongside the official fields is it possible to include additional information.

See our full [guidance on metadata](https://standard.threesixtygiving.org/en/new-docs-style/metadata/) for further details.

# Converting Postcodes into Geocodes to anonymise address information
Converting postcode data into geocodes protects the privacy of recipients while allowing you to include useful data that will allow your grants to be geolocated. The practical process may vary depending on the process you use for preparing your 360Giving data and the volume of data.

Geocodes can be found using the <a href="https://findthatpostcode.uk/" target="_blank">Find that Postcode website.</a>

Firstly, use the search on the homepage. You can enter a postcode and get details of the full range of geocodes associated with that location, for example these are the results for the <a href="https://findthatpostcode.uk/postcodes/N1%209AG.html" target="_blank">London postcode N1 9AG</a>. 

You should then decide which type of geocode to include in your data. 
- Some publishers use either **Local Authority** or **Ward** areas for recipient location, as these types of geocodes work with <a href="https://help.grantnav.threesixtygiving.org/en/latest/#location_data" target="_blank">GrantNav’s location filtering functions.</a> 
- Place-based funders, such as community foundations, often use smaller areas such as the **Lower Super Output Area**, to provide information about the grant location.

If you’re preparing a small number of grants at a time then manually searching to get the relevant codes and adding these into your data at the data preparation stage could be a straightforward approach.

## Using Postcode to Geocode lookup tool
Find that Postcode has a <a href="https://findthatpostcode.uk/addtocsv/" target="_blank">'Add fields to CSV'</a> service which means you can upload a list of postcodes into the tool and then download a file with all the geodata you’ve chosen to use.

If you have a batch of postcodes to convert to geocodes, the practical steps might involve: 

1. Prepare your 360Giving data including a column with the relevant postcode data.
2. If using Excel, convert this file into CSV format. See this guidance for further details of <a href="https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba" target="_blank">how to convert a file between Excel Workbook and CSV.</a>
3. Upload this file into the 'Add fields to CSV' service at <a href="https://findthatpostcode.uk/addtocsv/" target="_blank">https://findthatpostcode.uk/addtocsv/</a>
4. Select your preferred geocode types.
5. Click 'Add data to CSV'. The tool will automatically download an updated version of your file with geocodes included.
6. Delete the column of postcode data from this version of the file.
7. Rename the new columns to match the 360Giving Data Standard. For example if using Ward codes the headings should be renamed as follows:
  - Ward Code = Recipient Org:Location:Geographic Code
  - Ward Name = Recipient Org:Location:Name
8. Re-save as Excel file (xlsx file format).

<div class="box box--teal">
    <h3 class="box__heading">Getting further help</h3>
    <p>If you can't find the information you need or you have further questions please email <a href="mailto:support@threesixtygiving.org">360Giving Helpdesk</a> or fill out our <a href="https://docs.google.com/document/d/1LitLsFnMRXRZKXeEZqw8Dw1tbR9AMDpHj0446y8l6WY/edit?usp=sharing" target="_blank">feedback form</a>.</p>
</div>
