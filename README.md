####
# DjangoDataViz - Final Project P.4
####
- What's your project?



   ... My project is to use Django to create a database which will display and organize data.

- What is your first major milestone?




  ... My first major milestone is to set up the database.

- What do you not know that you will need to learn?





    ... I will need to learn how to change the settings for each of the components of a database.

- In what ways is your project too ambitious?





  ... It may be too ambitious since I want to display the data in too many ways.

- In what ways is it possibly not ambitious enough?






   ... I think it is ambitious enough.

# Sources:
### Borrowing Main Code From This Amazing Tutorial:
[Main Source Code Github Link](https://github.com/codingforentrepreneurs/Django-Chart.js)

--------------------------
### Other:
--------------------------
- [Django Project Tutorial pt.1](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)

--------------------------
- [Django Project Tutorial pt.2](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)

--------------------------
- [Django Project Tutorial pt.3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)

--------------------------
- [Django Project Tutorial pt.4](https://docs.djangoproject.com/en/2.0/intro/tutorial04/)

--------------------------
- [Django Project Tutorial pt.5](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)

--------------------------
- [Reading/Writing .txt files w/ python](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)

--------------------------
- [Tensorflow Tutorial/Setup](https://www.tensorflow.org/get_started/get_started_for_beginners)

--------------------------
- #### Python Crash Course
--------------------------
### Break Progress:
- I completed initial setup after major setbacks since I did not add /polls/ (the app) in the URL which wasted a lot of time
- I have read through the steps provided by the Python Crash Course to see how to add user sign and enabling public access to the site using Heroku and multiple libraries which provides basic services but is free
- I am also working on the templates for the page which uses HTML
- I also read through the steps to style the page using the django-bootstrap3 app which can be used under myproject (name for main project file) since it is an app
- I also found ways to display graphs with django through GitHub which has many apps to do this using django apps and JavaScript: Django Graphos Django Uncharted Django Chartkit but I am still working out how to implement these
#### Project Progress from Spring Break
```shell
I am using this code to take advantage of the django interactive python shell to understand Database searches and filters using id's and also to verify that my code is working
>>> from polls.models import Question, Choice

Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

 Django provides a rich database lookup API that's entirely driven by
 keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

 Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

 Lookup by a primary key is the most common case, so Django provides a
 shortcut for primary-key exact lookups.
 The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

 Give the Question a couple of Choices. The create call constructs a new
 Choice object, does the INSERT statement, adds the choice to the set
 of available choices and returns the new Choice object. Django creates
 a set to hold the "other side" of a ForeignKey relation
 (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

 Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

 Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

 Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

 The API automatically follows relationships as far as you need.
Use double underscores to separate relationships.
 This works as many levels deep as you want; there's no limit.
 Find all Choices for any question whose pub_date is in this year
 (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

 Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```



### Code From:
[Django Project Tutorial pt.5](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)
- This is an example of the tests used to verify if the app is working

```python
#This is located in the the tests.py file under the polls app under the main project which I named myproject

import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question

class QuestionModelTests(TestCase):
  def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```       
- After inputting this into tests.py I ran the test by going to command prompt, activating my virtual environment, and
typing: cd finalProject which goes into my main folder where the main django project is located.
Then I typed: python manage.py test polls which give me all the errors which makes it a useful debugger


### Week 12:
- I worked on getting GitHub working and got the majority of my files uploaded using git commands with bash, but ran into
a problem with updating my files so my old files are on GitHub.
https://github.com/ajojothepineapple (Repository is Data-Visualization-Using-Django)
- I finished the polls tutorial on the django's website in order to gain a better understanding of django the main takeaway was debugging and automated testing in django
- The apps I previously found on GitHub are not working so am I am now working on using django-dashing which is a framework that can visualize data using javascript I will be using:
https://github.com/talpor/django-dashing/
- At the same time, I am looking into using chart.js instead because it may be better for my purpose. I found a very informative tutorial on youtube which teaches how to incorporate chart.js w/ django and use bootstrap for styling
https://www.youtube.com/watch?v=B4Vmm3yZPgc

### Week 13: Could only attend one class meeting so less work than previous turn-ins
- Able to find a suitable app that provides clean Data Visualization
- Learned how to use GitHub properly
- Found better Text Editor (Sublime Text 3 Community Edition)
- Learned more about how to navigate through Command Prompt and Bash

### Week 14:
- Switched to Atom (better text editor and has better built-in GitHub control because developed by GitHub)
- I also used postman to perform automated tests on the local host 8000 port. (I am still trying to figure out what the many tests that I can perform)
- Found a way to read .txt files using python : [Reading/Writing .txt files w/ python](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
- Still trying to fix:
```
  return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 941, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'None'
```

### Week 15:
- Front end completed except for extra styling if time permits (Majority of front end from tutorial)
- #### **Fixed MAJOR Error** ```no module error``` **by doing:**```pip install djangorestframework```
- Ran into major errors with Heroku but after a lot of experimentation stack overflow posts found I needed to install Heroku CLI which allows me to deploy apps w/ CP
-  After typing ```heroku local``` the error ``` ``ModuleNotFoundError: No module named 'fcntl'```(in package gunicorn) came up. Has something to do with conflicting packages because I tested this suspicion w/                 
 ```shell
(datav) C:\Users\Ajosh.Antony20\DjangoDataViz\FrontEnd\src>pip install gunicorn
Requirement already satisfied: gunicorn in c:\users\ajosh.antony20\appdata\local\continuum\anaconda3\lib\site-packages (19.8.1)
pandas 0.22.0 has requirement python-dateutil>=2, but you'll have python-dateutil 1.5 which is incompatible.
matplotlib 2.2.2 has requirement python-dateutil>=2.1, but you'll have python-dateutil 1.5 which is incompatible.
jupyter-client 5.2.3 has requirement python-dateutil>=2.1, but you'll have python-dateutil 1.5 which is incompatible.
bokeh 0.12.14 has requirement python-dateutil>=2.1, but you'll have python-dateutil 1.5 which is incompatible.
anaconda-client 1.6.14 has requirement python-dateutil>=2.6.1, but you'll have python-dateutil 1.5 which is incompatible.
```



Will try to make a new venv and uninstall conflicting packages and uninstall and reinstall gunicorn
- Found usable Data Set
- Used tutorial and prior knowledge to create reading/writing python program
- May use Eve to connect the python output and front end

--------------------
