# Guide to regranting
## Introduction
The 360Giving Data Standard allows funders to describe grants that are intended for onward distribution through the use of the **For Regrant Type** field and **Regrant Type** codelist. This guide explains how to use the codelist when publishing data about these kinds of grants.

## About the codelist
The codelist includes seven codes that should be used to identify that a grant is intended for regranting. All the codes represent types of grants intended for redistribution, each describing the different ways that funders can redistribute funding or contribute to funds for redistribution. The codelist includes the most frequently used ways that grants are redistributed, as well as some less common but significant types.

### Regrant Type codelist

```eval_rst
.. csv-table::
   :file: ../../codelists/regrantType.csv
   :header-rows: 1
   :widths: auto
```
### Explanation of terms

**Donor funder**

In this guidance, the term ‘donor funder’ is used to describe the funder giving the grant intended for redistribution. This means the funder that is named and identified by the 360Giving data fields **Funding Org:Name** and **Funding Org:Identifier**. For the purposes of deciding which code to use, the funder described in the 360Giving data will be considered to be the ‘donor funder’ even if the original source of the funding is from a grant they have themselves received.

**Recipient and End Recipient**

In this guidance, the term ‘recipient’ is used to describe the organisation in direct receipt of the grant intended for redistribution. This means the recipient that is named and identified by the 360Giving data fields **Recipient Org:Name** and **Recipient Org:Identifier**. The guidance also uses the term ‘end recipient’, which means the organisations or individuals that are expected to receive the redistributed funding. The end recipients will not appear in the structured data of the grant record, but they may be described in general or specifically in the title or description fields. The end recipients may also appear elsewhere in 360Giving data if the recipient of the grant intended for redistribution has published the onward grants.

#### FRG010 (Common regrant)
When to use this code:
Grants given by a single funder to a single organisation, for the purpose of distribution as grants.
This is the most common form of grant for regranting. Examples might involve a grant given to a specific programme in which the “donor funder” is involved in the decision-making process for awarding the grants. The grant could also be a contribution to a fund, where the “donor funder” has no involvement in the decisions about how the funds are distributed.

#### FRG020 (Transfer to intermediary)
When to use this code:
Grants awarded to a membership network or federated charity, for the purpose of being distributed to connected organisations.
The recipient might distribute the funds in the form of grants, or direct payments. The funding received by the connected organisation is intended for redistribution as grants, and may include grantmaking administration and costs: it isn’t necessary to separate these out into a separate grant.

#### FRG030 (Match funding)
When to use this code:
Grants awarded to one other funder, which are matched by that other funder and then distributed as grants to end recipients. The match could be any ratio (it does not have to be 50/50).
This code should be used when there is coordination between the two or more funders involved in the match, with one responsible for onward distribution of the grants.
This code ***should not be used*** for a grant awarded to a recipient on the condition that match funding is raised from other sources.

#### FRG040 (Funder collaboration)
When to use this code:
Grants awarded to a pooled fund or funder collaboration.
The grants may be awarded to one of the participating funders, or to a third party organisation that is responsible for making the grants from the pool of funding. The donor funders are likely to be involved in decision-making about the grants awarded.
Grants awarded to a general appeal fund – which may have multiple funders contributing to the same fund – should be coded as **FRG010 (Common regrant)** if the donor funder does not have any decision-making role in the onward distribution of the funds.

#### FRG050 (Fiscal sponsor)
When to use this code:
Grants awarded to an organisation, which acts as fiscal sponsor or hosting organisation on behalf of the intended end recipient of the donor funder.
This code could be used when a transaction is made to an organisation to distribute payments, but the donor funder has specified the recipients. This is sometimes used to fund campaigns or grassroots initiatives or to fund overseas organisations.
This code should only be used when the recipient named and identified in the **Recipient Org:Name** and **Recipient Org:Identifier** fields is the fiscal sponsor/agent organisation. If the publisher names the ultimate end recipient in the Recipient Org fields, the grant should not be coded using any **Regrant Type** code, unless it is given with the intention of redistribution by the end recipient.

#### FRG060 (Endowment)
When to use this code:
Grants which are given in order to set up a new grantmaking organisation or fund, or make a substantial transfer of funds to an existing organisation for grantmaking. These grants may represent a capital investment (the investment the organisation uses to generate income) or spend (the running costs of the organisation), as well as grant-distribution over a significantly longer period of time. 
This type of grant intended for redistribution is different from **FRG010 (Common regrant)** because of the size of the award and the time scales intended for the funds to be distributed as grants.

#### FRG070 (Multipurpose)
When to use this code:
Grants where a proportion of the amount is intended for onward distribution as grants, but a proportion is also to fund other activities carried out by the recipient that don’t relate to grantmaking.
Grants awarded for regranting that include the administration costs of the recipient managing the distribution should not be classed as multi-purpose, unless the funding is also contributing towards activities that aren’t related to regranting. Grants for regranting which also include administration costs for the recipient to manage the grants should be coded with any other appropriate code in this list.

### Still not sure which code to use?
The code descriptions and guidance provide examples of which codes to use to categorise types of grants for regranting. If the grant you want to categorise could fit into more than one category, please label using the primary type.
If you are still not sure which category is appropriate for your grant contact <support@threesixtygiving.org> for further guidance.

## Sharing further information about your grants for redistribution
The **Regrant Type** code list provides a consistent and comparable way to identify your grants as being intended for redistribution. 
Alongside the codes, it is recommended that you use other 360Giving Data Standard fields, such as **Description**, **Title** or **Grant Programme:Title** to provide more detail about the intended end recipients or other funders involved in a funder collaboration.

### Examples
- **Title:** For regranting to small charities and grassroots
    - **Grant Programme:Title:** Community Grant Partners
    - **Description:** Grant to the Local Resilience Fund for redistribution as small grants of between £500 and £5,000 to charities and grassroots organisations supporting local communities in Birmingham.

- **Title:** Funding for women’s organisations
    - **Description:** Grant to provide three-year sustainable funding to specialist women's organisations, particularly focused on those led by and for Black and minoritised women.

- **Title:** Youth Fund
    - **Description:** To be distributed as grants to organisations providing support to young people based in and benefiting young people in Cheshire and Merseyside.

- **Title:** Funding to address fuel poverty
    - **Description:** For distribution as grant payments to individuals and households at risk of fuel poverty in Worcestershire. Priority given to people under the age of 65 living in rural areas.

- **Title:** Match funding
    - **Description:** Contribution to 50/50 match funding for onward distribution to specialist infrastructure organisations to be spent on business support to develop new operating models and business plans.

- **Title:** Capital grants for distribution as grants by Partner Funder
    - **Description:** Capital funding for the installation of accessible toilets in village halls and community centres in Cambridgeshire; to be awarded by Partner Funder under the 2023 grant programme.

## Who should use the Regrant Type codelist?
The responsibility for using the codelist sits with the “donor funder” giving the grant intended for redistribution. This means the funder that is named and identified by the 360Giving data fields **Funding Org:Name** and **Funding Org:Identifier**.
Funders that receive grants for onward distribution as grants are not expected to use this codelist, except in cases where they are also awarding grants that are intended for redistribution. 
Grants awarded to recipients to fund projects and activities **must not** be categorised using this codelist: the field should be left blank or not supplied.
## Guidance on using the codelist
Read our guidance about [how to use the codelists](../technical/codelists) for further information about how to add the For Regrant Type field and Regrant Type codes to 360Giving data.
