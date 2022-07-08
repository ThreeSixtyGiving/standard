# Governance and Revision Control

## Introduction

The 360Giving Data Standard was initially developed through an iterative process in 2014, resulting in an initial draft version in February 2015. Over the next three years as organisations started to use the standard, we worked towards a first version of the Standard, addressing some issues identified through its wider adoption. Version 1.0 was released on 1st June 2018.

The 360Giving Data Standard has many stakeholders: grantmakers (including charitable trusts and foundations, local and central government, non-departmental public bodies, lottery funders); fundraisers; policy makers and researchers; civil society organisations; and oversight authorities (such as the UK charity regulators).

Our vision for the Standard is that it helps UK funders to share consistent, high-quality data about grants so the sector is able to use this information to support effective decision making. In order to achieve this the Standard needs to be maintained and upgraded to meet the needs of users, and the community will be actively engaged in informing and shaping it.

This document outlines the governance and process for managing changes to the 360Giving Data Standard.

## Governance of the Standard

### About 360Giving

The 360Giving Data Standard is managed and maintained by 360 Giving (Trading as 360Giving), a registered charity (number 1164883) and a registered company (number 09668396).

Our vision is for grantmaking in the UK to become more informed, effective and strategic.

Our aim is for more money to go to where it is needed most to support communities and good causes through a more informed understanding of the grantmaking picture.

Our mission is to help UK funders publish their grants data in an open, standardised way, and support people to understand and use this data to improve charitable giving.

