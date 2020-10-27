PASSWORD:
    1- user authentification: we need  to add to settings.py (installed_apps) "django.contrib.auth" and "django.contrib.contenttypes" AND migrate after added them;
    2- Never store passwords as plain text!!!;
    3- We will use PBKDF2 algorithm with SHA256 hash (built-in to django);
    4- we need to use also bcrypt and Argon2(opensource alghorithm haching);
    5- pip install bcrypt;
    6- pip install django[argon2];
    