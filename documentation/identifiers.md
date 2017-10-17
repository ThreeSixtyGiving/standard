# Identifiers

```eval_rst 

.. admonition:: Why identifiers matter

  Identifiers are an important part of any dataset. They let a computer uniquely identify and refer to specific grants, organisations, transactions and so-on. 

  Whilst a human being may be good at recognising that "INDIGO TRUST", "The Indigo Trust", and "indigo-trust" all refer to the same organisation, computers find this a lot trickier. 

```

360Giving asks you to give identifiers to:

* [Grants](grant-identifier)
* [Organisations](organisation-identifier);
* Transactions; 
* Classifications;
* and other unique elements in your data.

These go in an ```Identifier``` column alongside accessible text descriptions of the grant, the name of an organisation, or the title of a classification.


```eval_rst
.. _creating-identifiers:
```

## Identifier basics

You may already have identifiers in your own data. For example, a number for each application or grant. You can use these existing **internal identifiers** as part of your published data. 

*However,* because there might be an overlap between the internal identifiers you use, and the internal identifiers another funder uses, you need to add a **prefix** to avoid this possible clash. 

```eval_rst
.. admonition:: For example

  If Indigo Trust have a grant called 'Grant27', and Nominet Trust also have a grant called 'Grant27' the two will get confused when combining the two datasets. But if, when publishing, each one adds a prefix, then we end up with two unique identifiers: '360G-indigotrust-Grant27' and '360G-Nominet-Grant27'
```

For grants, and other identifiers particular to your organisation, you use can use a **360G prefix**.

For organisation identifiers, if you can, use an officially recognised identifier for the organisation, following the [organisation identifier](organisation-identifier) guidance below. If you can't do this right away, you can also use your internal identifiers for grantees along with your assigned 360G prefix. 


```eval_rst
.. _register-prefix:
```

## Get your prefix

