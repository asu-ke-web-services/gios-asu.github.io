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

## Navigation

The navigation provided in the ASU Web Standards is an extension of the navigation menu provided by Bootstrap.  Here is an example of how to put together the HTML for a nav bar:

```html
<div id="site-name-desktop" class="section site-name-desktop">
  <div class="container">
    <h1 class="site-title" id="asu_school_name"><span class="first-word"><a href="__organization_url__">__organization_name__</a></span>&nbsp;|&nbsp; <a href=
    "__school_url__">__school_name__</a></h1>
  </div>
</div>
<nav class="navbar navbar-ws" role="navigation">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=
      "#ws-navbar-collapse-1"><span class="sr-only">Toggle navigation</span></button>
      <a class="navbar-brand" href="__school_url__">__school_name__</a>
    </div>
    <div id="ws-navbar-collapse-1" class="collapse navbar-collapse">
      <ul id="menu-header-menu" class="nav navbar-nav">
        __navigation_dropdowns__
      </ul>
    </div>
  </div>
</nav>
```

The navigation dropdowns can by any combination of the following types:

### Home Tab

The home tab is the first menu navigation item on the menu.

```html
<li>
  <a href="./" title="Home">
    <span class="fa fa-home hidden-xs hidden-sm" aria-hidden="true"></span><span class="hidden-md hidden-lg">Home</span>
  </a>
</li>
```


### Single Tab

A single tab on the menu navigation is created with the following markup:

```html
<li>
  <a title="__navigation_item_name__" href="__href__">__navigation_item_name__</a>
</li>
```

### Simple Menu

A simple menu is a dropdown menu in the navigation and is created with the following markup:

```html
<li class="dropdown">
  <a title="__navigation_item_name__" href="#" data-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">
    __navigation_item_name__ <span class="caret"></span>
  </a>
  <ul role="menu" class="dropdown-menu">
    <li>
      <a title="__item_name__" href="__href__">__item_name__</a>
    </li>
    <li>
      <a title="__item_name__" href="__href__">__item_name__</a>
    </li>
    <!-- ... -->
  </ul>
</li>
```

### Mega Menu

Mega menus are used to display many dropdown sections of related links.

The sections use bootstrap's containers to fluidly display menu items.  This example is 2 columns and uses `col-md-6`. 

```html
<li class="mega-menu dropdown">
  <a title="__navigation_item_name__" href="#" data-toggle="dropdown" class="dropdown-toggle" aria-haspopup="true">
    __navigation_item_name__ <span class="caret"></span>
  </a>
  <ul role="menu" class="dropdown-menu">
    <li class="li-row-container">
      <div class="row">
        <div class="column col-md-6 vertical-border-right">
          <ul>
            <li class="dropdown-title">Column 1</li>
            <li><a title="__item_name__" href="__href__">__item_name__</a>
            </li>
            <li><a title="__item_name__" href="__href__">__item_name__</a>
            </li>
            <li><a title="__item_name__" href="__href__">__item_name__</a>
            </li>
          </ul>
        </div>
        <div class="column col-md-6">
          <ul>
            <li class="dropdown-title">Column 2</li>
            <li><a title="__item_name__" href="__href__">__item_name__</a>
            </li>
            <li><a title="__item_name__" href="__href__">__item_name__</a>
            </li>
          </ul>
        </div>
      </div>
    </li>
  </ul>
</li>
```

<!--break-->

## Mega Footer

The Mega Footer is the section before the legal footer, but after the content of the page.  It can contains the school logo, contact information, social media links, page links, and more:

```html
<div class="big-foot">
  <div class="container">
    <div class="row">
      <div class="col-md-4 col-sm-12 space-bot-md">
        <img class="footer-logo" src="https://sos.wp.prod.gios.asu.edu/files/2015/01/SOS_REV.png">
        <br>            
        <address>
          Arizona State University<br>
          800 South Cady Mall <br>
          Tempe, AZ 85281<br>
          Phone: <a class="phone-link" href="tel:(480) 727-6963">(480) 727-6963</a><br>
          Fax: (480) 965-8087<br>
        </address>    
      </div>
      <div class="col-md-6 space-bot-md">
        <h2 data-toggle="collapse" data-target="#menu-item-596-nav">Categories  <span class="caret hidden-sm hidden-md hidden-lg"></span></h2>
        <ul class="big-foot-nav collapse in">
          <li class="menu-item">
            <a title="__item_name__" href="__href__">__item_name__</a>
          </li>
        </ul>
      </div>
    </div><!-- /.row -->
  </div><!-- /.container -->
</div>
```

<!--break-->

## Heros

Hero units are made to callout specific content.

