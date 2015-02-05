---
layout: post
title: Components
description: "Base components for building your website"
tags: ["ASU Web Standards Bootstrap"]
image:
  feature: components.jpg
  credit: Vadim Sherbakov
  creditlink: https://unsplash.imgix.net/4/madebyvadim.jpg?q=75&fm=jpg&s=fe3525c767180ee0355028065cba9e01
---

In addition to all of the components that [Bootstrap](http://getbootstrap.com/) offers, the ASU Web Standards Bootstrap repo adds a few new components that you can use in your project.

<!--break-->

### Navigation

The navigation provided in the ASU Web Standards is an extension of the navigation menu provided by Bootstrap.  Here is an example of how to put together the HTML for a nav bar:

```html
<div id="site-name-desktop" class="section site-name-desktop">
  <div class="container">
    <h1 class="site-title" id="asu_school_name"><span class="first-word"><a href="{{organization_url}}">{{organization_name}}</a></span>&nbsp;|&nbsp; <a href=
    "{{school_url}}">{{school_name}}</a></h1>
  </div>
</div>
<nav class="navbar navbar-ws" role="navigation">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=
      "#ws-navbar-collapse-1"><span class="sr-only">Toggle navigation</span></button>
      <a class="navbar-brand" href="{{school_url}}">{{school_name}}</a>
    </div>
    <div id="ws-navbar-collapse-1" class="collapse navbar-collapse">
      <ul id="menu-header-menu" class="nav navbar-nav">
        {{navigation_dropdowns}}
      </ul>
    </div>
  </div>
</nav>
```

The navigation dropdowns can by any combination of the following types:

#### Single Tab

TODO

#### Simple Menu

TODO

#### Mega Menu

TODO

<!--break-->

### Lead Paragraphs

You can add what is known as a `lead paragraph` to your content.  Lead paragraphs pop out and are slightly larger in font than normal paragraphs.

They normally follow headings and are one sentence long.

<p class="lead">This is an example lead sentence</p>

```html
<p class="lead">This is an example lead sentence</p>
```

<!--break-->

### Calendar Dates

Calendar dates are widgets that you can add to your application in order to allow users to visually see a date and download it to add the date to a calendar app of their choice.

<div class="calendar-date calendarPopover" data-original-title="" title="">
  <time datetime="2014-01-01">
    <span class="weekday">Sun</span>
    <span class="date">1</span>
    <span class="month">Jan</span>
  </time>
</div>

```html
<div class="calendar-date calendarPopover" data-original-title="" title="">
  <time datetime="2014-01-01">
    <span class="weekday">Sun</span>
    <span class="date">1</span>
    <span class="month">Jan</span>
  </time>
</div>
```

<!--break-->

### Profile

TODO

<!--break-->

### Visit Campus

TODO


