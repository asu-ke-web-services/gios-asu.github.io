---
layout: post
title: Page Features
description: "Setting up your page features"
tags: ["GIOS WordPress"]
image:
  feature: camera.jpg
  credit: Bastian Sara
  creditlink: https://ununsplash.imgix.net/photo-1420721690512-d1f4b58c5f9b?q=75&fm=jpg&s=90f28ba1c527dfeeda70bc3ac9fe0511
---

On each of your pages on your WordPress site, you can have a page feature which can have a "hero image" &emdash; a large, action oriented, visually appealing image that sets the tone of the page.

In order to use the Page Feature functionality, enable `Custom Fields` by editing a Page, clicking on `Screen Option` on the top right corner, and selecting `Custom Fields`.

<!--break-->

## Page Feature Image

You can have large hero image appear at the top of your image by adding a custom field:

| Name                     | Value                      |
|--------------------------|----------------------------|
| page_feature_description | /files/2015/02/example.jpg |

It is recommended that you upload your hero image to your Media, but you can reference an image that resides on a different server by using a absolute URL.

## Page Feature Title

You can have large text appear on top of your hero image by adding a custom field:

| Name               | Value                      |
|--------------------|----------------------------|
| page_feature_title | The Page Title             |

## Page Feature Description

You can have large descriptive text appear on top of your hero image, but below your title text by adding a custom field:

| Name                     | Value                      |
|--------------------------|----------------------------|
| page_feature_description | A longer descriptive text that will word rap for you |


## Page Feature Type

This is a special custom field that will change the behavior of the page feature and the hero image.

| Name              | Value                      |
|-------------------|----------------------------|
| page_feature_type | default                    |

Values can be:

* `default`: this is the normal behavior of the page feature. The page feature will have a static height and the hero image will scale to cover the page feature area.
* `ratio`: the page feature and the hero image will scale to have a height of 30% of the width.
* `slim`: this is very similar to the default behaviour, but the height of the page feature will be 70px.

If you do not have the `page_feature_type` set, it will default to `default`.