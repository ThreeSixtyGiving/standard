# Example page from David: Plan


<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste  </td>
    <td>Maria Anders  </td>
    <td>Germany  </td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>



```eval_rst
.. admonition:: For example

  If Indigo Trust have a grant called 'Grant27', and Nominet Trust also have a grant called 'Grant27' the two will get confused when combining the two datasets. But if, when publishing, each one adds a prefix, then we end up with two unique identifiers: '360G-indigotrust-Grant27' and '360G-Nominet-Grant27'
```

<details>
  <summary>Why identifiers matter [EXAMPLE REMOVE]</summary>

  Identifiers are an important part of any dataset. They let a computer uniquely identify and refer to specific grants, organisations, transactions and so-on.

  Whilst a human being may be good at recognising that "Big Lottery Fund", "BLF", and "big-lottery-fund" all refer to the same organisation, computers cannot make this connection unless a unique identifier is provided.

</details>


First Header | Second Header | Extra column
------------ | ------------- | -------
Content from cell 1 | Content from cell 2 | more data
Content in the first column | Content in the second column | more data

```eval_rst

.. admonition:: Why identifiers matter

  Identifiers are an important part of any dataset. They let a computer uniquely identify and refer to specific grants, organisations, transactions and so-on.

  Whilst a human being may be good at recognising that "Big Lottery Fund", "BLF", and "big-lottery-fund" all refer to the same organisation, computers cannot make this connection unless a unique identifier is provided.

```

```eval_rst
.. admonition:: For example

  If Indigo Trust have a grant called 'Grant27', and Nominet Trust also have a grant called 'Grant27' the two will get confused when combining the two datasets. But if, when publishing, each one adds a prefix, then we end up with two unique identifiers: '360G-indigotrust-Grant27' and '360G-Nominet-Grant27'
```

```eval_rst

.. admonition:: For example

  A charity registered in England and Wales with the Charity Commission of England and Wales, with the charity number '1070468' will use a list code prefix of ``GB-CHC``.

  This gives an unique organisation identifier of ``GB-CHC-1070468``

```

````eval_rst
.. hint::

  UK company numbers are a unique combination of eight digits, which in some cases include letters as well as numbers. The majority of company numbers for companies registered in England and Wales start with a **leading zero**.

  Publishers should be aware of the problems that missing leading zeros in UK company numbers present when creating identifiers. `Learn more`__ about how to avoid this pitfall.
.. __: https://www.threesixtygiving.org/support/company-numbers/

````


## Who is this guide for?

This guide is for anyone from a UK funding organisation who wants to publish their grants data openly in the 360Giving Data Standard. 

This guide will help organisations publish data for the first time. It will also be useful to:
- People taking over responsibility for preparing and sharing 360Giving data for their organisation from a colleague.
- Anyone who wants to know more about what sharing 360Giving data involves.

It is designed to help you at any stage of the publishing process – whether you are at the very beginning of your journey and planning your approach, preparing your data, at the publishing stage, or looking for ways to promote the fact you have published.

We want to help you achieve your goal of sharing open and comparable grants data using the 360Giving Data Standard. This isn’t a reporting process, it’s an opportunity to communicate about your grantmaking using data.

Our pro-bono support helps funders navigate the steps to share their grants data using the 360Giving Data Standard. We provide guidance and direct support to help streamline the process as far as possible.

At any point in this process please feel free to contact our free Helpdesk via <support@threesixtygiving.org> with any queries (large or small).

## What’s in the guide?

The guidance sets out the fourthree key stages in the 360Giving publishing process, and highlights the options available and factors that will inform the choices you make:

- Plan
- Prepare
- Publish
- Promote

These stages apply to all types of funder. However the approach you take, the support you need, and how long the process will take, can all vary, depending on a range of factors:

- The information you collect about your grantmaking.
- The systems you use to manage the data.
- How much data you want to share.
- Your organisational and technical capacity.

## The stages in brief

### Planning 

You will identify the scope of the grants information you want to share and check for any issues with missing information. This is also the time to consider the potential privacy and responsible data implications of sharing your grants data.

### Preparing

Once you have identified the grants information you intend to publish, your data needs to be transformed into 360Giving Data Standard data, using the correct formats and headings. You will check your data using the 360Giving Data Quality Tool.

For many publishers preparing their data is a manual process involving converting data exported into a spreadsheet from a grants management system. However some grants management systems make it possible to export data with some or all of the preparations needed to convert the information into 360Giving data built-in.

### Publishing 

Your prepared file of 360Giving data needs to be made available online with clear permissions to allow for its use. This usually involves uploading the file to your website and linking to the file with text referring to the open license. The final step is to let 360Giving know that your data is live!

### Promoting

...

## Before you start

### What are the benefits of publishing 360Giving grants data?

