---
layout: post
title: Getting Started
description: "An introduction to what the ASU Web Standards are and how to use the ASU Web Standards Bootstap Repo"
tags: ["ASU Web Standards Bootstrap"]
image:
  feature: path.jpg
  credit: Francisco Casero
  creditlink: https://ununsplash.imgix.net/25/empty-track.jpg?q=75&fm=jpg&s=ff243e360ba24d29009695c0dce4e71a
---

The [ASU Web Standards Bootstrap Github repository](https://github.com/gios-asu/ASU-Web-Standards-Bootstrap) is a barebones, platform independent implementation of the new web standards outlined by the [ASU Enterprise Marketing HUB](https://hub.asu.edu/).  It's main purpose is to provide styling for websites that are not in Drupal or WordPress.

The repository contains CSS, JavaScript, and font files that you can use as a foundation for your website, in conjunction with Twitter Bootstrap and jQuery.

If you are creating a WordPress website, we recommend using the [Wordpress Theme]({% post_url 2015-5-3-asu-web-standards-wordpress-getting-started %}) to integrate the web standards into your website.

If you are creating a Drupal website, please use [WebSpark](http://webspark.asu.edu/).


<!--break-->

## Dependencies

The following dependencies are required for the Web Standards to work correctly on your website:

- [Twitter Bootstrap](http://getbootstrap.com/)
- [jQuery](http://jquery.com/)
- [Lightning Touch](https://github.com/ucsf-ckm/LightningTouch)
- [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
- [Moment JS](http://momentjs.com/) - Used for calendar ICS files.
- [ASU Header](https://drupal.asu.edu/build/asu-header-footer-version-40)

If each webpage on your website includes the above CSS and JavaScript plugins, then you are ready to include the web standards in your website!

<!--break-->

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

Please remember to include all of the dependencies.  Include all 3rd party stylesheets and scripts BEFORE including the stylesheets and scripts provided in this repo.

For developers or when debugging, consider using the non-minified JavaScript files and adding the `*.map` files to where your `*.css` files are.

<!--break-->

## Details

This theme uses [Font Awesome](http://fortawesome.github.io/Font-Awesome/).  Bootstrap natively provides Glyphicons, which means both can be used in tandiem.

This theme uses the Google Font Roboto.  If you do not include Roboto in your website using the instructions provided on [Google Font's website](http://www.google.com/fonts/specimen/Roboto), the font will default to 'Helvetica Neue', then Helvetica, then Arial, then the browser's default sans-serif font.

For more information concerning all of the new components and CSS styles that are introduced in this theme, check out [Components]({% post_url 2015-5-2-asu-web-standards-bootstrap-components %}) and [CSS]({% post_url 2015-5-2-asu-web-standards-bootstrap-css %}).

### Repo Structure

When you download the repository, you will need to following files from the Github Repo:

```bash
build/
├── css/
|   ├── bootstrap-asu.css
|   └── bootstrap-asu-theme-base.css
├── js/
│   ├── bootstrap-asu.js
└── fonts/
    ├── fontawesome-webfont.eot
    ├── fontawesome-webfont.svg
    ├── fontawesome-webfont.ttf
    ├── fontawesome-webfont.woff
    └── FontAwesome.otf
```

This is the most basic form of the Web Standards.  They are precompiled files for quick drop-in usage of any project that uses Bootstrap.  We provide CSS, JS, and font files for convenience. Fonts from FontAwesome are included.

When integrating the Web Standards into a Bootstrap project, you will get the following directory structure:

```bash
webroot/
├── css/
│   ├── bootstrap.css
│   ├── <b>bootstrap-asu.css</b>
│   ├── <b>bootstrap-asu-theme-base.css</b>
├── js/
│   ├── jquery.js
│   ├── bootstrap.js
│   ├── <b>bootstrap-asu.js</b>
└── fonts/
    ├── <b>fontawesome-webfont.eot</b>
    ├── <b>fontawesome-webfont.svg</b>
    ├── <b>fontawesome-webfont.ttf</b>
    ├── <b>fontawesome-webfont.woff</b>
    └── <b>FontAwesome.otf</b>
```

<!--break-->

## Theming

Theming is done by creating your own `boostrap-asu-theme-base.css`.  This CSS file controls only the colors that appear on your website.

The SASS files that are used to create a theme base are in `scss/custom`. The `_variable.scss` file contains all of the color codes used to theme an ASU website. 

In order to compile your SASS files into a CSS file, use a SASS processor to compile `bootstrap-asu-theme-base.scss`.  This will create a custom version of `boostrap-asu-theme-base.css` that you can use on your website.

We recommend using [Grunt](http://gruntjs.com/). Please see the [actual repository](https://github.com/gios-asu/ASU-Web-Standards-Bootstrap) for in-depth details for developers.