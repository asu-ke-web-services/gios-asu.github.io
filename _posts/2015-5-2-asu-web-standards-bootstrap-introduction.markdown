---
layout: post
title: ASU Web Standards Bootstrap Introduction
description: "An introduction to what the ASU Web Standards are and how to use the ASU Web Standards Bootstap Repo."
tags: ["ASU Web Standards Bootstrap"]
image:
  feature: empty-track.jpg
  credit: Francisco Casero
  creditlink: https://ununsplash.imgix.net/25/empty-track.jpg?q=75&fm=jpg&s=ff243e360ba24d29009695c0dce4e71a
---

The [ASU Web Standards Bootstrap Github repository](https://github.com/gios-asu/ASU-Web-Standards-Bootstrap) is a barebones, platform independent implementation of the new web standards outlined by the [ASU Enterprise Marketing HUB](https://hub.asu.edu/).  It's main purpose is to provide styling for websites that are not in Drupal or WordPress.

The repository contains CSS, JavaScript, and font files that you can use as a foundation for your website, in conjunction with Twitter Bootstrap and jQuery. 
~~~

## Dependencies

The following dependencies are required for the Web Standards to work correctly on your website:

- [Twitter Bootstrap](http://getbootstrap.com/)
- [jQuery](http://jquery.com/)
- [Lightning Touch](https://github.com/ucsf-ckm/LightningTouch)
- [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
- [Moment JS](http://momentjs.com/) - Used for calendar ICS files.
- [ASU Header](https://drupal.asu.edu/build/asu-header-footer-version-40)

If each webpage on your website includes the above CSS and JavaScript plugins, then you are ready to include the web standards in your website!
~~~

## Installing the Web Standards

You can use one of the following ways to use this repo:

- [Download the latest release](https://github.com/gios-asu/ASU-Web-Standards-Bootstrap/releases).
- Clone the repo: `git clone https://github.com/gios-asu/ASU-Web-Standards-Bootstrap.git`.

The files that you should include in your website are the ones in `/build`.

Add the following to your head (after your stylesheets for bootstrap):

```html
<!-- ASU Bootstrap Standards -->
<link href="/css/bootstrap-asu.css" rel="stylesheet">
<link href="/css/bootstrap-asu-theme-base.css" rel="stylesheet">
```

Add the following to the end of your `<body>` before the closing `</body>` tag, but after your other script tags:

```html
<!-- ASU Bootstrap Standards -->
<script src="./js/bootstrap-asu.min.js"></script>
```

Please remember to include all of the [dependencies](#dependencies).  Include all 3rd party stylesheets and scripts BEFORE including the stylesheets and scripts provided in this repo.

For developers or when debugging, consider using the non-minified JavaScript files and adding the `*.map` files to where your `*.css` files are.
~~~

## Details

This theme uses [Font Awesome](http://fortawesome.github.io/Font-Awesome/).  Bootstrap natively provides Glyphicons, which means both can be used in tandiem.

This theme uses the Google Font Roboto.  If you do not include Roboto in your website using the instructions provided on [Google Font's website](http://www.google.com/fonts/specimen/Roboto), the font will default to 'Helvetica Neue', then Helvetica, then Arial, then the browser's default sans-serif font.

For more information concerning all of the new components and CSS styles that are introduced in this theme, check out [https://gios-asu.github.io/](https://gios-asu.github.io/).

