# EM-Commerce
# Table of Contents
* [Introduction](#introduction)
* [User Expereince (UX) design](#1-user-expereince-ux-design)
    * [User Goals](#11-user-goals)
    * [User Expectations](#12-user-expectations)
    * [Color Scheme](#13-color-scheme)
    * [Images and Log](#14-images-and-logo)
    * [Site Skeleton](#15-site-skeleton)
* [Features](#2-features)
    * [Main Section](#main-section)
* [Technologies Used](#3-technologies-used)
* [Testing](#4-testing)
    * [Testing tools](#41-testing-tools)
    * [Manual Testing](#42-manual-testing)
    * [Lighthouse Reports](#43-lighthouse-reports)
* [Bugs](#5-bugs)
* [Deployment](#6-deployment)
* [Acknowledgement](#7-acknowledgement)

Welcome to [E.M-Commerce!](https://em-comm.herokuapp.com/)

# Introduction

E.M-Commerce is an online shop which can sell all kind of products from clothes to big home appliances. The app was build with HTML, CSS, JavaScript,Python and Django. The main purpose of the project is to Create, Read, Update and Delete (CRUD) entries in a database and display them, integrate payment system with Stripe and in the same time trying to give a good user experience.

![responsive image](/media/responsive1.PNG)
![responsive image](/media/responsive2.PNG)
![responsive image](/media/responsive3.PNG)

# 1. User Expereince (UX) design

* The site structure is designed considering the expectation of users to be simple and easy to use;
* The user interface is easy to navigate;
* The app is interactive, with nice alerts after each action;
* Responsive design for all screen/device sizes like mobile, tablet and desktop;


# 1.1 User Goals

The app is designed for shoppers that want to do their shopping online and secure;

# 1.2 User Expectations

The content of the app changes at every action of a user. Folloiwng user's expections ware considered while designing the site:

* The site structure is designed considering the expectation of users to be simple and easy to use;
* The user interface is easy to navigate;
* Responsive design for all screen/device sizes like mobile, tablet and desktop;

# 1.3 Color Scheme

The choice of website right foreground and background colour is essential that decides the site visitors wheather to emote the site or not. I used [Color Hunt](https://colorhunt.co/) to select the background and foreground color. Colors that i used are:

* the content it`s mostly blank and white and because the app will store many images it will take the colors from them;
* and some bootstrp5 colors: warning, info, primary, alert

# 1.4 Images and Logo

This website was created for academic purposes, all photos were searched and downloaded from [Giphy website](https://giphy.com/) and [Google search](https://google.com/)

# 1.5 Site Skeleton

[Balsamiq](https://balsamiq.com/) was used to create wireframes of the website. This was very useful as it gives the template of the UI. Wireframes were designed for web browser and a mobile browser format:

## Main Page:
![Main page whireframe image](/media/main-page.PNG)

# 2. Features

# Main Section

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* Banner is centered on the top 
* Products are listed on the main page using OwlCarousel 
* Popular categories are listed on the main page with catecogires links


## Products Page:
![Products page whireframe image](/media/products-page.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* Side menu to filter products by category, price and rating
* Products are displayed with names, price, category and rating


## Products Details:
![Products Details page whireframe image](/media/product-detail.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* Product image is shown on the left side
* Product details are on the rigth side with review stars also
* Under the product details I have added product reviwe. A user must be logged in to be able to submit a review


## Cart:
![Cart page whireframe image](/media/cart.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* A teble is displayed with the products added to cart. In the table I put product image, product variation if it`s the case, an input to increse and decrese the product quantity, a button to remove the product from cart no metter the quantity added.
* On the right side I displayed the total of the purchase with price for items, VAT and delivery and to buttons one for checout and one to go back to products search


## Checkout:
![Cart page whireframe image](/media/checkout.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* A form is displayed on the left to compleate shipping details.
* On the right side si a table with products that you are about to pay with details and price.
* Under the form is an input from Stripe to add card details with two buttons one to go back to the cart and one to proced checkout

## Checkout Informations:
![Cart page whireframe image](/media/checkout-infromation.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* A list with checkout information is displayed including order number, shipping details and Personal Informations
* Under the list I put a button to go to the perosnal profile