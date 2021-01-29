# FLASHCARDS

>[Khalid Ali] https://github.com/Alikhalid2020
  
# Description  

This is an application help students remember things by use of  tiny flash cards where they can write anything they think its important. or update them or and delete

##  Live Link  
 Click [View Site]()  to visit the live-site
  
## User Story  
  
A user must be authenticated to see his flashcards.
A user's flash card can contain a title with some notes.
Flashcards should be organized according to subjects/courses.
A user can delete or update a flash card he has created.
A user should see when the flash card was created and when it was last updated.
  
## Setup and Installation  
 
##### Cloning the repository:  
 ```bash 
 https://github.com/Alikhalid2020/FlashCards
```
##### Navigate into the folder and install requirements  
 ```bash 
cd into Instagram
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```

##### Running the application  
 ```bash 
 python manage.py runserver 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8.5](https://www.python.org/)  
* [Django 3.1.3](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Bootstrap4](https://getbootstrap.com/)
* CSS
* JavaScript 
  
  
## Known Bugs  
some slight issues with updating and search function
## Contact Information   
If you have any question or contributions, please email me at lanrakhaled@gmail.com
  
## License 

MIT <br>
Copyright © by Khalid Ali,Victor Lominyo ,Trevor Nyagah