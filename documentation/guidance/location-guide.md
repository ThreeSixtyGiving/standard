# 360Giving guide to location data

## Why is location data important?
Location data helps users to understand where organisations are based or activities are happening, which helps to build a more complete picture of where funding is going geographically.

Finding out where in the UK grants go is a key question that 360Giving data can be used to answer, but this is only possible when good quality and consistent location data - also known as geodata - is shared. 

Location is not one of the [ten core fields](decide-what-information-to-share), so the 360Giving Data Standard does not require geodata to be included. However, location information is so useful that we do recommend including it whenever possible. When data also includes geographic codes, it makes the data more comparable, and allows the data to be visualised in maps or analysed alongside other datasets.

## The basics
The 360Giving Data Standard includes a range of ways to describe locations which are split into three types of fields: recipient, funder and beneficiary location. 

- **Recipient location** is where the recipient of a grant is based.
- **Funder location** is where the funder of a grant is based.
- **Beneficiary location** is where the funded work is being delivered or the people who access the funded work are based. 

Recipient, funder and beneficiary locations can be shared in the form of place names and geographic codes. Recipient and funder locations can also be shared in the form of an address.

### About geographic codes
A geographic code, or geocode, is a unique identifier that represents a location or geographic object. These geocodes allow geographic entities to be distinguished from each other and provide a more consistent way to identify a place than using the location name.

Geocodes are useful in the same way as other [identifiers](../technical/identifiers) in the 360Giving Data Standard. Whilst a person may be good at recognising that “Royal Borough of Kingston upon Thames”, “Kingston” and “London Borough of Kingston” refer to the same place, computers cannot make this connection unless a unique identifier in the form of a geocode is provided.

Geocodes can be used to produce maps showing the distribution of funding geographically and allow grants data to be analysed alongside official statistics, such as the <a href="https://en.wikipedia.org/wiki/Multiple_deprivation_index" target="_blank">Indices of multiple deprivation.</a>

Whenever possible, geocodes should be shared by funders publishing on 360Giving with the name of the area and geocode type.

**Types of geographic codes**

**Country codes** - two-letter country codes taken from <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO_3166-1_alpha-2.</a> For example the code for the United Kingdom is **GB**, the code for Spain is **ES**.

**ONS codes** - nine character codes managed by the <a href="https://en.wikipedia.org/wiki/ONS_coding_system" target="_blank">Office for National Statistics</a> which describe a wide range of geographical areas in the UK - including the four nations of the UK, regions in England, local authority areas, electoral wards and <a href="https://www.ons.gov.uk/methodology/geography/ukgeographies/censusgeography#output-area-oa" target="_blank">Census output areas.</a> 

**Postal Codes** - full or partial postal codes associated with a UK postal address, or the equivalent codes used in other countries.

**Latitude and Longitude** - coordinates that indicate a point on the globe, using the <a href="https://en.wikipedia.org/wiki/World_Geodetic_System" target="_blank">World Geodetic System.</a>

## Recipient organisation location
**Recipient location** fields indicate where the grant recipient is based. It could be the location of a main office or branch, whatever is most appropriate for the grant. 

Many funders collect address information from applicants during the grants management process, which makes including recipient location information straightforward. Over <a href="https://qualitydashboard.threesixtygiving.org/alldata" target="_blank">two-thirds of organisations</a> sharing 360Giving data include this type of information.

### Address fields
There are fields which allow for the full postal address of an organisation to be published. However providing the city or town name and a postcode is sufficient to make the data useful.

Publishing street addresses is not recommended because it does not add to the usefulness of the data and omitting these details helps to avoid privacy issues if a recipient organisation is registered at a home address or if an organisation is supporting vulnerable people (for example, a refuge).

View the full range of available <https://standard.threesixtygiving.org/en/latest/technical/reference/#recipient-org" target="_blank">recipient organiation address fields.</a> 

**Considering privacy**

In populated areas a postcode is unlikely to identify a specific building, but in rural or less built-up areas, a postcode could be linked to a small number of addresses.

When sharing data about grants awarded to individuals - or small and informal charities or groups whose address may be a home address - it is not appropriate to share any address or postcode data directly.

In these cases, the location information should be converted from postcodes into geocodes prior to publishing the data.

See our guidance on [converting postcodes into geocodes](converting-postcodes-into-geocodes-to-anonymise-address-information) for further information, and here is our [guidance on data protection](../guidance/data-protection/) for further considerations about privacy and location data.

