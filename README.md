# DjangoModels
Zuri Django Models Task

## Activities
Created an app named blog and installed it

Created a new model in the blog app called post and added the following fields

Title : A string of maxlength 200, use Django’s models.CharField

Text : Any amount of text, use Django’s TextField

Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

Created_date : A date-time column, use Django’s models.DateTimeField. 

Published_date : A date-time column, use Django’s models.DateTimeField.

Created migrations for your new model using the makemigrations Django command. 

Ran all migrations using the migrate Django command.