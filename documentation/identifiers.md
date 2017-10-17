# Identifiers

```eval_rst 

.. admonition:: Why identifiers matter

  Identifiers are an important part of any dataset. They let a computer uniquely identify and refer to specific grants, organisations, transactions and so-on. 

  Whilst a human being may be good at recognising that "Big Lottery Fund", "BLF", and "big-lottery-fund" all refer to the same organisation, computers cannot make this connection unless a unique identifier is provided. 

```

360Giving asks you to give identifiers to any of the following elements that you include in your data:

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

For organisation identifiers, we strongly encourage you to use an officially recognised identifier for the organisation, following the [organisation identifier](organisation-identifier) guidance below. 


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
* Voluntary and community organisations
* Overseas organisations
* Public bodies
* Schools, universities and other educational establishments
* Individuals

Most organisations (with the exception of unregistered voluntary and community groups) have some sort of official registration number that can be used as a uniquely identifier and used to look up their details from an official registers or public list. 

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

* UK Company Number - [GB-COH](http://org-id.guide/list/GB-COH)
* Charity Numbers - [GB-CHC](http://org-id.guide/list/GB-CHC), [GB-SC](http://org-id.guide/list/GB-SC), [GB-NIC](http://org-id.guide/list/GB-NIC)
* Education establishments - [GB-EDU](http://org-id.guide/list/GB-EDU) and [GB-UKPRN](http://org-id.guide/list/GB-UKPRN) 
* Local authorities - [GB-LAE](http://org-id.guide/list/GB-LAE) (England), [GB-LAS](http://org-id.guide/list/GB-LAS) (Scotland), [GB-PLA](http://org-id.guide/list/GB-PLA) (Wales)  - 

If you have a registered number from some other scheme, including overseas registrars, check the [org-id List Locator](http://org-id.guide/) for a Registration Agency Code to use. If the Registration Agency Code you need is not listed, [contact the support team](http://www.threesixtygiving.org/contact/).

If you do not have any external registration numbers for the organisation, use your 360Giving prefix and any internal identifier you have for this organisation.


```eval_rst

.. admonition:: Special 360 giving fields for charity and company number

   Because 'Company Number' and 'Charity Number' are so important for analysing grantmaking in the UK, the 360 Giving Standard includes additional special fields these on their own (without the prefixes), to help users of the data. 

   If you have these details, you should fill them in, **in addition to** providing the unique organisation identifier using the method above. 
```

### Collecting organisation identifiers

Make sure that when you collect charity or company numbers, you clearly identify in your forms or systems which type of number they are. 

```eval_rst
.. _codes:
```

## Classifications

[Contact the support team](http://www.threesixtygiving.org/contact/) for details of prefixes to use when publishing classification codes for your grants.
