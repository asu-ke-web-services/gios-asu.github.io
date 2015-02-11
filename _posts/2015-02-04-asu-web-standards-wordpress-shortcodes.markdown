---
layout: post
title: Shortcodes
description: "New shortcodes that you can use in WordPress"
tags: ["ASU Web Standards WordPress"]
image:
  feature: tools.jpg
  credit: Todd Quackenbush
  creditlink: https://unsplash.imgix.net/reserve/oIpwxeeSPy1cnwYpqJ1w_Dufer%20Collateral%20test.jpg?q=75&fm=jpg&s=d8cce13e5d977aeec5bdbec256987adf
---


The [ASU Web Standards Wordpress Github repository](https://github.com/gios-asu/ASU-Web-Standards-Wordpress-Theme) provides new shortcodes that you can use when writing pages and posts.

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