To register a prefix for your organisation, [click here](http://www.threesixtygiving.org/support/standard/register/).

All registered prefixes should start with 360G unless you have been advised otherwise by the support team. 

```eval_rst
.. _grant-identifier:
```

## Grant Identifier

To create your grant identifiers:

1. Make sure you have asked for a 360Giving prefix.
2. Look for an existing internal identifier given to your grants (for example, a sequential number assigned to each grant at the point of application). The important thing is that the identifier should be unique inside your organisation, so adding the prefix will make it unique across the whole world.
3. Add this to the end of your 360Giving prefix.

```eval_rst
.. admonition:: For example

  If your prefix is ``360G-xyztrust`` and you have a grant identified internally as ``123``, you would combine these to give ``360G-xyztrust-123``
```

  We recommend using a hyphen (-) for the separator to use between your prefix and the internal identifier. Avoid using slashes (\ and /) as these can cause problems with some applications.

  If your internal identifiers include spaces or special characters, we recommend replacing these with underscore (_):

  ``360G-xyztrust-123_ABC``

```eval_rst
.. _organisation-identifier:
```

## Organisation Identifier

There are many different kinds of organisations that give, receive or benefit from grants, such as:

* Registered companies
* Registered charities
* Community organisations
* Overseas organisations
* Public bodies
* Schools, universities and other educational establishments
* Individuals

Most organisations have some sort of official registration number that can be used to uniquely identify them and to look up their details from an official registers or public list. 

There are two parts to an organisation identifier:

* **A list code** that describes the list the identifier is taken from.
* **An identifier** taken from that list.

In 360Giving data we ask publishers to use a list code taken from the [org-id list locator](http://org-id.guide/). This provides an open, maintained list of codes for many different lists around with world, giving a way to identify almost any organisation. 

```eval_rst

.. admonition:: For example

  A charity registered in England and Wales with the Charity Commission of England and Wales, with the charity number '1070468' will use a prefix of ``GB-CHC``. 

  This gives an unique organisation identifier of ``GB-CHC-1070468``

```

### Choose the best identifier

Some organisations have more than one identifier: they might be a charity **and** a company (charitable companies), or a charity **and** an educational establishment. 

In these cases, it's important to know which identifier to pick so that users of data have the best possible chance of understanding that two grants have been made to the same organisation. 

[org-id.guide](http://org-id.guide) ranks identifier lists by relevance and quality to help you pick the best identifier. 

```eval_rst

.. hint:: Relevance and quality defined: 

  * Relevance: are you likely to find the organisation you are looking for in this list?
  * Quality: are the identifiers in this list stable and linked to open, accessible contextual data, and can they be easily mapped to other identifiers.
```

Search on [org-id.guide](http://org-id.guide) for identifier sources for [UK organisations](http://org-id.guide/?structure=&coverage=GB&subnational=&sector=), [UK charities](http://org-id.guide/?structure=charity&coverage=GB&sector=), or [any other organisation type](http://org-id.guide/).

### Commonly used identifier lists

The following identifier lists are often used in 360Giving publication. They are listed here in rough order of priority (e.g. if you already know the company number, use this in preference to the charity number).

* [GB-COH](http://org-id.guide/list/GB-COH) - UK Company Number
* [GB-CHC](http://org-id.guide/list/GB-CHC), [GB-SC](http://org-id.guide/list/GB-SC), [GB-NIC](http://org-id.guide/list/GB-NIC) - Charity Numbers
* [GB-EDU](http://org-id.guide/list/GB-EDU) and [GB-UKPRN](http://org-id.guide/list/GB-UKPRN) - Education establishments
* [GB-LAE](http://org-id.guide/list/GB-LAE) (England), [GB-LAS](http://org-id.guide/list/GB-LAS) (Scotland), [GB-PLA](http://org-id.guide/list/GB-PLA) (Wales)  - Local authorities


If you have a registered number from some other scheme, including overseas registrars, check the [org-id List Locator](http://org-id.guide/) for a Registration Agency Code to use. If the Registration Agency Code you need is not listed, [contact the support team](http://www.threesixtygiving.org/contact/).

If you do not have any external registration numbers for the organisation, use your 360Giving prefix and any internal identifier you have for this organisation.
    
If you use a database that records details of organisations in a separate lookup table, this may provide an identifier you can use. 
    
If you only record data in a spreadsheet, and don't assign organisations an ID, you could use a spreadsheet formula to turn the organisation name into an identifier (e.g. removing spaces and lowercasing the name). The support team can provide guidance on this. 
    
If there is a chance that your organisation identifiers might overlap with grant identifiers, just add 'ORG' into the identifier string (e.g. '360G-xyztrust-ORG123')

```eval_rst

.. admonition:: Special 360 giving fields for charity and company number

   Because 'Company Number' and 'Charity Number' are so important for analysing grantmaking in the UK, the 360 Giving Standard includes additional special fields these on their own (without the prefixes), to help users of the data. 

   If you have these details, you should fill them in, **in addition to** providing the unique organisation identifier using the method above. 
```

### Collecting organisation identifiers

Make sure that when you collect charity or company numbers, you clearly identifier in your forms of systems what kind of number they are. 



```eval_rst
.. _codes:
```

## Classifications

[Contact the support team](http://www.threesixtygiving.org/contact/) for details of prefixes to use when publishing classification codes for your grants.

## A step further: using identifiers to join up information

We use simple text identifiers in 360Giving. As well as using these identifiers in your published data, you could also tell your grantees their prefixed identifier, and encourage them to include it in any documents they publish about their funded projects, or to include it as a 'machine tag' (or hashtag) when uploading photos and videos to social media sites. 

> For example, some of the development of 360Giving was funded by grant '360G-indigotrust:IND233'. If you [search the web for that identifier](https://www.google.co.uk/search?q=360G-indigotrust%3AIND233), you will find this site. If there were project reports published online about this grant, or photos and videos, you might be able to discover those as well. If you just searched for the **internal identifer** [IND233](https://www.google.co.uk/search?q=IND233) you would have to comb through details of all sorts of other things identified as IND233 before finding any information about the grant.

You can also make use of your 360Giving identifiers in internal reports and documents, as this will make it easier to digitally link these up with the data in your 360Giving data files in future.
