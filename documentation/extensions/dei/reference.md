# Technical Reference

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


```eval_rst
.. jsonschema-titles:: ../../extras/extensions/dei/360-giving-schema.json
```

### Codelists

The extension adds several codelists to promote interoperability between datasets. These are all **closed** codelists, meaning that only values from the codelists may be used.

#### Asked Status

A codelist to declare whether DEI Data Standard questions were asked for this grant, and how.


```eval_rst
.. csv-table:: 
   :file: ../../extras/extensions/dei/codelists/askedStatus.csv
   :header-rows: 1
   :widths: auto
```

#### Available Options

A codelist to declare which answer options were available to the respondents.

```eval_rst
.. csv-table:: 
   :file: ../../extras/extensions/dei/codelists/availableOptions.csv
   :header-rows: 1
   :widths: auto
```

#### Reply Status

A codelist to declare whether a reply to DEI Data Standard questions was received or not.

```eval_rst
.. csv-table:: 
   :file: ../../extras/extensions/dei/codelists/replyStatus.csv
   :header-rows: 1
   :widths: auto
```

#### Taxonomy Codes

The authoritative source for the DEI Taxonomy codes vocabulary is the [DEI Data Standard](https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard) and should take precedence over all other sources of information about the DEI Taxonomy codes, including this codelist.

The DEI Extension for 360Giving creates and maintains this codelist by taking the hierarchical codes defined in the DEI Data Standard, encoding them into JSON, and then generating this codelist automatically. This is necessary to provide a machine-readable codelist to support validation.

Please see the [Guiding Principles](#guiding-principles) section for more information on how we respond to updates in the DEI Standard.

```eval_rst
.. csv-table:: 
   :file: ../../extras/extensions/dei/codelists/taxonomyCodes.csv
   :header-rows: 1
   :widths: auto
```
