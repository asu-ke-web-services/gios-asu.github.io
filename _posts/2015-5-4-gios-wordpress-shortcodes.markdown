---
layout: post
title: Shortcodes
description: "All of the WordPress shortcodes that are available to you."
tags: ["GIOS WordPress"]
image:
  feature: desk.jpg
  credit: Jeff Sheldon
  creditlink: https://ununsplash.imgix.net/photo-1416339684178-3a239570f315?q=75&fm=jpg&s=c39d9a3bf66d6566b9608a9f1f3765af
---

The combination of themes and plugins that the GIOS Multisite installation uses allow you to use a wide variety of shortcodes in your Posts, Pages, and templates.

<!--break-->

## Events Short List

```php
[events-short limit=number]
```

The `events-short` shortcode takes in a `limit` and grabs the upcoming `limit` number of events and outputs a list of the events. 

The events that the shortcode grabs are determined by the event categories that are set in `Administration -> GIOS Settings`.

The name is a bit of a misnomer since it does not output an actual list, but rather paragraph tags.

Here is some example output:

```php
[events-short limit=2]
```

```html
<p class="short-event">
  <a href="https://schoolofsustainability.asu.edu/events/rsvp/intel-sustainable-building">
    Feb 13 - 2015 Intel Sustainable Buildings Conference Industry Expert Panel
  </a>
</p>
<p class="short-event">
  <a href="https://schoolofsustainability.asu.edu/events/rsvp/sos-volunteer-project">
    Feb 14 - Show the Garden Some Love!
  </a>
</p>
```

<!--break-->

## Events Blurb

```php
[events-blurb slug='slug']
```

The `events-blurb` shortcode takes in a `slug` and grabs that event and outputs the markup for the blurb view.

The slug should be a valid event slug obtained from the GIOS DB.

Example usage and output:

```php
[events-blurb slug='intel-sustainable-building']
```

```html
<div class="event event-blurb asu-box">
  <h2 class="title">
    <a name="intel-sustainable-building" href="https://schoolofsustainability.asu.edu/events/rsvp/intel-sustainable-building">
      2015 Intel Sustainable Buildings Conference Industry Expert Panel
    </a>
  </h2>

  ...
</div>
```

<!--break-->

## Events Detail

```php
[events-detail slug='slug']
```

The `events-blurb` shortcode takes in a `slug` and grabs that event and outputs the markup for the detailed view.  This does not include the RSVP form.

The slug should be a valid event slug obtained from the GIOS DB.

This shortcode should be used very rarely and it is recommended to use the `[events-blurb]` shortcode instead.

Example usage:

```php
[events-detail slug='intel-sustainable-building']
```

<!--break-->

## News Slider

TODO

<!--break-->

## Media List

```php
[list-gios-media type='slug' limit='number']
```

The `list-gios-media` shortcode takes in a category `slug` and displays `limit` number of media from that category.

The limit defaults to 10 if not included.

<!--break-->

## Media Thumbnail

```php
[gios-media-thumb slug='slug']
```

The `gios-media-thumb` shortcode takes a media `slug` and displays a thumbnail view of that media object.

<!--break-->

## Media Detail

```php
[gios-media slug='slug']
```

The `gios-media` shortcode takes a media `slug` and displays a detailed view of that media object.

<!--break-->

## Iframe

```php
[iframe src='url' width='number' height='number']
```

The `iframe` shortcode takes in a `src`, `width`, and `height`, and generates the HTML markup for the iframe.