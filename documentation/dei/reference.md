# DEI Reference

## About

This is the documentation for the DEI Extension provided by 360Giving. The DEI Extension is an extension to the 360Giving Data Standard which allows [Diversity, Equality, and Inclusion (DEI) Data Standard](https://www.funderscollaborativehub.org.uk/dei-data-standard) data to be published alongside [360Giving data](https://standard.threesixtygiving.org/en/latest/#), so that it can be validated and used in 360Giving tools.

The DEI Data Standard is developed and maintained by the DEI Data Group, with technical support provided by 360Giving.

The DEI Extension has been developed and is maintained by 360Giving to support new and existing 360Giving publishers to include DEI Data Standard data in their 360Giving data files.

### Governance and Versioning

As an extension to the 360Giving Data Standard, the DEI Extension is managed outside of the [governance process](https://standard.threesixtygiving.org/en/latest/about/governance/) of the 360Giving Data Standard itself.

360Giving is the steward of the DEI Extension. Our CEO is responsible for its day-to-day management, supported by a Product Manager and an external specialist technical team, Open Data Services Coop.

#### Aims and Approach

Our aims and approach for maintaining the DEI Extension are as follows:

1. Compatibility with the 360Giving Data Standard
To maintain compatibility with the latest release of the 360Giving Data Standard. 

2. Compatibility with the DEI Data Standard
To maintain compatibility with the DEI Data Standard itself whenever possible. Updates to the DEI Extension will be issued in a timely manner to bring it in line with changes to the taxonomy structure and codes included in the DEI Data Standard, as well as any guidance about how to apply this to publishing the data alongside 360Giving data.

3. Use semantic versioning
To use semantic versioning to version this extension: MAJOR updates will not be compatible with previous versions of the extension, MINOR updates will add new features that are backwards compatible, and PATCH updates will fix bugs and amend documentation. 

4. Consider stakeholders needs in the revision process
To consider stakeholders needs and follow [360Giving Data Standard revision processes](https://standard.threesixtygiving.org/en/latest/about/governance/#the-revision-process) when making updates to the DEI Extension.

#### Versions

The DEI Extension is versioned using [Semantic Versioning](https://semver.org/).

The version number of the DEI Extension and update processes and schedules are *separate* from each: the [360Giving Data Standard](https://standard.threesixtygiving.org/en/latest/about/governance/#versions); and the [DEI Data Standard](https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard).

This means there may be times when data shared using the DEI Extension does not match the latest version of the DEI Data Standard.

The version number and all notable changes are documented by Release via the Changelog.

#### Changelog

All notable changes to the DEI Extension are documented by Release via the extension's [Github repository](https://github.com/ThreeSixtyGiving/360-dei/releases)

## Technical Reference

### Extension Structure Overview

The DEI Extension defines new fields and structures for use within 360Giving data, for the purpose of publishing data using the DEI Data Standard within a file of 360Giving grant data. It also adds a number of new codelists to validate the contents of various fields.

Some fields are used to share taxonomy and free text data collected through the application of the DEI Data Standard. There are also fields used to share metadata, which allow publishers to provide information about how the DEI Data Standard was applied in their specific context.

The DEI Extension adds a new field called `deiDetails` to each grant. Inside `deiDetails` there are three fields: `leadership`, `mission`, and `project`. These represent the three application areas of the DEI Data Standard for grantmaking.

Each of the `leadership`, `mission`, and `project` fields has the format of a `DeiApplicationArea` object. This is a new object defined by the DEI Extension so that each application area and its responses have the same structure and semantics, which makes the data more consistent and simpler to publish and use. `DeiApplicationArea` contains fields for important metadata to represent whether a question was asked (and how), as well as for sharing the responses to these questions.

The extension structure is as follows:

* `grants` (from [360Giving Data Standard](https://standard.threesixtygiving.org/en/latest/technical/reference/#))
  * `deiDetails`
    * `deiVersion`
    * `purposes` 
    * `leadership`, `mission`, and `project` (`DeiApplicationArea`)
      * `askedStatus` (required)
      * `replyStatus`
      * `availableOptions`
      * `additionalDetails`
      * `response`
        * `taxonomyCodes`
        * `livedExperience`
        * `Geography`

In the extension, the `deiDetails` field is *optional for each grant*. However, when it is included then each `leadership`, `mission`, and `project` become *required for that grant*, and each of these then have a required `askedStatus` field.

For a publisher of data using this extension this means that:

* If there is no DEI information for the grant, you may omit the entire `deiDetails` field for that grant
* If there is DEI information for the grant, then you must include the `deiDetails` field and provide at least a value in `askedStatus` for each of the `leadership`, `mission` and `project` application areas. This is to ensure a minimum level of context required for a user to interpret the data correctly.

### Schema

This section contains a reference for the Extension’s schema

#### Grant and DEI Details

The extension defines the `deiDetails` field, which is a new object in the 360Giving Grant Schema

TODO schema table for grants.deiDetails

#### DEI Application Area

The extension defines a new `DeiApplicationArea` with the following fields:

TODO schema table for DeiApplicationArea

### Codelists

The extension adds several codelists to promote interoperability between datasets. These are all **closed** codelists, meaning that only values from the codelists may be used.

#### Asked Status

A codelist to declare whether DEI Data Standard questions were asked for this grant, and how.

#### Available Options

A codelist to declare which answer options were available to the respondents.

#### Reply Status

A codelist to declare whether a reply to DEI Data Standard questions was received or not.

#### Taxonomy Codes

The authoritative source for the DEI Taxonomy codes vocabulary is the [DEI Data Standard](https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard) and should take precedence over all other sources of information about the DEI Taxonomy codes, including this codelist.

The DEI Extension for 360Giving creates and maintains this codelist by taking the hierarchical codes defined in the DEI Data Standard, encoding them into JSON, and then generating this codelist automatically. This is necessary to provide a machine-readable codelist to support validation.

Please see the [Guiding Principles](#guiding-principles) section for more information on how we respond to updates in the DEI Standard.
