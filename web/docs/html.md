# Html documentation
## Overview
The website mainly uses [Bootstrap](https://getbootstrap.com) to get a proper layout regardless of what device we used to open it.
## File structure
- [index.html](https://github.com/gedand/452c8c82-Virucid/blob/main/web/index.html): Main page, every uploaded pictures can be found here.
- [login_register.html](https://github.com/gedand/452c8c82-Virucid/blob/main/web/login_register.html): Starting page, before we could view/download any pictures, we have to register/login to the site.
- [single_image.html](https://github.com/gedand/452c8c82-Virucid/blob/main/web/single_image.html): After clicking on any image found on the main page, we are redirected to this page, containing a single picture and all the comment for it.

## Login / Registration
There is a single administrator by default, no more can be registered(The password setup is explained [here](https://github.com/gedand/452c8c82-Virucid/tree/main/backend/config))

User login very simple.

![User login](https://github.com/gedand/452c8c82-Virucid/blob/main/web/docs/pics/login.jpg)

The basic user registration is very simple, but the password needs to meet certain requirements:
- At least **10 characters** long
- Needs to contains at least **1 number**, **1 lowercase** and **1 uppercase** character.

![User registration](https://github.com/gedand/452c8c82-Virucid/blob/main/web/docs/pics/register.jpg)
