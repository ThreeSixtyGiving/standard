# Codelists

## Introduction

The 360Giving Data Standard includes over 100 different data fields with specific names and rules about the format of the information that can be shared in each field.

There are some fields where the values that can be provided are also strictly regulated, requiring the use of a code from a specific codelist.

For example, the 360Giving Data Standard includes a field for Currency which requires publishers to use the International Organization for Standardization’s (ISO) standardised set of codes, called <a href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO 4217</a>. This means that instead of the data in this field describing the currency in various ways – such as “£” or “pounds” or “Pound Sterling” – the currency is “GBP”. 360Giving also makes use of standardised two-letter country codes taken from <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>. This makes 360Giving data more interoperable between 360Giving publishers and also enables it to be used alongside other non-360Giving datasets.

Although many fields and types of information are not suitable for standardisation in the form of a codelist, common codes should be used whenever possible. In autumn 2022, upgrades to the 360Giving introduced four new codelists into the Standard for the first time, which have been developed through consultation with data publishers and users.

This guidance explains the codelists used in 360Giving Data Standard and how to publish and use them.

## What are codelists?

Codelists are a list of values. Each value has three elements:

* a short name, which is designed for humans to read and understand
* a description, which explains to humans the meaning behind the code so that we can interpret it
* and the **code**, which is included in the data

If you have ever used a web form and selected a value from a drop-down list, this is very similar to how codelists function.

The reason for using codes instead of names is because it avoids issues caused by typos, spaces or different cases. It also means the accompanying name and description can be amended or translated without the codes needing to be changed.

## Open and closed codelists

Codelists can be closed or open.

### Closed codelists
These are intended to be comprehensive. For example, the currency codelist covers all currencies in the world.

When a codelist is closed it means that publishers must only use the codes in the codelists, and cannot add new codes if there is no appropriate code for them to use. 

### Open codelists

These are intended to be representative, but not comprehensive.

When a codelist is open it means that publishers may use a new code outside those in the codelist, if there is no appropriate code for them to use.

```eval_rst
.. _codelists-used:
```

## The codelists used in the Standard

There are seven codelists used in 360Giving Data Standard.

Two codelists, Currency and Country code are managed by ISO and the five remaining codelists are managed directly by 360Giving.

Managed externally

