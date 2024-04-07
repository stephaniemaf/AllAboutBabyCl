# Introduction

This is a blog created in Django. My Blog name is All About Baby. This Blog is intended to give users information about babies threw thier first year of life. The posts in this blog are related to baby development and feeding. There is a navigation bar at the top of the page and from the blog page you can navigate to a page with recipes. On this recipe page you will find recipes for feeding your baby there first foods. You are able to sign into this website and as an authenticated user you will be able to leave comments and like/unlike posts and recipes. You are to log out and register to the site also. There is an admin panel for Admin users the loh in information for his will be found at the end of this ReadMe.
The data base for my blog is hosted on [elephantsql](https://www.elephantsql.com/) 
The site will be deployed threw [Hreoku](https://id.heroku.com/)
Images stored on [cloudinary](https://cloudinary.com)

# How to begin

When you first get to my webside blog you can see posts and recipes by navigating through the nav bar at the top. If you want to leave comments you must register first as a user of the site. Once registered you will be able to not only see the posts and recipes but you will be able to leave comments on posts and you will be able to like them also.

Once you leave a comment you will see an edit and delete button under your own comment. If you click on either button you will be brought to a new form page. From here you can edit or delete your commetn depending on which button you clicked. Once the action has been preformed, you will be redirected back to the post or recipe that you clicked the button on.

# Blog Functionality

## Templates

In the directories base.html is the main template and my other templates inherit from that 
Index.html is the form that handles displaying my blog posts and post_detailholds my comment form and ability to like posts.
For the recipe page i dublicated these templates and renamed them. so Recipe_index.html and Recipe_detail.html. These forms handle the recipe posts and comments respectivaly. I have seperate forms for updating and deleting comments these also inhereit from base.html and i have templates ffor creating a recipe and subscribing to the newsletter.

## Authorisaton

Djnago framworks have the ability to implement an admin feature here i am able to Approve comments before the can be seen by the user. I can write adn deploy my block posts and i can also create a user name and password from this admin site. On the admin panel there are roles and permissions. The abilty to create an admin(superuser) and this person had the abily to preform all parts of crud on the site for each model. 

As a registered site user you have the ability to create recipes for the blog and you are able to leave comments for both recipes and blog posts and you can also update and delete these comments. Therby manipulating the database from the front end as a user. 


## Login and Registration

Threw Djangos authentication system-openid, i implemented login/logout abiliies and the ability to register as a user for the site. As a registered user you can like and unlike posts and you are able to create a passowrd to log in. You are able to change your password aswell if you have fogotten it. 

## Database management

In order to create models and store recipes and blog posts i used [elephantsql](https://www.elephantsql.com/). When Creating,Updating or Deleting parts of the models you make migrations threw the terminal window in using the code - (python3 manage.py makemigrtaions) and if everything looks good you can proceed with (python3 manage.py migrate). This will update the database on elephantsql. These models are Post, Comment, Recipe and Subscribe

## CRUD

By logging into the admin panel The super user has the ability to preform full crud functionality my creating posts deleting them, updating usernames and passwords. Users can read all posts like/and unlike posts create profiles and change login information. Registered users of the site can Comment on Posts and Recipes, Like and Unlike posts they enjoy, Users and now Update(edit) and Delete their comments and now can add a Recipe they would like to share with others. Users must wait for admin approval of their comments and uploaded recipes and will recieve a message about this after they are redirected back to the page they where on when commenting or adding a recipe.

## Images

When creating blog posts users have the ability to use there own images and if they fail to upload one a default image has been provided in the index.html file.

# Testing


I will be manually testing my Blog for this project!

## Home Page:
To begin with i started testing the the Home page.
The nav bar contains 5 nav links a background image with text overlay and a footer with 2 social media links.

### The nav bar:
Expectation = I expect to be able to click on each nav link and be brought to the page they are linked to.
Result = These worked as expected i clicked on each link and was brought to their respective pages untill i added the new home page nav link. When i first clicked this link it brought me to the blog page instead of the new home page.

Fix = I had to update the urls.py as origionally my blog page was called home and i renamed it to blog, so both url paths where leading to the blog page. [path('blog/', views.PostList.as_view(), name='blog'),] i had left the single quotes empty but adding blog here fixed my issue

The home page has a background image with text overlay. This is centered and stretched to fit the whole screen there are no buttons on links here

### The Footer:
Expectation = I expect the footer to have the words Made by stephanie and links to facebook and instagram. I want these links to lead to the home page of their respective sites.
Result = I clicked on each link and am brought to the front page of their respective sites.

# The Blog page:
To get here i clicked the blog nav link. On this page  i have blog posts. To test this i chose the first blog post on the page. 
Expectation = I ecpected to cleack on the blog post and be brought to the post content where i would fine and image at the top of the page followed by the post content and under this a form for leaving comments on the bottom right and a list of comments on the left. I used content_type in my Comment model as i was using this model for both Blog posts and Recipes. I needed to use it to keep track of all my models in order to assign the right comments with theyre respective posts.
Result = I clicked on the post and recieved and an attribute error for content type so i went back to my view page and imported content type at the top of the file and reloaded the page and there was no error now.

# bugs 
As of right now there is no known bugs on the site that i am aware of.

# Validator Testing

## Tested on [Validator](https://pep8ci.herokuapp.com/)
Code passed through validator with no issues
![val](images/val.png)
![val1](images/val1.png)
![val2](images/val2.png)
![val3](images/val3.png)
![val4](images/val4.png)


# Credits 
I took ideas for this project from the code institute walkthrough I think therforeI blog.

# Important links
Link to my GitHup repository

* Hosted on heroku

# notes
Before i started this module i had a baby and doing this project with a newborn was quite intense and difficult i wasnt able to put in the amount of work and time i was before and its reflected in my work i understand i may not pass today but in the mean time i will keep learning and hopfully if i need to resubmit it will be up to the standard i want and is needed. 