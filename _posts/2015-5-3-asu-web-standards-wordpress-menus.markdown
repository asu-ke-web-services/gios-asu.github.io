---
layout: post
title: Menus
description: "Menus and menu options that you can use in WordPress"
tags: ["ASU Web Standards WordPress"]
image:
  feature: board.jpg
  credit: Drew Patrick
  creditlink: https://ununsplash.imgix.net/32/6Icr9fARMmTjTHqTzK8z_DSC_0123.jpg?q=75&fm=jpg&s=bd8827942e8be9220eb2d0e58844b01e
---

This theme supports two main menus: a main navigation menu and a footer menu. 

<!--break-->

## Main Navigation

The main navigation menu only supports a max of three levels.  The top level
of the menu will be the pills/tabs that you see in the menu. The second level will
create a basic dropdown under that pill.  A third level will force that dropdown
to become a "Mega Menu." 

Only the lowest level of pills will actually be clickable. If you create a three level deep menu, only the deepest pills will be links.

If you want to indicate that links will exit your website in the menu, go to `Custom Options->CSS Classes` and manually add the class `external-link` to you menu item.  It will add an external link icon to the right of your menu item.

<!--break-->

## Footer Menu

When creating the footer menu, we recommend clicking on "Screen Options" on the top right corner of the admin panel and selecting "CSS Classes".

Creating a Footer Menu is as easy as 1-2-3:

1. Click "Create Menu" and create top level menu items such as "Academics", "Connect", "Impact", "People", and edit these top level items to have "#" as the URL link and "h2" has the "CSS Classes (Optional)".
2. Use the "Pages" tab to add links under the top level menu items to specific pages.
3.  Click the checkbox next to "Footer Menu" in "Menu Settings" and then click "Save Menu". Your menu will now appear at the bottom of the page!
