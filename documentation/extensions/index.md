# Extensions

The [360Giving Data Standard](https://standard.threesixtygiving.org/en/latest/about/) is a uniform and consistent way to describe grantmaking data. It consists of a set of information fields that must be included when a grantmaking organisation shares grant data. Organisations publishing grant information using the Standard use the same formatting so the data can be easily understood, collated and compared by anyone. Data published using the 360Giving Data Standard can be located and ‘read’ easily by different applications and machines, including 360Giving’s own tools [GrantNav](https://grantnav.threesixtygiving.org) and [360Insights](https://insights.threesixtygiving.org).

360Giving data publishers may sometimes wish to collect and publish information which is not part of the 360Giving Data Standard. The Standard permits publishers to use any number of “additional fields“ in their data to meet their needs, but these additional fields are not recognised by the Standard. This means that they cannot be validated using tools such as the [Data Quality Checker](https://dataquality.threesixtygiving.org/) or used to filter data in GrantNav and 360Insights, and different publishers including the same kind of information may struggle to coordinate around how to name and structure this additional data. Read our guidance on [Additional fields](../technical/reference.md#additional-fields).

**Extensions** to the 360Giving Data Standard are a way to address some of the issues with additional fields by introducing new optional fields and structures into 360Giving data. Each extension formally defines fields, structures, and rules which can then be recognised by tooling such as the Data Quality Checker which allows the data using extensions to be validated, and also provides further standardisation which supports interoperability between different datasets.

Extensions also address the issue of trying to support different use cases of 360Giving data whilst maintaining the stability and integrity of the Standard. A set of fields and features may be important to a significant portion of the 360Giving publishing community while there may not be enough demand to warrant adding the feature to the core set of Standard fields. Developing these features as an Extension can meet the needs of the community in a much shorter timescale, as well as providing a way to test out how the features work in practice. It is possible that an extension to the 360Giving Data Standard may later be integrated into the core Standard.

This section is the home for documentation about approved extensions to the 360Giving Data Standard.
To date there is only one approved extension which is used for the publication of [DEI Data Standard](https://www.funderscollaborativehub.org.uk/dei-data-standard) data alongside 360Giving data.

```eval_rst

.. toctree::
   :maxdepth: 3

   dei/index

```