<div class="bs-example">
  <div class="hero hero-bg-img hero-action-call" style="background-image: url({{ site.url }}/images/{{ page.image.feature }});">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <h2>A top university designed for you</h2>
          <p>Become a master learner—one who is able to thrive in tomorrow's dynamic work environment—at one of the world's most innovative universities today.</p>
          <button class="btn btn-primary" type="button">See more rankings</button>
        </div>
      </div><!-- /.row -->
    </div><!-- /.container -->
  </div>
</div>

```html
<div class="hero hero-bg-img hero-action-call" style="background-image: url(__image_url__);">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12">
        <h2>A top university designed for you</h2>
        <p>Become a master learner—one who is able to thrive in tomorrow's dynamic work environment—at one of the world's most innovative universities today.</p>
        <button class="btn btn-primary" type="button">See more rankings</button>
      </div>
    </div><!-- /.row -->
  </div><!-- /.container -->
</div>
```

<!--break-->

## Lead Paragraphs

You can add what is known as a `lead paragraph` to your content.  Lead paragraphs pop out and are slightly larger in font than normal paragraphs.

They normally follow headings and are one sentence long.

<div class="bs-example">
  <p class="lead">This is an example lead sentence</p>
</div>

```html
<p class="lead">This is an example lead sentence</p>
```

<!--break-->

## Calendar Dates

Calendar dates are widgets that you can add to your application in order to allow users to visually see a date and download it to add the date to a calendar app of their choice.

<div class="bs-example">
  <div class="calendar-date calendarPopover" data-original-title="" title="">
    <time datetime="2014-01-01">
      <span class="weekday">Sun</span>
      <span class="date">1</span>
      <span class="month">Jan</span>
    </time>
  </div>
  <div class="clearfix"></div>
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

## Profile

<div class="bs-example">
  <!-- Example profile -->
  <div class="profile">
    <div class="profile-heading">
      <div class="row">
        <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
          <div class="profile-pic">
            <img src="http://placehold.it/266x266" alt="Jason Striker" class="img-responsive space-bot-md">
          </div>
        </div>
        <div class="col-xs-12 col-sm-5 col-md-5 col-lg-6">
          <p>
            <strong>Jason Striker</strong><br>
            Manager Communications (UTO)<br>
            UTO Planning and Programs<br>
            University Staff
          </p>
          <p>
            <a href="#">Jason.Striker@asu.edu</a><br>
            <a href="#">(480) 727-5426</a><br>
            Mail Code: 0101
          </p>
          <p>
            Student Information<br>
            Graduate Student<br>
            Communication Studies<br>
            New Interdis Arts &amp; Sciences
          </p>
        </div>
        <div class="col-xs-12 col-sm-3 col-md-3 col-lg-2">
          <ul class="profile-actions">
            <li><a href="#">Print Profile</a></li>
            <li><a href="#">Update Profile</a></li>
            <li><a href="#">Report Abuse</a></li>
          </ul>
        </div>
      </div><!-- /.row -->
    </div>
    <ul class="nav nav-tabs">
      <li class="active"><a href="#bio" data-toggle="tab">Bio</a></li>
      <li><a href="#research" data-toggle="tab">Research Interests</a></li>
      <li><a href="#vitae" data-toggle="tab">Curriculum Vitae</a></li>
    </ul>
    <!-- Tab panes -->
    <div class="tab-content">
      <div class="tab-pane fade in active" id="bio">
      <p>Jason Striker is an advocate and educator who facilitates intercultural, interpersonal and meaningful discourse. His specialization in digital communication, social media and online community building fosters the know-how and know-why, to support accessibility and accountability — for all — within online mediums. He strives to teach how to communicate effectively and judiciously, digitally and face to face.</p>
      <p>Jason serves the ASU Community as the communication manager for the University Technology Office; as a teaching assistant for COM 324; is the Vice President of Professional Development for the Graduate Professional Student Association, volunteers nationally with the National Assocation of Graduate &amp; Professional Students (NAGPS) as their Director of Relations, and serves on the Committee for Campus Inclusion (CCI).</p>
      </div>
      <div class="tab-pane fade" id="research">
        <h3>Profile example tab</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu felis, blandit a lorem nec; adipiscing pretium est. </p>
      </div>
      <div class="tab-pane fade" id="vitae">
        <h3>Profile example tab</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu felis, blandit a lorem nec; adipiscing pretium est.</p>
      </div>
    </div><!-- /.tab-content -->
  </div>
</div>