* [Currency](#currency)
* [Country code](#country-code)

Managed by 360Giving

* [GeoCode Type](#geocode-type)
* [Regrant Type](#regrant-type)
* [Location Scope](#location-scope)
* [Grant to Individuals Purpose](#grant-to-individuals-purpose)
* [Grant to Individuals Reason](#grant-to-individuals-reason)

All the codes used in the Standard are alphanumeric and case sensitive.

The codelists in the 360Giving Data Standard are **closed in type**. This means that you may only use the codes listed in the codelists.

For the codelists managed directly by 360Giving, if there is no appropriate code to use, it is possible to propose new codes be added to the list. Further information about how to propose new codes is set out in [Versioning and Upgrade Process](../about/governance).

(currency)=
### Currency

A codelist with values to specify the currency used in amounts.  For example GBP is the code for Pounds Sterling.

The codes from this codelist can be published in the Currency field, and also appear in the Transactions object.

To view the full list of codes visit <a href="https://en.wikipedia.org/wiki/ISO_4217" target="_blank">ISO 4217</a>.

(country-code)=
### Country code

A codelist with values to specify the 2-character ISO Country Code of a location. For example GB is the code for the United Kingdom of Great Britain and Northern Ireland.

The codes from this codelist can be published in three fields:

* Recipient Org:Location:Country Code 
* Funding Org:Location:Country Code
* Beneficiary Location:Country Code

The Geocode fields are part of objects which are an array. This means that multiple iterations of the field can be included when a publisher has more than one location to share per grant.

To view the full list of codes visit <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO-3166-1-alpha-2</a>.

(geocode-type)=
### GeoCode Type

A codelist with values to specify which type of UK geographical code has been provided in the associated Geocode field.

The codes from this codelist can be published in three fields:

* Recipient Org:Location:Geographic Code Type
* Funding Org:Location:Geographic Code Type
* Beneficiary Location:Geographic Code Type

The Geocode Type fields are part of objects which are an array. This means that multiple iterations of the field can be included when a publisher has more than one location to share per grant.

```eval_rst
.. csv-table:: 
   :file: ../../codelists/geoCodeType.csv
   :header-rows: 1
   :widths: auto
```

```eval_rst
.. _regrant-type:
```

### Regrant Type

A codelist with values to specify that a grant is intended for redistribution, broken down into seven types of regrant.

The codes from this codelist can be published in the field **For Regrant Type**. The **For Regrant Type field** can only be included once with a single code per grant.

For further explanation of how to use the Regrant Type codelist, including examples, read the [360Giving guide to regranting](../guidance/regranting).

```eval_rst
.. csv-table::
   :file: ../../codelists/regrantType.csv
   :header-rows: 1
   :widths: auto
```

```eval_rst
.. _location-scope:
```

### Location Scope

A codelist with values to specify a grant's geographical scope, broken down into seven levels.

The codes from this codelist can be published in the field **Location Scope**. The **Location Scope field** can only be included once with a single code per grant.

For further explanation of the location scope codelist, including examples, read the [360Giving guide to location data](../guidance/location-guide.md).

```eval_rst
.. csv-table::
   :file: ../../codelists/locationScope.csv
   :header-rows: 1
   :widths: auto
```

```eval_rst
.. _grant-purpose:
```

(grant-to-individuals-purpose)=
### Grant to Individuals Purpose

A codelist with values to specify the purpose of the grant, in terms of what the funding will be used for. This codelist is intended for use in grants to individual recipients only.

The codes from this codelist can be published in the field **To Individuals Details:Grant Purpose**.

The **To Individuals Details:Grant Purpose** field is an array. This means that when a grant has more than one purpose it is possible to include multiple codes in this field, separated by a semi-colon.

**Please note:** This is the only codelist field that is an array. All other fields in the 360Giving Data Standard which use codelists only allow a single code per field.

```eval_rst
.. csv-table:: 
   :file: ../../codelists/grantToIndividualsPurpose.csv
   :header-rows: 1
   :widths: auto
```

```eval_rst
.. _grant-reason:
```

(grant-to-individuals-reason)=
### Grant to Individuals Reason

A codelist with values to specify the reason that the grant was awarded to the recipient. This codelist is intended for use in grants to individual recipients only.

The codes from this codelist can be published in either of two fields, **To Individuals Details:Primary Grant Reason** and **To Individuals Details:Secondary Grant Reason**. Each field can only be included once with a single code per grant.

```eval_rst
.. csv-table::
   :file: ../../codelists/grantToIndividualsReason.csv
   :header-rows: 1
   :widths: auto
```

```eval_rst
.. _codes-how-to:
```

## How to use codelists in 360Giving data

Only codes from the codelists may be used. Any other code included in the data will result in invalid data. Please be aware that the codes are also case sensitive. Reproduce uppercase and lowercase letters in the codes correctly or the code will not be recognised and your data will be invalid.

Only one code is allowed per field, and it is not possible to include comma separated lists of codes in a single field. If the field is an array (see [Reference](reference)) then you may use more than one code from the codelist in a spreadsheet by adding columns utilising the [Numbering](numbering) technique, which is used elsewhere for describing multiple occurrences of e.g. Locations.

Codes may not be applicable to all grants. When a grant has no relevant code, the field must be left blank. Do not use filler values such as N/A — a codelist field must only be populated with valid codes or left blank.

### Adding extra information

The code names can be included in **Title** or **Description** text fields to help users of the data.

Including the code names and descriptions in additional non-Standard fields may also be helpful when preparing the data, and for data users.

However, be aware that only the codes themselves are validated by 360Giving tools, and the additional data fields will not be included in data downloads provided by 360Giving tools.

#### Examples

Regrant Type

<div class="table table--zebra">
  <table>
    <thead>
      <th>Identifier</th>
      <th>Description</th>
      <th>Amount Awarded</th>
      <th>For Regrant Type</th>
    </thead>
    <tbody>
      <tr>
        <td>360G-ExampleFdn-001</td>
	<td>Contribution to pooled fund for charities supporting local residents</td>
	<td>50000</td>
	<td>FRG040</td>
      </tr>
      <tr>
        <td>360G-ExampleFdn-002</td>
	<td>Contribution to salary of benefits adviser</td>
	<td>10000</td>
	<td></td>
      </tr>
      <tr>
        <td>360G-ExampleFdn-003</td>
	<td>To be awarded as grants to small arts organisations</td>
	<td>25000</td>
	<td>FRG010</td>
      </tr>
      <tr>
        <td>360G-ExampleFdn-004</td>
	<td>To fund outdoor play equipment for nursery</td>
	<td>5000</td>
	<td></td>
      </tr>
    </tbody>
  </table>
</div>

Grant To Individuals Codelists

<div class="table table--zebra">
  <table>
    <thead>
      <th>Identifier</th>
      <th>To Individuals Details:Primary Grant Reason</th>
      <th>To Individuals Details:Secondary Grant Reason</th>
      <th>To Individuals Details:Grant Purpose</th>
    </thead>
    <tbody>
      <tr>
        <td>360G-ExampleFdn-001</td>
	<td>GTIR010</td>
	<td>GTIR030</td>
	<td>GTIP070;GTIP080</td>
      </tr>
      <tr>
        <td>360G-ExampleFdn-002</td>
	<td>GTIR010</td>
	<td>GTIR100</td>
	<td>GTIP020;GTIP030;GTIP040</td>
      </tr>
    </tbody>
  </table>
</div>
