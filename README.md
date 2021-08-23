# Auckland Locations of Interest scraper

## Overview

This Django app produces a website that shows an up-to-date table of all Covid locations of interest in Auckland, New Zealand, ordered by date updated, with the last added or updated items at the top.  
It is designed to be accessible, easy on the eyes, clear, and readable.  

Since writing this website, the Ministry of Health website updated their locations of interest page to include a sort feature! However, I still find my app useful because it's so clear and quick to read.

## Dependencies

Dependencies are listed in requirements.txt.
Pip can be used to install them.

## Instructions

This repo includes a Python file populate_database.py which can be used to create the initial mysql database and table for the information, and populate it with the current data from the Ministry of Health website.

It also includes a program in main/management/commands/scraper.py that can be used to scrape the Ministry of Health website periodically and update the database with new entries and updates.

In order to be deployed, a database will need to be created and the details added to populate_database.py, get_list.py, and settings.py.
settings.py might also need further configuration.  
The Procfile here is for Heroku deployment. Heroku also reads the requirements.txt automatically.  
Currently gunicorn is installed. To use with Apache or others, further configuration would need to be done.

## Demo

My site is currently deployed on Heroku at https://auckland-loi.herokuapp.com.  
I used a free database from JawsDB MySQL.
