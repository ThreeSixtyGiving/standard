# Governance and Revision Control

## Introduction
The 360Giving Standard has many stakeholders: grantmakers (including charitable trusts and foundations, government, non-departmental public bodies, lottery funders); fundraisers; policy makers and researchers; civil society organisations; and oversight authorities (such as the Charity Commission and HMRC). These stakeholders are primarily in the UK, where 360Giving is based and where it has focused its efforts to date. The needs and interests of these stakeholders are varied. As the 360Giving Standard develops over time, with updated versions and new publishers, it is important that a diverse group of stakeholders are engaged in the process.

This document outlines the governance and revision processes for the 360Giving Standard. It was agreed at a Standard Stewardship Committee meeting on Friday 5th April 2019. The Stewardship Committee must be consulted before any changes are made either to this document or to the governance and revision processes for the 360Giving Standard.

## Version 1.0 and Beyond
The 360Giving Standard was initially developed through an iterative process in 2014, resulting in an initial draft version in February 2015. During 2015, several organisations piloted use of the Standard. During 2017, we worked towards a first version of the Standard, version 1.0, focussing on addressing some issues identified through wider adoption of the Standard during 2015 and 2016. Version 1.0 was released on June 1st, 2018.

This document outlines the process for managing changes to the 360Giving Standard.

## Stewardship and Governance
360Giving was established as an independent non-profit in July 2015, and acts as the lead steward of the 360Giving Standard.

The organisation is led by a Chief Executive Officer (CEO) who is supported by a staff team of two as well as a technical team. The organisation’s activities and governance is overseen by a Board of Directors that includes representatives from across the charitable giving sector.

```eval_rst
The technical team work under contract to 360Giving, providing a help desk service and being responsible for the day-to-day management of the Standard documentation and validation tools. The technical team can be contacted via `support@threesixtygiving.org <mailto:support@threesixtygiving.org>`_.
```

