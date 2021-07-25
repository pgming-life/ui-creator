# [UI Creator](https://pgming-ui-creator.com/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/pgming-life/ui-creator/blob/main/LICENSE)

*UI Creator* is a service platform that allows users to manually place widgets, visually adjust their position and size, and output and download them as program code.  
It provides visual fine-tuning of input values for size and position on the program.  
However, please note that this app currently only supports Japanese.

![ui-creator-site](https://user-images.githubusercontent.com/84230279/126889440-572fb4b2-093b-49d8-982f-462cd2e69d78.png)

#### :exclamation:Be careful:exclamation:
The web application linked above does not always match the actual source code.  
It will be uploaded to the release repository on a regular basis.  

## We welcome active OSS activities!!
The first code is poor, but we will continue to improve this web application.
Please feel free to join us.:four_leaf_clover:

## Includes

**Git:**  
Download-> https://git-scm.com/download
```
$ mkdir ui-creator
$ git clone --depth 1 https://github.com/pgming-life/ui-creator.git ui-creator
```

**Backend:**
* Python (https://www.python.org/downloads/)
* Django
```
$ pip install Django==2.2.5
```
* Django REST framework
```
$ pip install djangorestframework==3.12.4
```

**Frontend:**
* Node.js (https://nodejs.org/en/download/)
* Vue CLI 3
```
$ npm install -g @vue/cli
```
* Vuetify
```
$ vue add vuetify
```

## Technology used

* Nginx
* Gunicorn
* Python3.8.2
* Django
* Django REST framework
* SQLite3 - development (virtualenv)
* PostgreSQL - release (psycopg2)
* Node.js
* Vue CLI 3
* Vuetify
* Vuex
* Vue Router

## License

MIT License (see [`LICENSE`](/LICENSE) file).
