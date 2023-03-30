# Publisher Guidance
## Introduction
The following guidance covers the first two stages of the 360Giving publishing process, **planning** (including **data protection**) and **preparing the data**. The section on preparing the data is supplemented by detailed guidance on using **Data preparation templates** that have been set up to support funders of grants to individuals to format their grant information into 360Giving data.

The final stages in the 360Giving publishing process involve [checking data quality](../../guidance/data-quality/) and [publishing the data openly](../../guidance/publish-data-openly/). As these steps are applicable to all types of grants and funders further information about these steps can be found in the [complete guide to publishing.](../../guidance/)
## Plan your process and data
All funders need to [decide what fields of information to publish.](../../guidance/plan-the-process/#decide-what-information-to-share) The full 360Giving Data Standard is comprehensive, with over 100 fields available to describe information about grants, recipients, funding organisations, programmes, locations and more. 

To ensure that the privacy and confidentiality of recipients is protected, funders of grants to individuals have a smaller range of fields to choose from, as well as restrictions on the types of information that can be shared in certain fields.

Funders also need to [decide what grants to include](../../guidance/plan-the-process/#decide-what-information-to-share/decide-what-information-to-share/#decide-what-grants-to-include), in terms of time period and programmes, choices which can be informed by the availability and quality of the data, and the usefulness of sharing information about historical grants.
<div class="box box--teal">
    <h3 class="box__heading">What counts as a grant to an individual?</h3>
    <p>The 360Giving Data Standard can be used to share data about grants to individuals and families, paid as money, in the form of cash or vouchers or goods or services that have been purchased for a specific individual or family. Gifts in kind that do not have a monetary value or benefit to a specific individual or family are not normally suitable for sharing as 360Giving data.</p></div>
    
## Field guidance
### 10 core fields
There are **10 core fields** of information which all 360Giving grant data about individuals must include. These fields ensure that the data will be usable and describe the **who, what, when and how much** of each grant:
- Identifier
- Title
- Description
- Currency
- Amount Awarded
- Award Date
- Recipient Ind:Identifier
- Recipient Ind:Name
- Funding Org:Identifier
- Funding Org:Name

**Recipient Ind:Identifier** and **Recipient Ind:Name**, grant **Identifier** and **Title** and **Description** should be populated in ways that ensure the privacy and confidentiality of recipients is protected.
#### Identifier
The unique identifier for this grant. Usually the identifier is constructed using the 360Giving Publisher prefix starting **360G** with the unique application or grant reference taken from a grants management system, separated by dashes, for example: **360G-ExampleFunder-123**

If there are data protection reasons why the unique identifiers cannot be taken from internal systems, they will need to be created instead. Read our [Grant Identifier guidance](../../technical/identifiers/#grant-identifier) for further information.
#### Title
A title for this grant activity, which should be generic to avoid the text identifying the recipient. The title should be under 140 characters long.
#### Description
A short description of this grant activity (no character limit). The description text is a summary description of the purpose of each grant, and provides an opportunity to let users know why you made the award. Searching **Title** and **Description** text is one of the main ways that users of 360Giving data identify what is being funded.

Descriptions for grants to individuals should be generic to avoid the text identifying the recipient. If no suitable grant description text is available, text describing the overall grant programme could be used instead.
#### Amount Awarded
The full amount awarded when the funding decision was made. This means multi-year grants show the total amount committed, whether the funds have been fully paid out yet or not.
Amount Award should be just numbers, without commas or currency symbols such as £.
#### Currency
Currency is split from the amount and uses a three letter code. **GBP** is used to represent British Pounds.
#### Award Date
When the decision to award this grant was made. Dates must be in **YYYY-MM-DD** format.

Usually the **Award Date** is the grants panel or trustee board meeting date when the grant was approved. If this information is not available, the grant payment date can be used instead.

When there is no precise award date available, a proxy date may be used instead. This could be the first or last day of the quarter or financial year in which the award was made.

**Award Date** should always be in the past. If an award date is in the future, this may be caused by a typo in the date, or the data includes grants that are not yet fully committed (and therefore not suitable for inclusion in 360Giving data).
#### Recipient Ind:Name
The individual recipient of the grant is expected to be anonymous. 

This field must not be blank and it is recommended that the generic text ‘**Individual Recipient**’ is used to ensure the privacy of the person receiving the funding.
#### Recipient Ind:Identifier
A globally unique identifier for this grant recipient. **Recipient Ind:Identifier** should be constructed using the 360Giving Publisher prefix starting 360G, an infix ‘IND’ followed by a unique number, separated by dashes, for example: **360G-ExampleFunder-IND-0001**

If there are data protection reasons why the unique identifiers cannot be taken from internal systems, they will need to be created instead. Read our [Individual Identifier guidance](../../technical/identifiers/#individual-identifier) for further information.
#### Funding Org:Name
The funding organisation’s name. This does not have to be the registered name, it can be the brand name the organisation prefers to be known by. 

**Please note:** For funders awarding grants on behalf of other funders, this would normally be the name of the funder distributing the grants. However, the organisation named as the funding organisation in 360Giving data could be the original ‘donor’ funder if this is agreed between the funders involved. Contact the 360Giving Helpdesk if you would like to discuss the options further.
#### Funding Org:Identifier
A unique identifier for the funding organisation, named in the Funding Org:Name field. The [Organisation Identifier Standard](../../technical/identifiers/#organisation-identifier) guidance explains how to create this org ID, based on the known company or charity number of the funder. 

The 360Giving Helpdesk can provide guidance on the correct Funding Org:Identifier to use.
### To Individuals Details fields
**Three new fields** have been added to the 360Giving Data Standard to support the publication of grants to individuals:
- **To Individuals Details:Primary Grant Reason**
- **To Individuals Details:Secondary Grant Reason**
- **To Individuals Details:Grant Purpose**

The fields are for use with **two codelists** that have been developed to support the publication of information about why the grant was awarded (**Grant to Individuals Reason**) and what the funding is to be spent on (**Grant to Individuals Purpose**). 

Funders are encouraged to use these codelists, alongside the text included in **Title** and **Description** fields, to provide information that will allow their data to be analysed and compared with other funders of grants to individuals.

The process of adopting the codelists may involve mapping the shared codelists against existing internal categorisations, or could require manual labelling of grants. Guidance on how to do this is provided in the Data Preparation Templates section below.

360Giving Helpdesk can provide additional guidance on using these codelists in your 360Giving data, and provide tailored support on how to map any internal categories or make decisions about manually labelling your grants.
#### Primary and Secondary Grant Reason
The codelist **Grant to Individuals Reason** includes categories that specify the reason that the grant was awarded to the individual recipient.
- The codes from this codelist must be published in either of two fields, **To Individuals Details:Primary Grant Reason** and **To Individuals Details:Secondary Grant Reason**. 
- Each field can only be included once with a single code per grant. If there is only a primary reason the secondary reason field can be left blank. 

See below for [Grant to Individuals Reason.](#Grants-To-Individuals-Reason)
#### Grant Purpose
The codelist **Grant to Individuals Purpose** includes categories to specify the purpose of the grant, in terms of what the funding will be used for.
- The codes from this codelist must be published in the field **To Individuals Details:Grant Purpose**.
- Funders may choose **one or more** of the categories to describe the purpose of the grant. When multiple codes are included, these must be separated by a **semi-colon**. 
- It is recommended that **a maximum of three categories** are used. 

See below for [Grant to Individuals Purpose.](#Grants-To-Individuals-Purpose)
### Recommended fields
Apart from the 10 core fields, all other fields in the 360Giving Data Standard are optional. However the majority of publishers do share a range of further information which make the data more useful and help users to understand their grantmaking better.

The following fields are **recommended**, which means you should consider including them in your data whenever possible.
#### Beneficiary location fields
The beneficiary location fields can be used to share useful information about the location of the individual grant recipients while protecting privacy. 

The location data is shared in the form of place names and geocodes, but address and postcode data is not allowed in these fields. This means the data can be analysed geographically and used in maps, but cannot be used to identify an individual recipient's specific location or home address.

For further guidance, please read our [guide to location in the 360Giving Data Standard.](../../guidance/location-guide/#about-geographic-codes)
- **Beneficiary Location:Name**
The fields used to share beneficiary location geocodes should be accompanied by fields for the location name whenever possible.
- **Beneficiary Location:Geographic Code**
A code referring to a geographical area, drawn from an established gazetteer such as the <a href="https://en.wikipedia.org/wiki/ONS_coding_system" target ="_blank">ONS Register of Geographic Codes</a> in the UK, at Ward or Local Authority level. 

It is recommended that location information is published at Ward area level, as this allows for a useful breakdown of grants by location, but does not allow for individuals to be identified. 

The Data Preparation templates have been set up to support the conversion of postcodes into Ward area level geocode. Further guidance on this step is [provided below.](../../individuals/data-preparation-templates/#converting-postcodes-into-geocodes)

Postcodes or ONS geocodes for small areas such as MSOA or LSOA **must not** be used for data protection reasons.
- **Beneficiary Location:Geographic Code Type**

The type of Geographic Code (geoCode) used (e.g. Ward, Parliamentary Constituency etc.). This value for this field should be drawn from the codelist of [geographic code types.](../../technical/codelists/#geocode-type)

The Data Preparation templates have been set up to automatically add the correct geocode type based on the location data provided.
#### Grant Programme:Title
Grant programmes information helps users to understand a funder’s different areas of focus and how their grants vary across these. 

There are also [additional grant programme field](../../technical/reference/spreadsheet-format/additional-fields/#grant-programme/) that can be used to share a description of the grant programme and link to further information.
#### Last Modified
This is metadata – data about the data – and shows users when information about the grant was last updated. **Last Modified** uses date-time format **YYYY-MM-DDThh:mm:ssZ**.
#### Data Source
This is metadata – data about the data – and shows users who published the grants data. This should be a link to the website of the organisation publishing the 360Giving data.
#### Grant duration fields
Funders with recurring or longer term grants can show this in their data by providing a start and end date of the grant, or the grant duration. Further information on [grant duration fields.](../../technical/reference/#planned-dates)
## Grants to individuals codelists
### What are codelists?
Codelists are a list of values. Each value has three elements:
 - a short name, which is designed for humans to read and understand
- a description, which explains to humans the meaning behind the code so that we can interpret it
- and the code, which is included in the data and allows machines to ‘read’ it

If you have ever used a web form and selected a value from a drop-down list, this is very similar to how codelists function.

The reason for using codes instead of names is because it avoids issues caused by typos, spaces or different cases. It also means the accompanying name and description can be amended or translated without the codes needing to be changed.
### The benefits of using shared codelists
In 360Giving data the **Title** and **Description** fields are usually the main ways that publishers can provide the ***detail of what has been funded*** and this is supported by additional information about the Recipient Organisation. But for data shared about grants to individuals, this text must be generic to avoid the information being used to identify individuals, and protect their privacy and confidentiality. This means the information that can be shared in these fields about grants to individuals will be less useful than that which can be shared by funders of grants for organisations and projects.

In order to mitigate against this issue, **two new codelists** have been developed in collaboration with members of ACO and refined through consultation with funders of grants to individuals.

When different funders use the same codelist in their data, it:
- Makes it easier to see the collective impact and analyse trends over time
- Allows individual funders to compare their grantmaking with peers
- Enables the development of dashboards and filters in tools to aid the visualisation of the data
### Using the shared codelists in 360Giving data
The codelists have been developed to be relevant to funders of grants to individuals, so the categories will be applicable to the broadest range of grants possible.

In order to be useful and usable, the lists have been kept relatively short, with categories at a high level. This means these codelists do not have the granular breakdown of categories that some funders may have in their own grants management systems. 

For some funders, particular programmes or all their grants may all fall under the same categories. Even at this high level, there is benefit to different funders using the shared codelists whenever possible.

As these codelists were specially developed for the 360Giving Data Standard, there are unlikely to be funders using these exact categories in their internal systems. This means that using the codelists in 360Giving data will involve some manual processing of data.
- For funders that have their own consistent internal categories, it will be possible to map these to the **Grant to Individuals Reason** or **Grant to Individuals Purpose** codelists.
- For funders who don’t have internal categories, the relevant code for each grant may have to be added manually.
<div class="box box--teal">
    <h3 class="box__heading">Deciding whether to categorise historical grants</h3>
    <p>There are internal benefits of using standardised codelists used by other funders to classify grants, which means the extra investment of time will be worthwhile. However if your organisation has limited capacity to code historical grants data, look instead at how to introduce the coding process into grants management processes, so they will be available to include in future publications.</p></div>
    
### Grant to Individuals Reason
A codelist with values to specify the reason that the grant was awarded to the recipient. This codelist is intended for use in grants to individual recipients only.

The codes from this codelist can be published in two fields, **To Individuals Details:Primary Grant Reason** and **To Individuals Details:Secondary Grant Reason**. Each field can only be included once with a single code per grant. 

If there is only one reason, it should be included in the primary reason field, and the secondary reason field and code can be left blank.

The codes, alongside their name and description, are as follows:
```eval_rst
.. csv-table::
   :file: ../../codelists/grantToIndividualsReason.csv
   :header-rows: 1
   :widths: auto
```
### Grant to Individuals Purpose
A codelist with values to specify the purpose of the grant, in terms of what the funding will be used for. This codelist is intended for use in grants to individual recipients only.

The codes from this codelist can be published in the field **To Individuals Details:Grant Purpose**.

The **To Individuals Details:Grant Purpose** field is an array. This means that when a publisher has more than one code to share per grant, these can be included in the same field, separated by a **semi-colon**. 

It is ***recommended that a maximum of three categories*** are shared to make it easier for the data to be analysed. The codes, alongside their name and description, are as follows:
```eval_rst
.. csv-table:: 
   :file: ../../codelists/grantToIndividualsPurpose.csv
   :header-rows: 1
   :widths: auto
```
#### Including internal categories alongside the shared classifications

For funders with their own categories for classifying their grants, this more granular data can be published in 360Giving data alongside, and in addition to, data from the **Reason** or **Purpose** codelists. Depending on the scope and complexity of the internal categories, these could be included in a range of ways:
- Using the 360Giving Data Standard [‘Classifications’](../../technical/reference/#classifications) fields.
- Values from a single value category list could be used to populate the **Title** field
- For classifications which allow for multiple categories, if they have hierarchies or when there are multiple different classifications, it may be easier to include this data in the form of a comma separated list in the **Description** field.

For further guidance about the best way to include internal categories in your 360Giving data, contact the 360Giving Helpdesk via <support@threesixtygiving.org>.

## Data protection
### Introduction
In general, open data should not contain personal or sensitive personal data that could allow a living person to be identified. Data to be published using the 360Giving Data Standard which does relate to identified individuals should be removed or anonymised to protect their privacy. All funders publishing 360Giving data need to consider data protection and privacy, and review their policies to ensure they can share the data about their grants responsibly. 

360Giving’s general guidance on [Data Protection](../../guidance/data-protection/) provides an overview of what to consider when sharing open grants data for the first time, focused on considerations for funders of grants to organisations.
### Data Protection for grants to individuals
For funders of grants to individuals, extra careful planning and clear processes are needed to ensure the data about these grants can be shared, while ensuring the privacy and confidentiality of the recipients.

The guidance below sets out the principles funders should follow, and the steps they should take to embed data protection into their 360Giving data publishing processes.
### Guiding principles to protect privacy
Responsibly publishing open data about grants received by individuals means that protecting their privacy and confidentiality is vital. 
The guidance and support has been designed to ensure that none of the following information will be published in data about grants to individuals:
- No **personal data** in the form of names or **other identifying information**.
- No **specific demographic data**, including no data collected using the **DEI Data Standard**.
- No **address** or **postcode** data.
### Anonymising data about grant recipients
A person’s name is a key piece of personal data which is expected to be anonymised in 360Giving data. 

It is recommended that **Recipient Ind:Name** field is populated with the generic text **Individual Recipient** to ensure the privacy of the person receiving the funding.

However even with the name removed, there are other ways that a recipient could be identified which need to be considered, so that appropriate processes are put in place to prevent this information from being published. These include:
- Identifiers taken from internal systems
- Description text
- Location
- Demographic data
#### Identifiers taken from internal systems
Two of the 10 core fields are unique identifiers for each grant and each recipient – **Identifier** and **Recipient Ind:Identifier**. 

Normally the grant **Identifier** is taken from a funder’s grants management system or database, so that the reference in their internal systems matches that used in the 360Giving data.

As these internal system references are specific to each recipient, they could be used to identify that person. When these identifiers are securely held and are only accessible to people who are authorised to access the grant recipient’s personal data, then it can be appropriate to publish these in 360Giving data. However, if the system identifiers are shared with third parties alongside recipient names or other personal details as part of the grantmaking process – for example with referral agencies, or as part of monitoring and reporting – then these could be used to identify people in your 360Giving data. 

**Recipient Ind:Identifier** may also be created using a system reference, and so should be treated with the same caution as grant Identifiers.

**Please note**: If there is a data sharing agreement in place with the third party which means it is acting as a data processor on behalf of the funder, then the identifiers may be published. Otherwise an alternative source of identifiers should be used.
#### Title and Description text
Searching **Title** and **Description** text is one of the main ways that users identify what is being funded when exploring data using <a href="https://grantnav.threesixtygiving.org/" target = "_blank">GrantNav</a>. This means that the **Title** and **Description** fields provide an opportunity to provide more information about each grant, which will let users know why you made the award and what it is for. 

Using clear and unambiguous language will help users to understand the purpose and reason for the grant, and the type of activities, communities or places being supported by the funding.

However, the text published about grants to individuals must be kept generic to avoid including any information that could be used to identify the recipient. 

**For example**

**A grant to pay for vocational training**
- **Do:** Mention the area of learning or skill, and why the person is taking the course. 
- **Don’t:** Name of the course or specific learning provider.

**A grant to buy household items for an older person who is an armed forces veteran experiencing financial hardship**
- **Do:** Mention the type of items to be purchased and that the recipient is an older person who is a veteran.
- **Don’t:** Name specific brands or models of items. Don’t include specific demographic information about the individual together, such as exact age, ethnicity and gender.

If no suitable grant description text is available because the information you hold is too specific to each individual, text describing the overall grant programme could be used instead.

For funders with internal categories for grants, these can also be included in the description to provide further details, as a comma separated list.
#### Location information
For grants to individuals, address information or postal codes **must not** be published, as these could lead to the recipient being identified.

It is recommended that instead, postcodes are converted into <a href="https://en.wikipedia.org/wiki/ONS_coding_system" target ="_blank">Office for National Statistics</a> (ONS) area names and geocodes at Ward or higher levels of geography. 

This allows useful data to be published, which will work with the location filtering functions of  <a href ="https://grantnav.threesixtygiving.org/" target ="_blank">GrantNav</a>, while protecting the privacy of individuals.

Guidance about how to convert postcodes to geocodes is included in the [Data Preparation templates section.](../../individuals/data-preparation-templates/#converting-postcodes-into-geocodes)

#### Demographic data

Specific demographic data which describe the recipient's protected characteristics should not be included in published data, as this information – combined with other details from the grant – could potentially be used to identify the individual.

This is true whether the demographic data is collected through bespoke internal systems or using the <a href="https://www.funderscollaborativehub.org.uk/collaborations/dei-data-standard" target ="_blank">DEI Data Standard</a>.

Demographic data about recipients is useful data, but it should only be published about individuals at aggregated levels, to ensure privacy and confidentiality. If you do choose to publish aggregate data about the demographics of your grantees, you may wish to publish this on your website alongside your 360Giving data, but in a separate file or section.

Demographic data about the recipient may also be linked to the reason for the grant, when a funder or grant programme has criteria which restricts funding to, for example, older or younger people, or is only available to women or people with specific disabilities or illnesses. In these cases, this demographic information can be included as part of the grant programme or description fields, when expressed in general terms.

### Data protection checklist
This checklist is designed to help audit the data held in internal systems that could be used to identify recipients. It will help to identify what information:
- Should not be published
- Can be published with changes to anonymise the information
- Can be published without any changes

#### System identifiers
<div class="table table--zebra">
    <table>
        <thead>
            <th>Do you share the following system IDs with third parties*?</th>
            <th>No</th>
            <th>Yes</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Do you share the following system IDs with third parties*?">Unique application/grant identifiers from your internal systems.</td>
                <td data-header="No">You can include these system identifiers in your published 360Giving data.</td>
                <td data-header="Yes">Create new grant identifiers before publishing this data.</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Do you share the following system IDs with third parties*?">Unique recipient identifiers from your internal systems.</td>
                <td data-header="No">You can include these system identifiers in your published 360Giving data.</td>
                <td data-header="Yes">Create new recipient identifiers before publishing this data.</td>
                  </td>
            </tr>
        </tbody>
    </table>
</div>

#### Descriptive text
<div class="table table--zebra">
    <table>
        <thead>
            <th>Do you grant Descriptions or Titles include the following?</th>
            <th>No</th>
            <th>Yes</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Do you grant Descriptions or Titles include the following?">The name of the recipient.</td>
                <td data-header="No">You can include this Title or Description text in your published data.</td>
                <td data-header="Yes">Amend your Title or Description text to remove identifying data, or use alternative text, such as grant programme description or category data.</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Do you grant Descriptions or Titles include the following?">A detailed breakdown of what the funding was for.</td>
                <td data-header="No">You can include this Title or Description text in your published data.</td>
                <td data-header="Yes">Amend your Title or Description text to remove identifying data, or use alternative text, such as grant programme description or category data.</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Do you grant Descriptions or Titles include the following?">Specific demographic information about the recipient.</td>
                <td data-header="No">You can include this Title or Description text in your published data.</td>
                <td data-header="Yes">Amend your Title or Description text to remove identifying data, or use alternative text, such as grant programme description or category data.</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Do you grant Descriptions or Titles include the following?">References to a referral agency making the application on the recipients behalf.</td>
                <td data-header="No">You can include this Title or Description text in your published data.</td>
                <td data-header="Yes">Amend your Title or Description text to remove identifying data, or use alternative text, such as grant programme description or category data.</td>
                  </td>
            </tr>
        </tbody>
    </table>
</div>

#### Geodata
<div class="table table--zebra">
    <table>
        <thead>
            <th>Does your grant information include the following geodata?</th>
            <th>No</th>
            <th>Yes</th>
        </thead>
        <tbody>
            <tr>
                <td class="table__lead-cell" data-header="Does your grant information include the following geodata?">Address details for the recipient’s home address.</td>
                <td data-header="No">No action.</td>
                <td data-header="Yes">Remove from data before publishing.</td>
                </td>
            </tr>
            <tr>
                <td class="table__lead-cell" data-header="Does your grant information include the following geodata?">Postcodes for the recipients home address.</td>
                <td data-header="No">No action.</td>
                <td data-header="Yes">Convert postcode data into Ward or higher level area codes before publishing the data.</td>
                  </td>
            </tr>
        </tbody>
    </table>
</div>


\* If the third parties with access to the data are covered by data sharing agreements, you can answer No.

### 360Giving Take Down Policy
A fundamental aspect of publishing using the 360Giving Data Standard, and publishing open data in general, is that once the information is released it may be downloaded and used by anyone.

A publishing organisation can decide to stop publishing data and/or can remove the data from their website at any time, however the information that has been published may still be held and used by anyone who has already downloaded it.

For publishers intending to publish grants to individuals the goal is to ensure that no information is shared in 360Giving data that could allow an individual to be identified. However, in the event that data is published that needs to be removed to prevent or limit a breach of privacy, 360Giving will follow our <a href ="https://www.threesixtygiving.org/take-down-policy/" target ="_blank">Take down policy</a> for the data linked from our <a href="https://data.threesixtygiving.org/" target="_blank">Data Registry</a> and loaded into our tools, so we will remove any published data on request.

## Prepare and format your data
### Introduction
For all funders, the practical steps to prepare your data will be influenced by how you collect and store information about your grants.

For many publishers, preparing their data is a manual process that involves exporting information from a grants management system and converting it in a spreadsheet file. However, some grants management systems make it possible to build in some or all of the steps needed to convert the information, so it can be exported directly from the system in 360Giving data format, for example in specially configured CRM systems, such as Salesforce or Microsoft Dynamics.

For most publishers, whether you are using grants management software or you hold your grants data in spreadsheets, the practical steps to get your data ready will be similar and involve making changes to the data in a file. 

Read the [general guidance about preparing 360Giving data](../../guidance/#prepare-and-format-your-data) for further information about your options.
### Register with 360Giving Helpdesk
Once you have decided to publish your grants data, please fill in our <a href="https://www.threesixtygiving.org/publisher-registration-form/" target ="_blank">Publisher Registration Form</a> to let us know more about your organisation, so 360Giving Helpdesk can provide tailored support to suit your needs.

You will be provided with a 360Giving Publisher prefix, which identifies your organisation and will be used in your 360Giving data to provide a unique identifier for each grant. For further information see our guidance about [grant identifiers.](../../technical/identifiers/#id2)

### Spreadsheet templates
Two types of template have been provided for funders with the 360Giving Data Standard fields needed to prepare and publish useful information about grants to individuals. The templates include the 10 core fields, some recommended fields and the three new fields that are used with the codelists. 

Use the Field guidance and Data Preparation templates guidance for further information about what types of data are suitable for sharing under each field.
- [10 core fields](../../individuals/publisher-guidance/#core-fields)
- [Recommended fields](../../individuals/publisher-guidance/#recommended-fields)
- [To Individuals Details fields](../../individuals/publisher-guidance/#to-individuals-details-fields)

The Data Preparation templates have been set up with data protection settings, to consistently anonymise recipient names, to create grant and recipients identifiers if internal systems IDs are not suitable for sharing and to support the conversion of postcodes into geocodes. 
<div class="box box--teal">
    <h3 class="box__heading">Give grants to organisations and individuals?</h3>
    <p>These templates are suitable for sharing data about grants to individuals only. If you give grants to both individuals and organisations you will need to use separate templates in separate files to publish these different types of grant.</p>
<p>Further information about the options for sharing data about grants to organisations can be found in the <a href="https://standard.threesixtygiving.org/en/latest/guidance/prepare-data/" target="_blank">general guidance on preparing data</a>. Please contact 360Giving Helpdesk for further guidance via <a href="mailto:support@threesixtygiving.org">support@threesixtygiving.org.</a></p></div>


#### 360Giving Grants to Inds Data Preparation Templates
These templates have been set up to make the practical steps of formatting grant information into 360Giving data more straightforward.

The templates can be used to convert data exported from a grants management system or copied from an existing file of grant data. It can also be used to collect data, by manually entering the information directly into the template. 
Each template can be tailored to each funder’s data and needs, however they are all set up in the same way with a range of sheets – including sheets for the source information from your systems or files, a sheet for information about your organisation required for creating 360Giving data, and a final sheet which formats the information you have provided into 360Giving data using formulas. 

There are two versions of the template. 

**360Giving-Grants-to-Inds-Data-Preparation-Template_Codelist-Mapping** is designed for use by funders who have internal categories for their grants which can be mapped against the shared 360Giving codelists.

Download a copy of the **<a href= "https://docs.google.com/spreadsheets/d/1ucTCgxS8V2Eg-fhbeHZBKgr4fg7HKRQs/" target ="_blank">Codelist-Mapping template</a>**

**360Giving-Grants-to-Inds-Data-Preparation-Template_Manual-Coding** is designed for use by funders who don’t have existing categories for their grants, and so need to manually code their grants using the shared 360Giving codelists.

Download a copy of the **<a href = "https://docs.google.com/spreadsheets/d/1ekc0nvjsgioZ6MvIcaI2Ecv5XBf7APMo/" target = "_blank">Manual-Coding template</a>**

Full guidance about the templates and how they work is provided in the [Data Preparation Templates section.](../../individuals/data-preparation-templates)

<div class="box box--teal">
    <h3 class="box__heading">Filling out the templates</h3>
    <p>The 10 core fields must be filled in so that there is no missing information.</p>
  <p>For all other columns, if information is not available the field should be left blank. Do not use dashes (-) zeros (0) or N/A to fill in blank fields as this will make your data harder to use.</p></div>
