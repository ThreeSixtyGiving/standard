# Get Data

In order to help grantmakers, developers and analysts discover data that uses the 360Giving Standard, 360Giving maintains a register of data at [http://data.threesixtgiving.org/](http://data.threesixtgiving.org/)

## JSON Feeds

### Registry

A JSON feed is available at
[http://data.threesixtygiving.org/data.json](http://data.threesixtygiving.org/data.json). The JSON is an array of objects in the following format:

~~~json

[
  {
     "title":"Title of the dataset",
     "description":"Description about the dataset",
     "identifier":"An internal identifier for this dataset from our
                  storage system",
     "license":"A link to the license information for this dataset.
                  Should be a valid URL",
     "license_name":"A human readable title of the license given in
                      the license field",
     "issued":"The date (YYYY-MM-DD) this dataset was first
                        recorded as published",
     "modified":"The datetime that this record was last changed.
                       The change could relate to any of the metadata
                       about the dataset",
     "publisher": {
        "name":"Name of the organisation publishing this dataset",
        "website":"Should be a valid URL to a website of that publisher",
        "logo":"Should be a valid URL to a logo for that publisher.
                You may not necessarily have permission to use this
                logo for your own purposes.",
        "prefix":"The unique 360Giving prefix used by this publisher
                  to identify the grants they publish."
     },
     "distribution":[ {
        "downloadURL":"A valid URL to directly access the data",
        "accessURL": "A valid URL, usually to a web page, where access
                      to the downloadURL can be found. The web page
                      usually has other useful information about the data",
        "title":"Title of the dataset"}
     ]
  },
]

~~~

### Metadata

360Giving provides [a JSON feed](https://storage.googleapis.com/datagetter-360giving-output/branch/master/status.json) that contains metadata about files in the registry, including file statistics (including size, location, validity against the standard), aggregate statistics (including total grants, values, and dates) and useful insights (including identifier schemes used).

Additionally, a [CSV report](https://gist.github.com/30d835ae16e2a30efde8a63acf03628d) is available, which contains a subset of the fields available in the JSON feed, focussed on the aggregate statistics.

## Downloading Data

[datagetter](https://github.com/datagetter/) downloads all of the data that is listed in the registry, and converts it to JSON for use in an application.

## FAQ

### How often do the JSON feeds update?

All of the feeds linked from this page update daily.

### How can I follow changes/developments?

This documentation is maintained on GitHub
[https://github.com/ThreeSixtyGiving/standard/tree/master/documentation/getdata](https://github.com/ThreeSixtyGiving/standard/tree/master/documentation/getdata)

### How do I give feedback or report bugs?

We welcome all feedback! Please open an issue at [https://github.com/ThreeSixtyGiving/standard](https://github.com/ThreeSixtyGiving/standard), or contact [info@threesixtygiving.org](mailto:info@threesixtygiving.org).

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />All JSON feeds linked from this page are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