The strategy for the Standard is a core part of the 360Giving strategy. The 2022-25 strategy – [Unleashing the Impact of Grants Data](https://www.threesixtygiving.org/about/unleashing/) – aims to shift the norm from funders sharing data to using it, and create a permanent transformation in data culture and practice.

During this strategy period, the Standard will remain focused on the needs of UK grantmakers. While international grants can and are published using the Standard, the data and needs of international funders can be better met through [IATI](https://iatistandard.org/en/) and other standards and products.

For further information about 360Giving visit: [https://www.threesixtygiving.org/about/](https://www.threesixtygiving.org/about/)

### Governance

360Giving is the steward of the 360Giving Data Standard. Our CEO is responsible for its day-to-day management, supported by a Product Manager and an external specialist technical team, [Open Data Services Coop](https://opendataservices.coop/).

The 360Giving Board of Trustees are responsible for setting the strategy of the charity and Standard, and both the Board and CEO are supported in the maintenance and development of the Standard by the 360Giving Data Standard Stewardship Committee.

#### The Stewardship Committee

It is the Stewardship Committee’s role to oversee and account for the appropriate and timely maintenance of the Standard, including what upgrades are required and the process for making them.

The Committee meets two to four times a year to discuss the Standard schema, look at how it is being used and consider any proposed changes or upgrades. This is a voluntary committee with representatives from 360Giving staff and Board, grantmakers, users of 360Giving data and open data and standards experts, with an independent Chair.

Secretarial support is provided to the Committee by 360Giving. The Committee is responsible for recommending formal upgrades of the Standard to the CEO and Board of 360Giving and ensuring the governance and revision process has been properly carried out.

For further details see the [current membership of the Stewardship Committee](https://www.threesixtygiving.org/support/standard/) and the [Terms of Reference](../../about/sc-tor). To contact the Stewardship Committee please email standard@threesixtygiving.org.

#### Guiding principles

Our principles for the 360Giving Data Standard are:

##### 1. Accessible
It has a low barrier of entry for publishers with a minimum number of required fields to be effective and inclusive to a range of funders. The Standard is described by a [JSON schema](https://json-schema.org/); however, we allow users to share data in spreadsheets and provide tools to convert data between formats to increase adoption and support organisations with a wide range of data maturity.

##### 2. Flexible
It allows for the publication of non-Standard fields alongside the official fields, so individual funders, or groups of funders, can tailor their data for their specific needs.

##### 3. Extendable
It can be extended to allow expansion of the information being shared in a consistent way and provide support for collaborations and collective activities.

##### 4. Interoperable
It uses internationally recognised standards in its data formatting and codelists. As far as is possible it aims to enable links to other standards and registers.

##### 5. Responsive
It is adaptable, allowing an element of continuous improvement to meet emerging needs.

##### 6. Usable
The data published using the Standard should be relevant, understandable by others and usable. 

#### Intellectual property

The 360Giving Data Standard is the intellectual property of 360Giving. The schema is provided under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Contributors to the Standard agree to transfer any copyright in their contributions to 360Giving, in order that it is held in trust as part of the Standard. No content infringing upon third-party Intellectual Property Rights will be included in the Standard.

### Versioning and Upgrade Process

To maintain the usefulness of the Standard, upgrades can be made to add new codes and fields, or occasionally make changes to existing fields and structures.

We take proactive approaches to identify opportunities to develop the Standard, as well as providing ways for stakeholders to provide feedback.

#### The revision process

We are committed to the [Open Stand principles](https://open-stand.org/about-us/principles/) of standards development; due process, broad consensus, transparency, balance and openness.

The 360Giving Data Standard revision process will ensure that:
* The consequences of any change for different stakeholders are identified and considered; it is clear why changes are needed, and that there is broad support from the impacted stakeholders for any proposed changes;
* Proposed changes are publicised, explained in non-technical terms and made using a transparent process, and all decisions and changes are made available for future reference.
* Publishers, users and intermediaries are provided with clear documentation about changes to allow them to update their data and tools;
* Changes to the 360Giving schema are made periodically, with the version number of the standard incremented to indicate that changes have been made;
* All notable changes are documented by Release via the [Changelog](https://github.com/ThreeSixtyGiving/standard/releases);
* Backwards compatibility is maintained wherever possible.

#### Identifying issues and proposals for upgrades

Issues and bugs, ideas for new features, and proposals for upgrades to the Standard can be identified in a range of ways.

This includes feedback generated by use of the Standard by publishing organisations and data users, user research and feedback from surveys, through engagement with sector bodies and networks and learning from other open data standards.

Ideas and upgrades can also be proposed by anyone at any point via the [360Giving discussion forum](https://forum.threesixtygiving.org/c/standard/5) as an issue for discussion, or by raising an issue or [pull request](https://help.github.com/articles/about-pull-requests/) on the [Standard GitHub repository](https://github.com/ThreeSixtyGiving/standard) with a clear description of the proposed change.

Issues can also be raised by contacting 360Giving directly at standard@threesixtygiving.org.

#### Involving stakeholders in Standard development

Our stakeholders include the funders who publish using the 360Giving Data Standard, the recipients of grants described by 360Giving data and data users, such as data analysts and developers.

Proposals to upgrade to the Standard can be explored through a variety of methods depending on the impact and nature of the proposed changes.

User engagement in the development of, and consultation on proposals, may involve:
* Working groups of stakeholders;
* Surveys, focus groups and individual interviews;
* Commissioned or in-house research.

Substantial developments, such as adding an Extension focused on specialist areas of funding practice, are likely to be developed in collaboration with networks or groups involving a range of stakeholders, to ensure the right level of engagement, consultation and subject expertise.

#### Prioritisation

The issues and proposals raised through all channels will be prioritised by considering user needs and demand, and will be guided by [360Giving strategy](https://www.threesixtygiving.org/about/unleashing/) and [values](https://www.threesixtygiving.org/about/our-values/).

#### Versions

The Standard uses Semantic Versioning [1]_ to distinguish between:

* MAJOR versions which make backwards-incompatible changes,
* MINOR versions which add functionality in a backwards-compatible manner, and
* PATCH versions which make backwards-compatible bug fixes.

These are captured by a version number in the format MAJOR.MINOR.PATCH.

If a change is backwards-compatible, this means that any data shared using an earlier version of the Standard will still meet the requirements of the Standard. Tools developed to use an earlier version should also still function as expected.

If a change is backwards-incompatible – also known as a ‘breaking change’ – data shared using earlier versions will no longer meet the requirements of the Standard, and tools may stop working as expected.

Not all parts of the Standard are used by all publishers and users of the data, so the impact of a backwards-incompatible change could be focused on a subset of publishers and users who are using those specific parts, but leave others unaffected.

##### Examples of version upgrades

###### MAJOR
In [October 2017, a proposal](https://forum.threesixtygiving.org/t/proposals-for-change-date-formats/46) was made to upgrade the schema, documentation and guidance to ensure Last Modified fields use [date-time formatting](../../technical/reference/#dates-and-times), which includes both a date and time component – YYYY-MM-DDThh:mm:ss. The impact of this change was that Last Modified dates using the date format – YYYY-MM-DD – would no longer meet the requirements of the Standard, making this a backwards-incompatible change. The upgrade was recommended for approval by the Stewardship Committee in March 2018, and the data publishers impacted by the changes were supported to update their data prior to the change being made live, as part of the release of [Version 1.0.0](https://github.com/ThreeSixtyGiving/standard/releases/tag/1.0.0) in June 2018.

###### MINOR
In [November 2020, a proposal](https://forum.threesixtygiving.org/t/minor-peer-review-of-metadata-update-available-for-comment/375) was made to upgrade the schema and documentation to add fields for publishing [Metadata](../../technical/metadata) into the 360Giving Package schema. Metadata is data about the data - for example when it was last updated, when it was released for publication, which organisation published it and which version of the 360Giving Data Standard was used, etc.  The impact of this change was that data publishers could start to include authoritative Metadata about their data and organisation in their 360Giving data files. The proposal added new fields but did not change any existing fields or formats, making this a backwards-compatible change which did not affect existing data or publishers. The upgrade was recommended for approval by the Stewardship Committee in January 2021 and the MINOR upgrade was made live and released as [Version 1.1.0](https://github.com/ThreeSixtyGiving/standard/releases/tag/1.1.0) in April 2021.

###### PATCH
In [November 2021, a proposal](https://forum.threesixtygiving.org/t/patch-updates-to-360giving-schema-and-package-schema/393) was made to amend the description text in the 360Giving Grants Schema to make it clear that the country code field uses the 2 character ISO-3166-1-alpha-2 codelist. The impact of this change is that data publishers and users were provided with clearer guidance about the requirements of this field. The proposal resolved an issue with the description being ambiguous but it did not add new fields or change any existing fields or data formats, making this a backwards-compatible bug fix. This change, along with a package of other PATCH changes were recommended for approval by the Stewardship Committee in December 2021, and the change was made live and released as [Version 1.1.1](https://github.com/ThreeSixtyGiving/standard/releases/tag/1.1.1) in December 2021.

#### Approval of upgrades

The Stewardship Committee has oversight of consultation processes to ensure that the needs of a range of stakeholders have been considered and are responsible for recommending upgrades to 360Giving’s CEO and Board for approval.

Once a change has been identified and developed through user engagement and consultation, a new proposal for a MINOR or MAJOR upgrade will be presented to the Stewardship Committee, at the next available meeting.

The committee will be asked to complete a review of the changes, and make a recommendation that a proposal should be accepted; accepted with minor changes; substantially revised or rejected.

The proposals, committee recommendations and comments or requests for revisions will be published alongside minutes of Stewardship Committee meetings on the [360Giving forum](https://forum.threesixtygiving.org/c/standard/5).

#### MAJOR versions and Extensions

To release a new MAJOR version upgrade or adding an Extension to the Standard, which are developments which can have a significant impact on users of the Standard, in addition to carrying out a process which considers the impact on users and consults with stakeholders as outlined above, the proposals will also be reviewed and approved by the 360Giving Board.

#### Final review and release

Once a proposal has been recommended by the Stewardship Committee and approval confirmed by 360Giving’s CEO or Board, the changes will be made to a development branch of the Standard and documentation. A development branch represents a package of changes being implemented at the same time and may include changes to the Standard, templates and guidance. This allows for a full review of the changes before final approval is given to make the upgrade to the Standard.

For MINOR upgrades, the development branch will then be made available for review for a period of at least two weeks. For MAJOR upgrades the review period will be at least one month. 

Following final approval, the development branch can be set to live.

#### PATCH versions

In recognition of the low impact that PATCH changes can have on the whole Standard, a proposal for a PATCH version upgrade is made via the 360Giving forum, with the Stewardship Committee and technical team notified via email. If no objections are received within one week, the PATCH change will be considered approved.

#### Changelog

All notable changes are documented by Release via the [Changelog](https://github.com/ThreeSixtyGiving/standard/releases).

### Deprecation Policy

If a term, such as a field title (known as a class or property in JSON schema) is scheduled to be renamed or removed as a result of the revision process, the next release must [deprecate](https://en.wikipedia.org/wiki/Deprecation) the term within the schema. The following MAJOR release must rename or remove the term from the schema, making it  obsolete. Data that is published  may use deprecated terms, but will receive warnings from the [360Giving Data Quality tool](https://dataquality.threesixtygiving.org/). Data that is published may not use obsolete terms, and will receive errors from the Data Quality Tool.

### Support Policy

When a new version upgrade is made to the Standard, support will be offered for one prior version. Support in this context means that data published using this version is recognised as meeting the requirements of the Standard and will be accepted by the 360Giving Data Registry, Data Quality Tool and other tools managed by 360Giving that use 360Giving data. This means that deprecated terms are supported but obsolete terms are not.

Support for any earlier version than this will not be guaranteed when a new version is released.

MAJOR version upgrades are backwards-incompatible and will therefore cause disruption for some publishers and users. MAJOR changes will have a proposed implementation timescale to allow users of the Standard or data to make amendments to systems and data, and will set a deadline for the retirement of the older versions.

As both PATCH and MINOR version upgrades are backwards-compatible, publishers and users will not experience disruption in their use of the Standard, even if they have not started using the features introduced through these types of upgrades. However publishers are encouraged to consider how they might adopt new features as they are introduced.

Publishers and users will be provided with notice of MAJOR upgrades and provided with guidance and support where appropriate to make a transition to using the new version, which they should aim to do within 18 months.

.. [1] Semantic Versioning is used in software management to keep track of developments by applying a version numbering system. Further information can be found at the [Semantic Versioning](https://semver.org/) website.