Publishing grants data using the 360Giving Data Standard [brings lots of benefits](https://www.threesixtygiving.org/support/why-publish-grants-data/ ), both for the funders who publish their grants data and for society.

### How do we register to become a 360Giving data publisher?

Once you have decided to publish your grants data please let us know by contacting 360Giving Helpdesk by emailing support@threesixtygiving.org. 

You will be provided with a 360Giving Publisher prefix, which identifies your organisation and will be used in your 360Giving data to provide a unique identifier for each grant (see our guidance about Identifiers for further details).

### Do we have to pay?

360Giving support for publishers is provided free of charge. There are no registration fees or costs associated with publishing 360Giving data.

Preparing 360Giving data does require a commitment of resources from the publisher in terms of staff time, especially when releasing your data for the first time. There can be costs in terms of consultancy or support fees for getting grants management systems set up to export 360Giving data. 

## How long the process takes

The amount of time it takes to prepare and share 360Giving data can vary depending on your circumstances. The amount of data to be published, and whether the data is well-organised and consistent are key factors in determining whether the process will be more or less time consuming. 

It will be possible to estimate the work involved once you have decided on the scope of your data, as set out in the Plan section below.

## About grants management systems

Grantmakers of all shapes and sizes, using a wide range of grants management systems as well as those collecting basic data in spreadsheets, have become 360Giving data publishers. 

Where and how you collect and store information about your grants has a fundamental impact on the data you will be able to share, and this will also influence the practical process taken to format your data to the 360Giving Data Standard. 

What grants management systems you use will be one of the first questions we’ll ask you when you start on your 360Giving publishing journey. Whatever the answer, there will be useful learning we can share from our work supporting over 150 other publishers.

See Section 2 on preparing your data for further details about the likely impact your grants management system will have on the publishing process.

## Publishing resources for community foundations

If you are a community foundation using the Digits2 grants management system please refer to [our special guidance](https://www.threesixtygiving.org/communityfoundations/cf-publishing-guide/) about the built-in 360Giving data extract to publishing 360Giving data.

# Examples

### Media card

<article class="media-card media-card--red">
    <div class="media-card__content">
        <header class="media-card__header">
            <h3 class="media-card__heading">Rachel Rank</h3>
            <span class="media-card__subtitle">Chief Operating Officer</span>
        </header>
        <p>Lorem ipsum dolor sit amet, <a href="#">consectetur adipisicing elit</a>. Harum quod vel voluptas recusandae dignissimos fugit deserunt molestiae, quae, blanditiis autem nesciunt odio consectetur error facilis. Ipsum, maiores cumque quo atque. Lorem ipsum Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae magni. </p>
    </div>

    <div class="media-card__image-wrapper">
        <div class="media-card__image" style="background-image: url(https://www.threesixtygiving.org/wp-content/uploads/47319360032_51d21156a2_c.jpg)"></div>
    </div>
</article>

### Alert tag

<div class="alert-tag">
    <span class="alert-tag__icon"><svg width="16" height="16" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M7 5.83333C6.70833 5.83333 6.41667 6.06667 6.41667 6.41667V9.91667C6.41667 10.2667 6.65 10.5 7 10.5C7.29167 10.5 7.58333 10.2667 7.58333 9.91667V6.41667C7.58333 6.125 7.29167 5.83333 7 5.83333ZM7 3.5C6.70833 3.5 6.41667 3.73333 6.41667 4.08333C6.41667 4.375 6.65 4.66667 7 4.66667C7.29167 4.66667 7.58333 4.43333 7.58333 4.08333C7.58333 3.79167 7.29167 3.5 7 3.5ZM7 0C3.15 0 0 3.15 0 7C0 10.85 3.15 14 7 14C10.85 14 14 10.85 14 7C14 3.15 10.85 0 7 0ZM7 12.8333C3.79167 12.8333 1.16667 10.2083 1.16667 7C1.16667 3.79167 3.79167 1.16667 7 1.16667C10.2083 1.16667 12.8333 3.79167 12.8333 7C12.8333 10.2083 10.2083 12.8333 7 12.8333Z" fill="#1D1536" />
        </svg>
    </span>
    <span class="alert-tag__content"><a href="#">Our guide to targeting your search</a></span>
</div>

<a class="alert-tag alert-tag--anchor" href="#">
    <span class="alert-tag__icon"><svg width="16" height="16" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M7 5.83333C6.70833 5.83333 6.41667 6.06667 6.41667 6.41667V9.91667C6.41667 10.2667 6.65 10.5 7 10.5C7.29167 10.5 7.58333 10.2667 7.58333 9.91667V6.41667C7.58333 6.125 7.29167 5.83333 7 5.83333ZM7 3.5C6.70833 3.5 6.41667 3.73333 6.41667 4.08333C6.41667 4.375 6.65 4.66667 7 4.66667C7.29167 4.66667 7.58333 4.43333 7.58333 4.08333C7.58333 3.79167 7.29167 3.5 7 3.5ZM7 0C3.15 0 0 3.15 0 7C0 10.85 3.15 14 7 14C10.85 14 14 10.85 14 7C14 3.15 10.85 0 7 0ZM7 12.8333C3.79167 12.8333 1.16667 10.2083 1.16667 7C1.16667 3.79167 3.79167 1.16667 7 1.16667C10.2083 1.16667 12.8333 3.79167 12.8333 7C12.8333 10.2083 10.2083 12.8333 7 12.8333Z" fill="#1D1536" />
        </svg>
    </span>
    <span class="alert-tag__content">Learn more about this</span>
</a>

### Buttons

<p>
    <a href="#" class="button">Button</a>
    <button class="button button--orange">Button Orange</button>
    <button class="button button--teal">Button teal</button>
    <button class="button button--yellow">Button yellow</button>
    <button class="button button--red">Button red</button>
    <button class="button button--black">Button black</button>
    <button class="button button--disabled">Button disabled</button>
</p>

<p>
    <a href="#" class="button button--large">Button</a>
    <button class="button button--large button--orange">Button Orange</button>
    <button class="button button--large button--teal">Button teal</button>
    <button class="button button--large button--yellow">Button yellow</button>
    <button class="button button--large button--red">Button red</button>
    <button class="button button--large button--black">Button black</button>
    <button class="button button--large button--disabled">Button disabled</button>
</p>

<p>
    <a href="#" class="button button--small">Button</a>
    <button class="button button--small button--orange">Button Orange</button>
    <button class="button button--small button--teal">Button teal</button>
    <button class="button button--small button--yellow">Button yellow</button>
    <button class="button button--small button--red">Button red</button>
    <button class="button button--small button--black">Button black</button>
    <button class="button button--small button--disabled">Button disabled</button>
</p>

### Default box (dark colour

<div class="box">
    <h3 class="box__heading">Developers</h3>
    <p>For a JSON feed of published datasets visit <a href="http://standard.threesixtygiving.org/en/latest/getdata/" target="_blank">standard.threesixtygiving.org</a></p>
</div>

### Prose image box

    <figure>
        <img src="https://www.threesixtygiving.org/wp-content/uploads/47319360032_51d21156a2_c.jpg" alt="">
        <figcaption>Lorem ipsum, dolor, sit amet consectetur adipisicing elit. <em>Fuga deleniti architecto nisi</em>, rerum aliquid aperiam minima <strong>saepe magnam eum. Odit aliquid similique magnam minima</strong>, corrupti, aliquam laudantium eos asperiores possimus?</figcaption>
    </figure>
    
    <html>
<body>

<h1>The figure and figcaption element</h1>

<figure>
  <img src="pic_trulli.jpg" alt="Trulli" style="width:100%">
  <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
</figure>

</body>
</html>


</div>

### Table

<div class="table table--zebra">
    <table>

        <thead>
            <th>Title</th>
            <th>Description</th>
            <th>Type</th>
            <th>Required</th>
        </thead>

        <tbody>

            <tr>
                <td class="table__lead-cell" data-header="Title">Identifier</td>
                <td data-header="Description">The unique identifier for this grant. Made up of your 360Giving prefix, and an identifier from your records. See the 360Giving Grant identifier guidance for details.</td>
                <td data-header="Type"><code>string</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--true">check</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Title</td>
                <td data-header="Description">A title for this grant activity. This should be under 140 characters long.</td>
                <td data-header="Type"><code>string</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--true">check</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Description</td>
                <td data-header="Description">A short description of this grant activity.</td>
                <td data-header="Type"><code>string</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--true">check</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Currency</td>
                <td data-header="Description">The currency used in amounts. Use the three-letter <a href='#'>currency code from ISO 4217</a> eg: Use GBP for Pounds Sterling.</td>
                <td data-header="Type"><code>string</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--true">check</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Amount Applied For</td>
                <td data-header="Description">Total amount applied for in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the application transactions for this grant.</td>
                <td data-header="Type"><code>number</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--false">close</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Amount Awarded</td>
                <td data-header="Description">Total amount awarded in numbers (do not include commas or currency symbols such as £). If you have provided detailed transaction information on a separate table, this should equal the sum of all the award transactions for this grant.</td>
                <td data-header="Type"><code>number</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--true">check</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Amount Disbursed</td>
                <td data-header="Description">Total amount disbursed (paid) to this grantee when this record was last updated (in numbers: do not include commas or currency symbols such as £)). If you have provided detailed transaction information on a separate table, this should equal the sum of all the disbursement transactions for this grant.</td>
                <td data-header="Type"><code>number</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--false">close</i>

                </td>
            </tr>

            <tr>
                <td class="table__lead-cell" data-header="Title">Award Date</td>
                <td data-header="Description">When was the decision to award this grant made. The date should be written as YYYY-MM-DD, or in full date-time format.</td>
                <td data-header="Type"><code>string</code></td>
                <td data-header="Required" class="table__checks">

                    <i class="material-icons table--true">check</i>

                </td>
            </tr>

        </tbody>
    </table>
</div>
