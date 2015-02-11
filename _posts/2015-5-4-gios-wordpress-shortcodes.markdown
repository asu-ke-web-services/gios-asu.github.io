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

```php
[news-slide tag='comma,seperated,list,of,tags' category='comma,seperated,list,of,categories']
```

The `news-slide` shortcode creates a slider from news articles in the given
tags and categories.

<!--break-->

## News List

```php
[news-list tag='comma,seperated,list,of,tags' category='comma,seperated,list,of,categories']
```

The `news-list` shortcode cretaed a slider from news articles in the given
tags and categories.


<!--break-->

## Person Blurb

```php
[person-blurb slug='slug']
[person-blurb id=number]
```

The `person-blurb` shortcode creates blurb markup for the given person based on the `slug` or the `id` passed into the shortcode.

If both a slug and an id are given, only the slug will be used.

<!--break-->

## Group People 

```php
[group-people slug=string (active=true/false) (relationship_type=string)]
```

The `group-people` shortcode creates markup for displaying all people in a group given the group `slug`.  Optional parameters include `active` and `relationship_type`.

* Note: relationship_type is comma seperated and does not support wildcards

<!--break-->

## Group People By Role

```php
[group-people-by-role slug=string (active=true/false) ]
```

The `group-people-by-role` shortcode creates markup for displaying all people in a group in roles.  Optional parameters include `active`. 

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


<!--break-->

## Containers

You can write the boiler plate for a bootstrap container using the following shortcode:

```php
[container]
  Your content
[/container]
```

The container can also be made to appear gray by specifying the gray attribute:

```php
[container gray=true]
  Your content
[/container]
```

You can also override the padding and margins for both container types:

```php
[container type="gray" margin="0" padding="0"]
```

The margin and padding options can be ANY of the following in ANY combination (order of precedence is in order, so `sm` will overwrite `bot-sm`):

```
0, sm, md, lg, xl, top-0, top-sm, top-md, top-lg, top-xl, bot-0, bot-sm, bot-md, bot-lg, bot-xl
```

<!--break-->

## Sidebars

You can write a sidebar for navigating the current page by using the sidebar tag.  The markup looks like this:

```php
[sidebar title='My title']
  Text1|#idOnPage1
  Text2|#idOnPage2
  Text3|#idOnPage3
[/sidebar]
```
