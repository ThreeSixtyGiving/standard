# Identifiers

```{eval-rst}

.. admonition:: Why identifiers matter

  Identifiers are an important part of any dataset. They let a computer uniquely identify and refer to specific grants, organisations, individuals, transactions and so-on.

  Whilst a human being may be good at recognising that “R S P B”, “Royal Society for the Protection of Birds” and “The RSPB” all refer to the same organisation, computers cannot make this connection unless a unique identifier is provided.

```

The 360Giving Data Standard asks you to give identifiers to any of the following elements that you include in your data:

* [Grants](#grant-identifier)
* [Organisations](#organisation-identifier);
* [Individuals](#individual-identifier)
* Transactions;
* Classifications;
* and other unique elements in your data.

These go in an `Identifier` column alongside accessible text descriptions of the grant, the name of an organisation, or the title of a classification.


```{eval-rst}
.. _creating-identifiers:
```

## Identifier basics

You may already have identifiers in your own data. For example, a number for each application or grant. You can use these existing **internal identifiers** as part of your published data.

However, to avoid overlap between the internal identifiers you use and the internal identifiers another funder uses, you need to add a **prefix**.

```{eval-rst}
.. admonition:: For example

  If Indigo Trust have a grant called 'Grant27', and the Dulverton Trust also have a grant called 'Grant27' the two will get confused when combining the two datasets. But if, when publishing, each one adds a prefix, then we end up with two unique identifiers: '360G-indigotrust-Grant27' and '360G-dulverton-Grant27'
```

For grants, and other identifiers particular to your organisation, you use can use a **360Giving prefix**.

For organisation identifiers, we strongly encourage you to use an officially recognised identifier for the organisation, following the [organisation identifier](organisation-identifier) guidance below.


```{eval-rst}
.. _register-prefix:
```

## Get your prefix

To register a prefix for your organisation see the [publisher guidance.](../../guidance/prepare-data)

All registered prefixes should start with 360G.
```{eval-rst}
.. _grant-identifier:
```

## Grant Identifier

To create your grant identifiers:

1. Make sure you have asked for a 360Giving prefix.
2. Look for an existing internal identifier given to your grants (for example, a sequential number assigned to each grant at the point of application). The important thing is that the identifier should be unique **inside your organisation**, so adding the prefix will make it unique across the whole world.
3. Add your 360Giving prefix in front of your identifier.

```{admonition} For example
If your prefix is `360G-xyztrust` and you have a grant identified internally as `123`, you would combine these to give `360G-xyztrust-123`
```

We recommend using a hyphen (-) for the separator to use between your prefix and the internal identifier. Avoid using slashes (\ and /) as these can cause problems with some applications.

If your internal identifiers include spaces or special characters, we recommend replacing these with underscore (_):

`360G-xyztrust-123_ABC`

```{hint}
If you do not have a unique grant reference to use you will need to create identifiers. You can use sequential numbers. Also including the year in which the grant was awarded helps to group the grants and makes it possible to restart the sequential numbers at the beginning of each year.

You can use any reference you choose as long as it is unique within your organisation. The 360Giving prefix will then be added to make the identifier globally unique.

```

### Considering privacy and security

Grant identifiers taken from internal systems are specific to each grant and can be linked to each recipient. If grant identifiers are used as credentials to give access to grant assessment or reporting systems, or the grant recipient is an individual, it may not be appropriate to include these in open data. If there are privacy or security concerns associated with your existing grant identifiers, you will need to create these instead.

```{eval-rst}
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

In 360Giving data we ask publishers to use a list code prefix taken from the <a href="https://org-id.guide/" target="_blank"> org-id list locator</a>. This provides an open, maintained list of codes for many different lists around with world, giving a way to identify almost any organisation.

```{admonition} For example
A charity registered in England and Wales with the Charity Commission of England and Wales, with the charity number '1164883' will use a list code prefix of `GB-CHC`.
```

```{hint}
UK company numbers are a unique combination of eight digits, which in some cases include letters as well as numbers. The majority of company numbers for companies registered in England and Wales start with a **leading zero**.

Publishers should be aware of the problems that missing leading zeros in UK company numbers present when creating identifiers. [Learn more](https://www.360giving.org/company-numbers/) about how to avoid this pitfall.
```

### Choose the best identifier

Some organisations have more than one identifier: they might be a charity **and** a company (charitable companies), or a charity **and** an educational establishment.

If you have more than one type of identifier for an organisation recorded in your system, it will be necessary to pick which one to use when creating an Organisation identifier.

<a href="https://org-id.guide/" target="_blank"> org-id.guide</a> ranks identifier lists by relevance and quality to help you pick the best identifier, based on what information you hold.

```{admonition} Relevance and quality defined
:class: hint

* Relevance: are you likely to find the organisation you are looking for in this list?
* Quality: are the identifiers in this list stable and linked to open, accessible contextual data, and can they be easily mapped to other identifiers.
```

Search on <a href="https://org-id.guide/" target="_blank"> org-id.guide</a> for identifier sources for <a href="https://org-id.guide/?structure=&coverage=GB&subnational=&sector=" target="_blank"> UK organisations</a>, <a href="https://org-id.guide/?structure=charity&coverage=GB&sector=" target="_blank"> UK charities</a>, or <a href="https://org-id.guide/" target="_blank"> any other organisation type</a>.

### Commonly used identifier lists

The following identifier lists are often used in 360Giving publication.

* UK Company Number - <a href="https://org-id.guide/list/GB-COH" target="_blank">GB-COH</a>
* Charity Numbers - <a href="https://org-id.guide/list/GB-CHC" target="_blank">GB-CHC</a> (Eng & Wales), <a href="https://org-id.guide/list/GB-SC" target="_blank">GB-SC</a> (Scotland), <a href="https://org-id.guide/list/GB-NIC" target="_blank">GB-NIC</a> (Northern Ireland)
* Education establishments - <a href="https://org-id.guide/list/GB-EDU" target="_blank">GB-EDU</a> and <a href="https://org-id.guide/list/GB-UKPRN" target="_blank">GB-UKPRN</a>
* Local authorities - <a href="https://org-id.guide/list/GB-LAE" target="_blank">GB-LAE</a> (England), <a href="https://org-id.guide/list/GB-LAS" target="_blank">GB-LAS</a> (Scotland), <a href="https://org-id.guide/list/GB-PLA" target="_blank">GB-PLA</a> (Wales), <a href="https://org-id.guide/list/GB-LANI" target="_blank">GB-LANI</a> (Northern Ireland)
* Mutual societies - <a href="https://org-id.guide/list/GB-MPR" target="_blank">GB-MPR</a>
* HMRC-recognised charities - <a href="https://org-id.guide/list/GB-REV" target="_blank">GB-REV</a>

If you have a registered number from some other scheme, including overseas registrars, check the <a href="https://org-id.guide/" target="_blank"> org-id List Locator</a> for a list code prefix to use. If the list code prefix you need is not listed, contact 360Giving Helpdesk via <support@threesixtygiving.org>.

### Organisations without official registration numbers

Not all organisations have an official registration number to use, including small unregistered groups and excepted charities.

When there isn’t an official registration number for a recipient then you must provide an internal identifier instead, combining your 360Giving publisher prefix with any internal identifier you have for this organisation. This could be the organisation’s account record reference from your database.

If no account record reference is available, or there are security or privacy reasons that mean this information should not be published, the internal identifier can be created using the recipient name. The name can be turned into an identifier by removing the spaces between words or replacing spaces with dash or underscore.

```{hint}
Example internal organisation identifiers using the publisher prefix and either an account reference from the organisation record or recipient name.

360Giving publisher prefix: 360G-XYZFunder

Recipient Org:Name: ABC Recipient

Account ID: 123456

If using the account ID: 360G-XYZFunder-123456

If using the recipient name: 360G-XYZFunder-ABC-Recipient
```

### Additional 360Giving fields for charity and company number

Because 'Company Number' and 'Charity Number' are so important for analysing grantmaking in the UK, the 360Giving Data Standard includes additional fields these on their own (without the prefixes), to help users of the data.

If you have these details, you should fill them in, **in addition to** providing the unique organisation identifier using the method above.

(individual-identifier)=
## Individual Identifier

In the 360Giving Data Standard, each individual recipient must have a unique identifier. However, unlike Organisation Identifiers, the reference used to identify the individual must not refer to official sources of data about the person for privacy and security reasons.

For example if the National Insurance number of a recipient is known to the funder, this information **MUST never** be published in 360Giving data.

The Recipient Ind:Identifier should be constructed using the 360Giving Publisher prefix starting 360G, followed by a unique reference.

```{hint}
360Giving publisher prefix: 360G-XYZFunder

Individual Identifier: 123456
   
Recipient Ind:Identifier = 360G-XYZFunder-123456
```

### Considering privacy and security

Individual identifiers taken from internal systems are specific to each recipient and could be used to identify that person. When these identifiers are securely held and are only accessible to people who are authorised to access the grant recipient’s personal data, then it can be appropriate to publish these in 360Giving data.

However, if the system identifiers are shared with third parties alongside recipient names or other personal details as part of the grantmaking process - for example with referral agencies, or as part of monitoring and reporting - then these could be used to identify people in your 360Giving data.

If there are any privacy or security concerns associated with your system identifiers, you should create these instead using random or sequential numbers.
