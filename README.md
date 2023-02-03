# product-management

###### For running this project, create a virtual environment with the command-
```python -m venv venv```
###### Activate the environment with-
```venv\scripts\activate```            (For Windows)

```source venv/bin/activate```         (For Linux)

###### Install all the requirements from the requirements.txt file with the command-
```pip install -r requirements.txt```
###### Go to the project directory with -
```cd Name_of_the_directory```
###### Run the poject with the command-
```python manage.py runsever```


## Technology Used-
-Django
-Django Rest Framework
-drf-yasg
-rest_framework_simplejwt


** In this project three apps are core, product, and user.
** User app is for the user, product app is for the products and core is common for both.
** I stored all the models in the core app.
** For user I create custom user, I mean instead of a username I used an email. And for user id, I used uuid.
** Fore product app there is 3 models (ProductCategory, Product, ProductImage). In product app, I added SlugField for getting the product details.
** For documentation I used drf-yasg and authentication simplejwt.
For product images, we can upload multiple images as a list.


## By doing this project I came to know -
-How to work with django rest framework
-How to work with API documentation
-How to work with third parties app
-How API Authentication works
-How API views and generics views are works
-How to work with multiple image upload
-How to write test