### Recipient location codes
In cases when it isn’t possible or appropriate to publish postal codes, it is possible to publish recipient location in the form of Office for National Statistics (ONS) geocodes.

When 360Giving data includes recipient location codes at **Local Authority** or **Ward** level, these will work with the <a href="https://help.grantnav.threesixtygiving.org/en/latest/locations.html" target="_blank">location filtering functions</a> of GrantNav, 360Giving’s search engine for grants data.

The fields used to share recipient location geocodes should be accompanied by fields for the location name and geocode type whenever possible.

<div class="table table--zebra">
    <table>
        <thead>
            <th>Field name</th>
            <th>Description</th>
            <th>Example value</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Field name">Recipient Org:Location:Name</td>
                <td data-header="Description">A name for this location.</td>
                <td data-header="Example value">Barrow-in-Furness</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Field name">Recipient Org:Location:Geographic Code</td>
                <td data-header="Description">A code referring to a geographical area, drawn from an established gazetteer such as the <a href="https://en.wikipedia.org/wiki/ONS_coding_system" target="_blank">ONS Register of Geographic Codes</a> in the UK. For example, the code for a local authority ward, or parliamentary constituency.</td>
                <td data-header="Example value">E07000027</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Field name">Recipient Org:Location:Geographic Code Type</td>
                <td data-header="Description">The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the codelist of <https://github.com/ThreeSixtyGiving/standard/blob/master/codelists/geoCodeType.csv" target="_blank">geographic code types.</a></td>
                <td data-header="Example value">NMD</td>
                </td>
            </tr>
        </tbody>
    </table>
</div>

View the full range of available <https://standard.threesixtygiving.org/en/latest/technical/reference/#recipient-org-location" target="_blank">recipient location fields.</a> 

## Beneficiary location
**Beneficiary location** fields are used to describe where the funded work is being delivered or where the people who will access the service or activity are based. 

These fields can also be used to describe the geographical scope of a grant programme or funder’s area of operation.

### Why is beneficiary location data useful?
Including beneficiary location can provide a more accurate picture of where grants are going geographically, as these fields focus on where the impact of the funding is being directed.

Beneficiary location is especially important in cases where the recipient location is in a different place from the activity being funded. This is common for grants awarded to larger regional or national organisations with head offices based in major cities that deliver services in different places around the country.
                  
**Beneficiary location names**
                  
The location names could describe any type and size of place; an estate, ward, town or city, local government area, parliamentary constituency, region or country. These values should be relevant to the scope of the grant or funded activity. 

Including the **location name** allows users to understand which places funding is reaching.

**Using location names consistently**
                  
Ensuring location names are consistent within your own data will make the information clearer and more usable, especially if it is not possible to also publish geocodes alongside the names.

For example, avoid having "Bristol, City of" and "City of Bristol" and “Bristol" or "Tyne & Wear" and "Tyne and Wear" in the same data. 

Also avoid using ambiguous terms such as ‘National’ which in a UK context could be interpreted as meaning any of the four nations or UK-wide. Use the specific country name - England, Scotland, Northern Ireland or Wales, or the term UK-wide to ensure users can interpret your grant data correctly.

**Beneficiary location geocodes**

Including geocodes that correspond with the beneficiary location names increases the usability of the data by providing a consistent way to identify these places, which make the data comparable across different funders. 

Data with geocodes can be used to produce maps showing the geographic distribution of funding and allow grants data to be linked with other data sources, such as official statistics.

The fields used to share beneficiary location geocodes should be accompanied by fields for the location name and geocode type whenever possible.

<div class="table table--zebra">
    <table>
        <thead>
            <th>Field name</th>
            <th>Description</th>
            <th>Example value</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Field name">Beneficiary Location:Name</td>
                <td data-header="Description">A name for this location.</td>
                <td data-header="Example value">Barrow-in-Furness</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Field name">Beneficiary Location:Geographic Code</td>
                <td data-header="Description">A code referring to a geographical area, drawn from an established gazetteer such as the <a href="https://en.wikipedia.org/wiki/ONS_coding_system" target="_blank">ONS Register of Geographic Codes</a> in the UK. For example, the code for a local authority ward, or parliamentary constituency.</td>
                <td data-header="Example value">E07000027</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Field name">Beneficiary Location:Geographic Code Type</td>
                <td data-header="Description">The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the codelist of <https://github.com/ThreeSixtyGiving/standard/blob/master/codelists/geoCodeType.csv" target="_blank">geographic code types.</a></td>
                <td data-header="Example value">NMD</td>
                </td>
            </tr>
        </tbody>
    </table>
