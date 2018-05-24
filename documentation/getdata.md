# Get Data

## List

A list of all known data in the 360Giving format can be found on the website at: [http://www.threesixtygiving.org/data/find-data/](http://www.threesixtygiving.org/data/data-registry/)

## JSON Feed

A JSON feed of this data can be found at the following endpoint: 
[http://data.threesixtygiving.org/data.json](http://data.threesixtygiving.org/data.json)

Requests to the endpoint will return a JSON file that contains a number of records about data sets.

The JSON is an array of objects in the following format:

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

## FAQ

### How often do people update their data?

Not often. A call to the JSON endpoint once a day would probably be more than enough.

### Do I need an API key?

No.

### How can I follow changes/developments?

This documentation is maintained on GitHub
[https://github.com/ThreeSixtyGiving/standard/tree/master/documentation/getdata](https://github.com/ThreeSixtyGiving/standard/tree/master/documentation/getdata)

As the documentation changes we will publish a changelog on this page.

### How do I report bugs

Please use the GitHub project: [https://github.com/ThreeSixtyGiving/standard](https://github.com/ThreeSixtyGiving/standard)

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />The JSON feed found at the endpoint is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
## Changelog

**2017-04-13** - Adds license information to this page

**2017-03-27** - Adds the `issued` and `modified` fields

**2016-06-28** - Adds the `prefix` field to the publisher list

**2016-06-07** - Changes links to list of all known data and to the JSON feed

**2016-05-24** - Added the `license_name` field

**2016-05-22** - Documentation first created

