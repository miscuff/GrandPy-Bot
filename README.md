# GrandPy-Bot
GrandPy-Bot is a Flask application. The purpose is to ask a question 
about location to grandpy-bot. He will respond to you by telling 
you a story about the location and he will show you where is it 
with Google map.

Link : https://carl-grandpybot.herokuapp.com/

## APIs 
* [Google Map](https://developers.google.com/maps/documentation)
* [Media Wiki](https://www.mediawiki.org/wiki/API:Main_page)

## Packages

* flask : Python framework to build web app
* pytest : Python framework to make unit test
* heroku : Cloud platform as a service supporting the application

## How to setup the project 
* Clone the repository 
* Install virtual environment

        pip3 install virtualenv
        virutalenv venv
        source venv/bin/activate
* Install requirements

        pip3 install -r requirements.txt

* Get Google map key
    
    - Get an API key following this link : [key](https://developers.google.com/maps/documentation/javascript/get-api-key)
    
* Run the project in Production
    
    - Create an account on heroku following this link : [heroku](https://id.heroku.com/login)
    
    - Set a config var for the API key
        
            heroku config:set GOOGLE_API_KEY="Your API key"
        
    - Deploy the application online :
        
            git push heroku master
            heroku ps:scale web=1

* Run the project in Development

    - Set in file config.py the GOOGLE_API_KEY

            GOOGLE_API_KEY = "your api key"
    
    - Run the program in local
    
            python3 run.py
            
    - Launch tests

            pytest