</div>
                  
View the full range of available <https://standard.threesixtygiving.org/en/latest/technical/reference/#beneficiary-location" target="_blank">beneficiary location fields.</a> 

### Challenges with beneficiary location data
Beneficiary location data can provide a more accurate location for the intended impact of a grant, and is therefore more useful when carrying out analysis on where grants go. However it is also a more challenging type of data to collect and publish.

The types of challenges include:

- This data can be difficult to collect consistently, especially if the size of areas supported by grants varies greatly from those with a national or regional scope to local or hyperlocal delivery areas.
- A grant could fund activities in an area that crosses local authority or region boundaries or doesn’t relate to any officially defined areas.
- The grant could fund activities being delivered in more than one place.
- The delivery location could be undefined, for example because the grant is unrestricted, is funding policy work or services that are provided online.

**Start by sharing what you can**
                  
We recommend that funders who collect location data that could be shared as beneficiary location should publish this information whenever possible.

There is no one-size fits all approach to beneficiary location, as funders have a diverse range of geographical scopes and priorities.

Funders with a geographical focus to their funding, especially place-based funders focused on a defined place (such as community foundations), will often be collecting detailed geodata that can be shared.

Funders with national programmes or without a geographic focus might collect this location data at a high level that indicates the region or country but does not drill down to smaller areas.

Currently <a href="https://qualitydashboard.threesixtygiving.org/alldata" target="_blank">two-thirds of organisations</a> sharing 360Giving data include beneficiary location name information but only one-third include beneficiary location codes.

### Guide to beneficiary location
Funders have a wide range of reasons for collecting beneficiary location, and the method and level of detail will depend on what questions the data is needed to answer.

These examples highlight a few of the common approaches, and outline the benefits and limitations these can have. Hopefully they will provide inspiration for funders that don’t currently collect and share beneficiary location information but would like to do so in future.

**Project location postcode**
                  
Funders can ask applicants to provide a ‘project postcode’ to indicate where the funded work will take place. This postcode might relate to an address or could also be picked from within a wider area.This data can be shared directly as a postal code, or converted into a geocode prior to publication.

The advantage of working with postcodes is that these are the most commonly used and understood type of geodata. A postcode can be matched to ONS geocodes and scaled up to a larger area when appropriate. Postcodes are also easy to convert into latitude and longitude coordinates for use in maps.

This approach can be suitable for collecting data about very localised funding or grants aimed at a specific location, such as a building or park. It is less accurate or useful for capturing the location of grants for any activities carried out over a larger area or multiple locations.

**Location picklist**
                  
On application forms funders may provide a list of locations - known as a picklist - for applicants to select the place or places where they are delivering their activities.

Grants management systems might have an ‘area of operation’ field with region or country values by default. For funders with a regional or county area of focus, the list of locations might be broken down into the local authority areas or at ward level for funders focused on a single city or council area. These place names can be published in 360Giving data on their own or with their corresponding geocodes.

The advantage of working with picklist values is the data is consistent and it can be straightforward to match these names with geocodes. This approach can be suitable for a wide range of funders and scaled to work for those funding nationally or locally. 

When location is collected at a regional or country level, the data is less usable for mapping but will still provide useful information for analysing broad trends and showing when the funded activity is in a different place from the recipient location.

When multiple locations are provided for each grant it is possible to publish these in 360Giving data. See the [guidance below](multiple-locations) for further information.

**Funder or programme area of operation**
                  
Funders with a defined area of operation or programmes (with place specific eligibility criteria) will know the maximum possible location area of a grant even if specific geodata isn’t being collected.

This type of scope data can be applied to all grants that meet the criteria, providing a useful starting point to publishing location data. When the funder or programme scope is a local authority area, this provides useful data for geographical analysis being carried out at a county, regional or national level. 

However the potential for variation within council areas means data provided at this level or higher cannot be meaningfully compared with statistical data such as Indices of Multiple deprivation, which are linked to small area geographies.

```eval_rst
.. _multiple-locations:
```
                    
