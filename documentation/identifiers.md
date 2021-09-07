# Identifiers

```eval_rst

.. admonition:: Why identifiers matter

  Identifiers are an important part of any dataset. They let a computer uniquely identify and refer to specific grants, organisations, transactions and so-on.

  Whilst a human being may be good at recognising that “R S P B”, “Royal Society for the Protection of Birds” and “The RSPB” all refer to the same organisation, computers cannot make this connection unless a unique identifier is provided.

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

However, to avoid overlap between the internal identifiers you use and the internal identifiers another funder uses, you need to add a **prefix**.

```eval_rst
.. admonition:: For example

  If Indigo Trust have a grant called 'Grant27', and the Dulverton Trust also have a grant called 'Grant27' the two will get confused when combining the two datasets. But if, when publishing, each one adds a prefix, then we end up with two unique identifiers: '360G-indigotrust-Grant27' and '360G-dulverton-Grant27'
```

For grants, and other identifiers particular to your organisation, you use can use a **360Giving prefix**.

For organisation identifiers, we strongly encourage you to use an officially recognised identifier for the organisation, following the [organisation identifier](organisation-identifier) guidance below.


```eval_rst
.. _register-prefix:
```

## Get your prefix

To register a prefix for your organisation see the [publisher guidance](https://www.threesixtygiving.org/support/publish-data).

All registered prefixes should start with 360G.
```eval_rst
.. _grant-identifier:
```

## Grant Identifier

To create your grant identifiers:

1. Make sure you have asked for a 360Giving prefix.
2. Look for an existing internal identifier given to your grants (for example, a sequential number assigned to each grant at the point of application). The important thing is that the identifier should be unique **inside your organisation**, so adding the prefix will make it unique across the whole world.
3. Add your 360Giving prefix in front of your identifier.

```eval_rst
.. admonition:: For example

  If your prefix is ``360G-xyztrust`` and you have a grant identified internally as ``123``, you would combine these to give ``360G-xyztrust-123``
```

  We recommend using a hyphen (-) for the separator to use between your prefix and the internal identifier. Avoid using slashes (\ and /) as these can cause problems with some applications.

  If your internal identifiers include spaces or special characters, we recommend replacing these with underscore (_):

  ``360G-xyztrust-123_ABC``

  ```eval_rst
  .. admonition:: Hint

  If you do not have a unique grant reference to use, or the ones you have should not be shared in open data due to privacy or security issues, then you will need to create an identifier for each grant.

  If you need to create identifiers you can use sequential numbers. Also including the year in which the grant was awarded helps to group the grants and makes it possible to restart the sequential numbers at the beginning of each year.

  You can use any reference you choose as long as it is unique within your organisation. The 360Giving prefix will then be added to make the identifier globally unique.

```



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

Most organisations (with the exception of unregistered voluntary and community groups) have some sort of official registration number that can be used as a unique identifier and used to look up their details from an official register or public list.

There are two parts to an organisation identifier:

* **A list code**: a prefix that describes the list the identifier is taken from.
* **An identifier** taken from that list.

In 360Giving data we ask publishers to use a list code prefix taken from the [org-id list locator](http://org-id.guide/). This provides an open, maintained list of codes for many different lists around with world, giving a way to identify almost any organisation.

```eval_rst

.. admonition:: For example

  A charity registered in England and Wales with the Charity Commission of England and Wales, with the charity number '1164883' will use a list code prefix of ``GB-CHC``.

  This gives an unique organisation identifier of ``GB-CHC-1164883``

```

````eval_rst
.. hint::

  UK company numbers are a unique combination of eight digits, which in some cases include letters as well as numbers. The majority of company numbers for companies registered in England and Wales start with a **leading zero**.

  Publishers should be aware of the problems that missing leading zeros in UK company numbers present when creating identifiers. `Learn more`__ about how to avoid this pitfall.
.. __: https://www.threesixtygiving.org/support/company-numbers/

````

### Choose the best identifier

Some organisations have more than one identifier: they might be a charity **and** a company (charitable companies), or a charity **and** an educational establishment.

If you have more than one type of identifier for an organisation recorded in your system, it will be necessary to pick which one to use when creating an Organisation identifier.

[org-id.guide](http://org-id.guide) ranks identifier lists by relevance and quality to help you pick the best identifier, based on what information you hold.

```eval_rst

.. hint:: Relevance and quality defined:

  * Relevance: are you likely to find the organisation you are looking for in this list?
  * Quality: are the identifiers in this list stable and linked to open, accessible contextual data, and can they be easily mapped to other identifiers.
```

Search on [org-id.guide](http://org-id.guide) for identifier sources for [UK organisations](http://org-id.guide/?structure=&coverage=GB&subnational=&sector=), [UK charities](http://org-id.guide/?structure=charity&coverage=GB&sector=), or [any other organisation type](http://org-id.guide/).

### Commonly used identifier lists

The following identifier lists are often used in 360Giving publication.

* UK Company Number - [GB-COH](http://org-id.guide/list/GB-COH)
* Charity Numbers - [GB-CHC](http://org-id.guide/list/GB-CHC), [GB-SC](http://org-id.guide/list/GB-SC), [GB-NIC](http://org-id.guide/list/GB-NIC)
* Education establishments - [GB-EDU](http://org-id.guide/list/GB-EDU) and [GB-UKPRN](http://org-id.guide/list/GB-UKPRN)
* Local authorities - [GB-LAE](http://org-id.guide/list/GB-LAE) (England), [GB-LAS](http://org-id.guide/list/GB-LAS) (Scotland), [GB-PLA](http://org-id.guide/list/GB-PLA) (Wales)
* Mutual societies - [GB-MPR](http://org-id.guide/list/GB-MPR)
* HMRC-recognised charities - [GB-REV](http://org-id.guide/list/GB-REV)

If you have a registered number from some other scheme, including overseas registrars, check the [org-id List Locator](http://org-id.guide/) for a list code prefix to use. If the list code prefix you need is not listed, [contact the support team](https://www.threesixtygiving.org/contact/).

If you do not have any external registration numbers for the organisation, use your 360Giving prefix and any internal identifier you have for this organisation. For guidance about how to create unique internal identifiers, [contact the support team](https://www.threesixtygiving.org/contact/).

### Organisations without official registration numbers

Not all organisations have an official registration number to use, including small unregistered groups and individuals.

When there isn’t an official registration number for a recipient then you must provide an internal identifier instead, combining your 360Giving publisher prefix with any internal identifier you have for this organisation. This could be the organisation’s account record reference from your database.

If no account record reference is available, or there are security or privacy reasons that mean this information should not be published, the internal identifier can be created using the recipient name. The name can be turned into an identifier by removing the spaces between words or replacing spaces with dash or underscore.

```eval_rst

.. admonition:: Hint: Example internal organisation identifiers using the publisher prefix and either an account reference from the organisation record or recipient name.


  360Giving publisher prefix: 360G-XYZFunder </br>
  Recipient Org:Name: ABC Recipient </br>
  Account ID: 123456</br>

  If using the account ID: 360G-XYZFunder-123456
  
  If using the recipient name: 360G-XYZFunder-ABC-Recipient

```

```eval_rst

.. admonition:: Additional 360Giving fields for charity and company number

   Because 'Company Number' and 'Charity Number' are so important for analysing grantmaking in the UK, the 360Giving Standard includes additional fields these on their own (without the prefixes), to help users of the data.

   If you have these details, you should fill them in, **in addition to** providing the unique organisation identifier using the method above.
```
