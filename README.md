# My Personal Website

I use Django to built my website.

## Virtual Enviroment

Recommend use **virtualenv**

``` text
pip install virtualenv
virtualenv <enviroment-name>

.\<enviroment-name>\Scripts\activate # PowerShell
source <enviroment-name>/bin/activate # Linux
```

### Import Packages

Use this command to import all packages.

`pip install -r .\requirements.txt`

## Demo

* Online

  I put the website on **pythonanywhere**.

  Check out et860525.pythonanywhere.com
* Offline

  After you download my project, you need to create a file call **`.env`** put it into **`.\web\`** folder(same with `settings.py`).

  Put some parameters into this file and make sure this project can work on your PC.

  ``` text
  SECRET_KEY=django-insecure-d!!+%r0s1f-mo0$74#iul*u%pesbel6#0e47$!^n%bopo7m%z9

  EMAIL_HOST_PASSWORD= # For your email password
  EMAIL_HOST_USER=     # For your email username

  SQL_NAME= # SQL name
  SQL_USER= # SQL user
  SQL_PASSWORD= # SQL password
  SQL_HOSTNAME=localhost
  ```
