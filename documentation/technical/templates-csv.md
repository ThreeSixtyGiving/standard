---
orphan: true # This suppresses warnings that this file is not included in any toc tree
---
# 360Giving CSV Templates

The CSV files listed below can be used as templates to create data to fit the 360Giving Data Standard:

```{eval-rst}
.. directory_list::
    :path: ../schema/summary-table/360-giving-schema-titles.csv/
    :url: ../../_static/summary-table/360-giving-schema-titles.csv/
```

## grants.csv

This is a simple flat file with most of the popular fields that most people use.

## Everything else

The rest of the CSV files in this directory allow you to create more complex data where, for example, data will not fit on on a single row.
You could, for example, specify that a single grant went to many Beneficiary Locations, in which case you would also use the Locations.csv