In the pursuit of openness and community-driven process, subscribers to the [360Giving online discussion forum](https://forum.threesixtygiving.org/c/standard) and those engaging with the [Standard GitHub repository](https://github.com/ThreeSixtyGiving/standard) will be kept informed at all stages about planned revisions to the 360 Standard, and will be offered clear and timely opportunities to input and comment.

To ensure the relevance, quality and effective implementation of proposed updates to the Standard, new version releases will be subjected to a process of peer review with invited reviewers from publisher and user communities, and an open review process.

```eval_rst
A Standard Stewardship Committee, made up of representatives from 360Giving staff and Board members, current and potential publishers, end users of 360 data and the technical team, is responsible for giving final approval to formal upgrades of the Standard and ensuring the processes in this document have been properly carried out. [1]_
```

### Intellectual property
The 360Giving Standard is the intellectual property of 360Giving. The schema is provided under a [Creative Commons Attribution 4.0 International License]( https://creativecommons.org/licenses/by/4.0/).

Contributors to the Standard agree to transfer any copyright in their contributions to 360Giving, in order that it is held in trust as part of the Standard. No content infringing upon third-party Intellectual Property Rights will be included in the Standard.

### Governance principles
```eval_rst
We are committed to the `Open Stand principles <https://open-stand.org/about-us/principles/>`_ for standards development. [2]_  The 360Giving Standard has been developed with:
```
* **Due process**: Decisions will be made with equity and fairness among participants. Through an open process for submitting issues, extensions and requests for updates, no one party will dominate or guide standard development. All processes will be transparent and opportunities will exist to appeal decisions. Processes for periodic standards review and updating are well defined in this document.
* **Broad consensus**: The process will allow for all views to be considered and addressed, such that agreement can be found across a range of interests.
* **Transparency**: We will provide advance public notice of proposed standards development activities, the scope of work to be undertaken and conditions for participation. Easily accessible records of decisions and the materials used in reaching those decisions will be provided. Public comment periods will be provided before final standards approval and adoption.
* **Balance**: Standard activities will not be exclusively dominated by any particular person, company or interest group.
* **Openness**: The 360Giving Standard processes are open to all interested and informed parties.

## Versioning and Upgrade Process
Over time, changes will be needed to the Standard, including addition of new codes and fields, and occasionally involving changes to existing fields and structures.

The revision process will ensure:
* The consequences of any change for different stakeholders are identified and considered;
It is clear why changes are needed, and that there is broad support for any proposed changes;
* Changes are easy to identify and are transparent, and publishers, users and intermediaries have clear documentation to allow them to update their data and tools;
* Changes to the 360Giving schema should be made periodically, with the version number of the standard incremented to indicate that changes have been made, and a change-log maintained.
* That backwards compatibility will be maintained wherever possible.

### Versions
Distinct branches of the Standard will be maintained within Github for each version. Branches can be in one of two states:
* Development – indicated by a -dev suffix (e.g. 1.0-dev). Both schema and documentation on a development branch can be updated and should only be implemented on an experimental basis.
* Live – with no suffix (e.g. 1.0). Only documentation updates are permitted on a live branch. All documentation changes must be reviewed to ensure they do not make any changes to the meaning of the Standard.

[Semantic Versioning](https://semver.org/) practices will be used to distinguish between:
* MAJOR versions which make backwards-incompatible API changes; and
* MINOR versions which add functionality in a backwards-compatible manner.
* PATCH version which make backwards-compatible bug fixes.

These are captured by a version number in the format MAJOR.MINOR.PATCH.

### Revision process
To release a new MINOR or MAJOR version upgrade will involve a number of stages outlined in the flowchart below, and described in more depth in the following sections.

![Revision process](https://github.com/ThreeSixtyGiving/standard/blob/new-docs-style/assets/upgrade_process_feb_2016.png)

PATCH version upgrades are a smaller process, in recognition of the low impact that PATCH changes can have on the whole standard. A proposal for a PATCH version upgrade is made via the forum, with the Stewardship Comittee and technical team notified via email. If no objections are received within one week, the PATCH change will be considered approved.

The revision process will follow these general principles:
* **Publicity**: All stages of the revision process will be announced via the 360Giving online forum. This is the formal channel for notification during the process.
* **Consensus**: The process should act in the interest of the data standard, with particular consideration given to what the changes will mean for current publishers. All processes should aim towards gaining community consensus for changes. In cases where consensus cannot be reached, the process will be escalated to the CEO of 360Giving and put to a final majority vote by the Stewardship Committee. The 360Giving technical team are responsible for generating key documentation during the process, but should always be guided by community consensus, submitting all decisions for public discussion.
* **Appeal**: Any party may appeal against decisions made during the process by writing to the Standard Stewardship Committee via the 360Giving discussion forum. The Stewardship Committee has the authority to reject proposed revisions on the Standard in response to appeals.


### Proposals
Changes to the Standard can be proposed by anyone at any point via the 360Giving discussion forum either as issues for discussion, or [pull requests]( https://help.github.com/articles/about-pull-requests/) with a clear description of the proposed change. Contributors are encouraged to raise discussions in order to seek consensus on proposed changes. Changes may be proposed as updated field definitions or codelist entries, or as new features to the Standard.

## Prioritisation
The technical team, with reference to community views, identify change proposals and extensions which should be considered for adoption in the next version of the Standard, assigning these to milestones in the issue tracker on GitHub where they are open for discussion.

Periodically, at the start of a revision process a cut-off date for proposals will be announced with at least two weeks’ notice. After that date, a prioritised list of updates is produced. Any new proposed changes received after this period may not be considered until the next prioritisation phase.

### Prioritisation review
The list is shared on the 360Giving online forum, with at least a two-week window for discussion.

Based on discussions, a final list is then proposed by the technical team with all the issues that will be taken forward into the rest of the process. A proposal that has made it this far may or may not make it into the final upgrade. As the proposal is worked into final concrete examples and schema changes, further issues may arise that mean the original proposal cannot be implemented.

## Development and Documents
The technical team, working with community members, will work on a development branch to prepare updates to the schema, documentation and codelists, according to the prioritised list.

This stage is likely to involve broad community engagement and discussion of specific decisions through GitHub issues.

At the point where all open issues are suitably addressed, the development branch can be submitted for review by the Standard Stewardship Committee.

## Review by the Stewardship Committee
The updated schema, documentation along with a change log and narrative description of the changes will be released for review by the Stewardship Committee. The Committee will be asked to complete a full review of the changes, and to submit to 360Giving’s CEO:
* A judgement on whether the overall upgrade, and/or specific changes should be **accepted, accepted with minor changes, substantially revised** or **rejected**.
* Comments on each request for revisions or rejection.

All reviews and the judgement made will be published. Community members may also submit their own reviews of the whole revision, or specific elements. The minimum period for Committee review is one month.

### Revisions
The 360Giving technical team, with reference to the Standard Stewardship Committee as appropriate, should evaluate reviews and decide whether the whole upgrade, or specific features of it, need to be revised, rejected or postponed to future processes.

If only minor changes are suggested, then the revised Standard can be submitted back to reviewers for a brief review period of at least two weeks. If major changes are required, then a longer follow up review process of at least one month should be allowed for.

### Release
Once all reviewer comments have been addressed to the satisfaction of the reviewer in question, then the updated version of the Standard should be submitted to the Standard Stewardship Committee for final approval, along with a short report of the process.

Following Stewardship Committee approval, the revision branch can be set to live.

## Deprecation Policy
```eval_rst
If a term (a class or property) is scheduled to be renamed or removed from the specification as a result of the revision process, the next release of the specification must deprecate [3]_ the term within the schema, and the following major release must rename or remove the term from the schema, making the term obsolete. Implementations may use deprecated terms, but will receive warnings from the 360Giving Data Quality tool described below. [4]_  Implementations may not use obsolete terms, and will receive errors from the Data Quality tool.
```

## Support Policy
Support will be offered for one prior version of the Standard. Support for any earlier versions than this will be ended when a new version is released. For example, when 1.1 is the latest release, 1.0 will be supported in the Data Quality tool and other relevant tools and platforms managed by 360Giving. When 1.2 is released, support for 1.0 will no longer be guaranteed.

Only the most recent PATCH version for a given MAJOR.MINOR version will be supported. For example, once 1.1.4 is released, 1.1.3 will no longer be supported.

Publishers are encouraged to review each new version when released, and to consider how they might adopt new features. Publishers should aim to move to a new major version within 18 months of its release.

## Definitions
**Stakeholder**
Anyone who is a current or potential publisher or user of the 360Giving Standard can be considered a stakeholder. When engaging with stakeholders, attention will be paid to representation of both publishers and users; representation of public and private sectors and civil society; and broad geographical representation.

```eval_rst
**Consensus**
“The principle of consensus has its origins in the desire to achieve the general acceptance and application of a Standard within its intended sphere of influence. This entails trying to ensure that the interests of all those likely to be affected by it are taken into account, and that individual concerns are carefully and fairly balanced against the wider public interest.” [5]_
```

## Terms of Reference - Stewardship Committee of the 360Giving Data Standard
1. Role of the Committee 

  * 1.1 The Stewardship Committee of the 360Giving Open Data Standard (the “Standard”) oversees and
accounts for the appropriate and timely maintenance of the Standard, including what upgrades are
required and the process for making them.

2. Primary activities
* 2.1 The Committee’s primary activities are to support and provide advice to the Chief Executive of
360Giving on any issues with the Standard and how to address them, including:
* Reviewing the Standard reference template, data and spreadsheet formats and the classifications used.
* Ensuring that the schema documentation remains up to date.
* Reviewing any changes, upgrades or extensions that may be required to the Standard and advising on a process for how and when to address them.
* 2.2 The Committee will review the Standard at minimum on a biannual basis, ensuring that it remains
fit for purpose and guided by principles of good practice for managing open data standards.
3. Appointment of members
* 3.1 It is 360Giving’s aim that the Committee includes a minimum of one member from each of its key
stakeholder groups, including its Board, staff, publishers, open data experts and end users.
* 3.2 Committee members will be appointed through an open and transparent process. Any person
wishing to become a member can nominate themselves and will be appointed on the agreement of
the Chief Executive of 360Giving and in consultation with the other Committee members.
* 3.3 There is no limit on how long members can be appointed for.
* 3.4 Committee members will not receive any financial or other benefit, but they may be reimbursed at
cost for reasonable out-of-pocket expenses (against presentation of supporting receipts) incurred
in relation to attending Committee meetings, or other activities undertaken at the request of the
Chief Executive of 360Giving.
4. Chair
* 4.1 The Committee may appoint one of their members to be the Chair of the Committee for such term
of office as they determine. The Chair will be appointed by a majority vote of the Committee. The
Chair will advise the Chief Executive of 360Giving on appropriate maintenance of the Standard and
on the approval of the Committee.
* 4.2 The Chair cannot be a paid employee of 360Giving.
5. Committee proceedings
* 5.1 The Committee will meet every six months to review the 360Giving data standard, formats and
classifications and to discuss whether any changes or upgrades are required.
* 5.2 The Committee is expected to meet in person at least once per annum.
* 5.3 The Chair shall convene and preside over all Committee meetings, coordinating with the Chief
Executive of 360Giving as required to ensure that members receive relevant documentation in
advance. Additional meetings may be convened at the request of two Committee members. In the
Chair’s absence, another member can be nominated by those present to preside.
* 5.4 At all times the Committee will work to promote, support and uphold the principles of transparency
in its activities by making full and accurate information about its activities and proposals publicly
available so that anyone can review them.
These Terms of Reference were prepared on 16th August 2016 by 360Giving and approved by members at the
inaugural Stewardship Committee meeting on 1st December 2016.
6. Conflicts of interest
* 6.1 Committee members are to declare any direct or indirect interest (whether personal, or by a duty of
loyalty to another organisation) that conflicts, or might conflict with the interests of 360Giving and
the appropriate maintenance of the Standard at the outset of any discussion on the relevant issue.
* 6.2 Any declaration of a conflict of interest is to be noted in the public record of discussions, together
with details of any proposals made.
7. Individual member’s responsibilities
* 7.1 Committee members will at all times:
Remain appropriately informed on 360Giving’s open data Standard and operating environment.
Endeavour to attend all Committee meetings, ensuring that they are adequately prepared to contribute
to the discussion.
Exercise independence of judgment, acting legally and in good faith to promote and protect 360Giving’s
interests.
Contribute to the broader promotion of 360Giving’s objects, aims and reputation through the
application of their skills, expertise, knowledge and contacts.
* 7.2 Members shall at all times have unrestricted access to all information, records and documents
relevant to the 360Giving Standard.
8. Amendments
* 8.1 The Committee shall periodically review these Terms of Reference to ensure they remain relevant to
and are consistent with 360Giving’s overall strategy and goals. It will advise the Chief Executive of
any recommended changes to the Terms of Reference and/or its membership. 

----------

```eval_rst
**Footnotes**

.. [1]  For a list of current Stewardship Committee members and their Terms of Reference, visit: https://www.threesixtygiving.org/governance-of-the-360giving-standard/.
.. [2] See https://open-stand.org/about-us/principles/.
.. [3] See https://en.wikipedia.org/wiki/Deprecation
.. [4] See https://dataquality.threesixtygiving.org/.
.. [5] See Pocket Guide to Standards Development, the British Standards Institution, 2012, p.9: https://www.bsigroup.com/Documents/about-bsi/NSB/BSI-pocket-guide-to-standards-development-UK-EN.pdf.
```
