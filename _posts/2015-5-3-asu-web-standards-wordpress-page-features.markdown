---
layout: post
title: Page Features
description: "Setting up your page features and hero images"
tags: ["ASU Web Standards WordPress"]
image:
  feature: person-with-camera.jpg
  credit: Ryan Tauss
  creditlink: https://unsplash.imgix.net/photo-1417577354685-3ab67e9716a3?q=75&fm=jpg&s=9a7442ea2b03579ef288da44a7602af5
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

Currently only default is supported.