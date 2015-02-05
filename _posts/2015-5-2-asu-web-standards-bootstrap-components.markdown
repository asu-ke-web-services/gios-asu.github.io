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

### Single Tab

TODO

### Simple Menu

TODO

### Mega Menu

TODO

<!--break-->

## Mega Footer

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
<div class="hero hero-bg-img hero-action-call" style="background-image: url(image_url);">
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

TODO