```html
<!-- Example profile -->
<div class="profile">
  <div class="profile-heading">
    <div class="row">
      <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4">
        <div class="profile-pic">
          <img src="http://placehold.it/266x266" alt="Jason Striker" class="img-responsive space-bot-md">
        </div>
      </div>
      <div class="col-xs-12 col-sm-5 col-md-5 col-lg-6">
        <p>
          <strong>Jason Striker</strong><br>
          Manager Communications (UTO)<br>
          UTO Planning and Programs<br>
          University Staff
        </p>
        <p>
          <a href="#">Jason.Striker@asu.edu</a><br>
          <a href="#">(480) 727-5426</a><br>
          Mail Code: 0101
        </p>
        <p>
          Student Information<br>
          Graduate Student<br>
          Communication Studies<br>
          New Interdis Arts &amp; Sciences
        </p>
      </div>
      <div class="col-xs-12 col-sm-3 col-md-3 col-lg-2">
        <ul class="profile-actions">
          <li><a href="#">Print Profile</a></li>
          <li><a href="#">Update Profile</a></li>
          <li><a href="#">Report Abuse</a></li>
        </ul>
      </div>
    </div><!-- /.row -->
  </div>
  <ul class="nav nav-tabs">
    <li class="active"><a href="#bio" data-toggle="tab">Bio</a></li>
    <li><a href="#research" data-toggle="tab">Research Interests</a></li>
    <li><a href="#vitae" data-toggle="tab">Curriculum Vitae</a></li>
  </ul>
  <!-- Tab panes -->
  <div class="tab-content">
    <div class="tab-pane fade in active" id="bio">
    <p>Jason Striker is an advocate and educator who facilitates intercultural, interpersonal and meaningful discourse. His specialization in digital communication, social media and online community building fosters the know-how and know-why, to support accessibility and accountability — for all — within online mediums. He strives to teach how to communicate effectively and judiciously, digitally and face to face.</p>
    <p>Jason serves the ASU Community as the communication manager for the University Technology Office; as a teaching assistant for COM 324; is the Vice President of Professional Development for the Graduate Professional Student Association, volunteers nationally with the National Assocation of Graduate &amp; Professional Students (NAGPS) as their Director of Relations, and serves on the Committee for Campus Inclusion (CCI).</p>
    </div>
    <div class="tab-pane fade" id="research">
      <h3>Profile example tab</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu felis, blandit a lorem nec; adipiscing pretium est. </p>
    </div>
    <div class="tab-pane fade" id="vitae">
      <h3>Profile example tab</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu felis, blandit a lorem nec; adipiscing pretium est.</p>
    </div>
  </div><!-- /.tab-content -->
</div>
```

<!--break-->

## Visit Campus

You can set up map blocks with the following markup:

<div class="bs-example">
  <div class="panel campus-visit">
    <div class="panel-body">
      <div class="row">
        <div class="col-sm-8 col-md-8">
          <h2>Visit our campus</h2>
        </div>
        <div class="col-sm-4 col-md-4">
          <button class="btn btn-primary pull-right">plan a visit</button>
        </div>
      </div><!-- /.row -->
      <address>
        <strong>Ira A. Fulton Schools of Engineering</strong><br>
        Arizona State University<br>
        P.O. Box 9309<br>
        Brickyard 6th Floor<br>
        Tempe, Arizona 85287-9309
      </address>
      <p>
        Administration: <a href="tel:480-727-5232">(480) 727 5232</a><br>
        Advising &amp; Student Services: <a href="tel:480-727-1874">(480) 727 1874</a>
      </p>
    </div>
    <div class="iframe-overlay"></div>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13319.17492398412!2d-111.9342584088297!3d33.428621644147384!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xa4e1b8ff83743e70!2sIra+A.+Fulton+School+of+Engineering!5e0!3m2!1sen!2sus!4v1406847501040" width="100%" height="225" frameborder="0" marginheight="0" marginwidth="0" scrolling="no"></iframe>
  </div>
</div>
```html
<div class="panel campus-visit">
  <div class="panel-body">
    <div class="row">
      <div class="col-sm-8 col-md-8">
        <h2>Visit our campus</h2>
      </div>
      <div class="col-sm-4 col-md-4">
        <button class="btn btn-primary pull-right">plan a visit</button>
      </div>
    </div><!-- /.row -->
    <address>
      <strong>Ira A. Fulton Schools of Engineering</strong><br>
      Arizona State University<br>
      P.O. Box 9309<br>
      Brickyard 6th Floor<br>
      Tempe, Arizona 85287-9309
    </address>
    <p>
      Administration: <a href="tel:480-727-5232">(480) 727 5232</a><br>
      Advising &amp; Student Services: <a href="tel:480-727-1874">(480) 727 1874</a>
    </p>
  </div>
  <div class="iframe-overlay"></div>
  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13319.17492398412!2d-111.9342584088297!3d33.428621644147384!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xa4e1b8ff83743e70!2sIra+A.+Fulton+School+of+Engineering!5e0!3m2!1sen!2sus!4v1406847501040" width="100%" height="225" frameborder="0" marginheight="0" marginwidth="0" scrolling="no"></iframe>
</div>
```

