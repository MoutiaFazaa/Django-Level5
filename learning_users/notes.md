PASSWORD:
    1- user authentification: we need  to add to settings.py (installed_apps) "django.contrib.auth" and "django.contrib.contenttypes" AND migrate after added them;
    2- Never store passwords as plain text!!!;
    3- We will use PBKDF2 algorithm with SHA256 hash (built-in to django);
    4- we need to use also bcrypt and Argon2(opensource alghorithm haching);
    5- pip install bcrypt;
    6- pip install django[argon2];
    7- in AUTH_PASSWORD_VALIDATORS we can use 'OPTIONS' like 'min_length' (check settings.py line 101) , other options of options in django documentations;
    8- after that we added 3 folders under learning_users folder : templates, static, media and add their DIR under templates_dir and base_dir;
    9- we need to add  in sttings.py media and static configurations:


        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/2.2/howto/static-files/

        STATIC_URL = '/static/'
        STATICFILES_DIRS = [STATIC_DIR,]

        #MEDIA
        MEDIA_ROOT = MEDIA_DIR
        MEDIA_URL = '/media/'

USERS MODELS:

    1- We need to build a user model that contains some attributes, and install the python images library pillow with : pip3 install pillow
    2- the images, js files and css are enregistrated in static folder but the uploaded images are in the media folder by using the media_root on settings.py ... so we need to create a form (forms.py file) to create a form for users.
    3- interaction between models.py and forms.py;
    4- after coding all this we need to import our model to admin.py     :

        from basic_app.models import UserProfileInfo
        # Register your models here.

        admin.site.Register(UserProfileInfo)

    5- 


    