### Sharing data with multiple beneficiary locations
It is possible to include multiple beneficiary locations for each grant, because the 360Giving Data Standard allows for the creation of [one to many relationships.](one-to-many-relationships)
                  
Multiple beneficiary location fields could be used to:
- Provide alternative types of geodata for the same location - for example including the local authority ward and parliamentary constituency area codes, and latitude and longitude coordinates which are all based on the same project postcode area.
- Describe two or more different locations that are impacted by the funding.
- Represent a bespoke area that does not correspond to any official ONS geocode by using a group of smaller area geocodes.

For publishers using [JSON format](360giving-json-schemas), sharing data with multiple locations for each grant is straightforward as the schema is designed to work in this way.

For publishers using spreadsheets, there are a couple of ways to structure one-to-many relationships for sharing multiple locations, which we have detailed below.

**Including multiple location fields in the main sheet**
                  
For publishers who have three or fewer fields of beneficiary location per grant, it will be easiest to include all three within the main grants sheet.

In these cases, the fields or sets of fields are numbered, starting with 0 for the first column. 

For example:

<div class="table table--zebra">
    <table>
        <thead>
            <th>Beneficiary Location:0:Name</th>
            <th>Beneficiary Location:1:Name</th>
            <th>Beneficiary Location:2:Name</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Beneficiary Location:0:Name">Copeland</td>
                <td data-header="Beneficiary Location:1:Name">South Lakeland</td>
                <td data-header="Beneficiary Location:2:Name">Barrow-in-Furness</td>
               </td>
            </tr>
        </tbody>
    </table>
</div> 

**Including multiple location fields in an additional sheet**
                  
With four or more columns of location data, it may become easier to include all the beneficiary location columns in a separate sheet within the file.

The main spreadsheet template includes a sheet for each part of Standard. The beneficiary location sheet includes the fields from this object and the grant Identifier, which is used to associate the data with each grant.

Using this method, there should be a row for each location, repeating the grant Identifier for each group of locations associated with the grant. The following example shows two grants which each have three Beneficiary Locations:

<div class="table table--zebra">
    <table>
        <thead>
            <th>Identifier</th>
            <th>Beneficiary Location:Name</th>
            <th>Beneficiary Location:Geographic Code</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Identifier">360G-ExampleFdn-001</td>
                <td data-header="Beneficiary Location:Name">Copeland</td>
                <td data-header="Beneficiary Location:Geographic Code">E07000029</td>
                    <tr>
                <td class="table__lead-cell" data-header="Identifier">360G-ExampleFdn-001</td>
                <td data-header="Beneficiary Location:Name">South Lakeland</td>
                <td data-header="Beneficiary Location:Geographic Code">E07000031</td>
                </td>
                  <tr>
                <td class="table__lead-cell" data-header="Identifier">360G-ExampleFdn-001</td>
                <td data-header="Beneficiary Location:Name">Barrow-in-Furness</td>
                <td data-header="Beneficiary Location:Geographic Code">E07000027</td>
                </td>
                  <tr>
                <td class="table__lead-cell" data-header="Identifier">360G-ExampleFdn-002</td>
                <td data-header="Beneficiary Location:Name">Carlisle</td>
                <td data-header="Beneficiary Location:Geographic Code">E07000028</td>
                </td>
                   <tr>
                <td class="table__lead-cell" data-header="Identifier">360G-ExampleFdn-002</td>
                <td data-header="Beneficiary Location:Name">Allerdale</td>
                <td data-header="Beneficiary Location:Geographic Code">E07000026</td>
                </td>
                  <tr>
                <td class="table__lead-cell" data-header="Identifier">360G-ExampleFdn-002</td>
                <td data-header="Beneficiary Location:Name">Eden</td>
                <td data-header="Beneficiary Location:Geographic Code">E07000030</td>
                </td>
              <tr>
        </tbody>
    </table>
</div> 

## Funding organisation location
In addition to providing location information for recipients and beneficiaries, the location of the funding organisation itself can be included, either using the address or location fields.

View the full range of available <https://standard.threesixtygiving.org/en/latest/technical/reference/#funding-org" target="_blank">funding organisation address fields</a> or <https://standard.threesixtygiving.org/en/latest/technical/reference/#funding-org-location" target="_blank">funding organisation location fields.</a>

### What's next?
Read our guidance to find out how to check your data using the 360Giving Data Quality Tool.
