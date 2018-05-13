####
# DjangoDataViz - Final Project P.4
####

*********************
## LIVE Link To Project: https://ajosh-django-dataviz.herokuapp.com/
*********************


# Sources:
### Borrowing Main Code From This Amazing Tutorial:
[Main Source Code Github Link](https://github.com/codingforentrepreneurs/Django-Chart.js)

--------------------------
#### Other:
-------------------------
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
- [Heroku Django Deployment](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)

--------------------------
- [Live Data Source](https://www.satori.com/docs/rtm-sdks/tutorials/python-sdk-quickstart)

--------------------------
- [Static Data Source (.txt)](https://catalog.data.gov/dataset/us-nuclear-power-reactor-plant-status)

--------------------------
- [W3 Schools](https://www.w3schools.com/bootstrap4/default.asp)

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
- Had to delete former repository and import to a new repositiry so a good chunk of commit messages were lost
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
- Changing the venv's did not work had to uninstall other conflicting packages and add requirements.txt, Procfile, and runtime.txt. This is outlined in [this](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html) useful tutorial.
- Found usable Data Set
- Used tutorial and prior knowledge to create reading/writing python program
- May use Eve to connect the python output and front end
- Attempting to use live data instead of static .txt file



### Week 16 (Final Week)
- Finished Front End Setup
- Added modules and data organization w/ inside convert.py organized data stored in organizedData.txt
- Now I need to somehow input the organized data into the data variable inside templates/charts.html using eve which may work locally but not when it is published
- I also need to add the corresponding label with each data point (the powerplant name) inside the label variable labels in charts/views.py 
- Using Satori I subscibed to the USGS live earthquake data feed and inputed the app key and other required variables to get the follwing live data:
```shell
C:\Users\Ajosh.Antony20\DjangoDataViz\Satori-live>python testing.py
Connected to Satori RTM!
Got message: {'geometry': {'coordinates': [-163.5518, 65.7668, 40], 'type': 'Point'}, 'id': 'ak19479040', 'type': 'Feature', 'properties': {'dmin': None, 'code': '19479040', 'sources': ',ak,', 'tz': -540, 'mmi': None, 'type': 'earthquake', 'title': 'M 2.0 - 126km ESE of Shishmaref, Alaska', 'magType': 'ml', 'nst': None, 'sig': 62, 'tsunami': 0, 'mag': 2, 'alert': None, 'gap': None, 'rms': 0.8, 'place': '126km ESE of Shishmaref, Alaska', 'net': 'ak', 'types': ',geoserve,origin,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak19479040', 'ids': ',ak19479040,', 'time': 1526184117716, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak19479040.geojson', 'updated': 1526184478859, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-148.1975, 63.4651, 1.5], 'type': 'Point'}, 'id': 'ak19479038', 'type': 'Feature', 'properties': {'dmin': None, 'code': '19479038', 'sources': ',ak,', 'tz': -540, 'mmi': None, 'type': 'earthquake', 'title': 'M 1.2 - 38km ENE of Cantwell, Alaska', 'magType': 'ml', 'nst': None, 'sig': 22, 'tsunami': 0, 'mag': 1.2, 'alert': None, 'gap': None, 'rms': 0.32, 'place': '38km ENE of Cantwell, Alaska', 'net': 'ak', 'types': ',geoserve,origin,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak19479038', 'ids': ',ak19479038,', 'time': 1526183714828, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak19479038.geojson', 'updated': 1526183896947, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-155.1356659, 19.3199997, 4.8], 'type': 'Point'}, 'id': 'hv70151707', 'type': 'Feature', 'properties': {'dmin': 0.03452, 'code': '70151707', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 1.9 - 16km SE of Volcano, Hawaii', 'magType': 'md', 'nst': 17, 'sig': 58, 'tsunami': 0, 'mag': 1.94, 'alert': None, 'gap': 135, 'rms': 0.14, 'place': '16km SE of Volcano, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151707', 'ids': ',hv70151707,', 'time': 1526183595310, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151707.geojson', 'updated': 1526183797710, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-154.918335, 19.4543343, 3.03], 'type': 'Point'}, 'id': 'hv70151682', 'type': 'Feature', 'properties': {'dmin': 0.00139, 'code': '70151682', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 1.8 - 1km S of Leilani Estates, Hawaii', 'magType': 'md', 'nst': 7, 'sig': 48, 'tsunami': 0, 'mag': 1.76, 'alert': None, 'gap': 181, 'rms': 0.15, 'place': '1km S of Leilani Estates, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151682', 'ids': ',hv70151682,', 'time': 1526183077290, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151682.geojson', 'updated': 1526183252480, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-155.2856598, 19.4168339, 0.58], 'type': 'Point'}, 'id': 'hv70151672', 'type': 'Feature', 'properties': {'dmin': 0.001689, 'code': '70151672', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 2.1 - 5km WSW of Volcano, Hawaii', 'magType': 'md', 'nst': 13, 'sig': 65, 'tsunami': 0, 'mag': 2.06, 'alert': None, 'gap': 100, 'rms': 0.11, 'place': '5km WSW of Volcano, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151672', 'ids': ',hv70151672,', 'time': 1526182808100, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151672.geojson', 'updated': 1526182979510, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-155.2380066, 19.3544998, 0.3], 'type': 'Point'}, 'id': 'hv70151667', 'type': 'Feature', 'properties': {'dmin': 0.01913, 'code': '70151667', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 2.2 - 8km S of Volcano, Hawaii', 'magType': 'md', 'nst': 30, 'sig': 72, 'tsunami': 0, 'mag': 2.16, 'alert': None, 'gap': 57, 'rms': 0.17, 'place': '8km S of Volcano, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151667', 'ids': ',hv70151667,', 'time': 1526182766080, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151667.geojson', 'updated': 1526182960830, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-143.0023, 60.2976, 0], 'type': 'Point'}, 'id': 'ak19479037', 'type': 'Feature', 'properties': {'dmin': None, 'code': '19479037', 'sources': ',ak,', 'tz': -540, 'mmi': None, 'type': 'earthquake', 'title': 'M 1.3 - 40km NW of Cape Yakataga, Alaska', 'magType': 'ml', 'nst': None, 'sig': 26, 'tsunami': 0, 'mag': 1.3, 'alert': None, 'gap': None, 'rms': 0.47, 'place': '40km NW of Cape Yakataga, Alaska', 'net': 'ak', 'types': ',geoserve,origin,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak19479037', 'ids': ',ak19479037,', 'time': 1526182513985, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak19479037.geojson', 'updated': 1526182683502, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-155.2541656, 19.439333, 0.49], 'type': 'Point'}, 'id': 'hv70151652', 'type': 'Feature', 'properties': {'dmin': 0.01743, 'code': '70151652', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 2.3 - 1km WNW of Volcano, Hawaii', 'magType': 'md', 'nst': 10, 'sig': 80, 'tsunami': 0, 'mag': 2.28, 'alert': None, 'gap': 169, 'rms': 0.13, 'place': '1km WNW of Volcano, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151652', 'ids': ',hv70151652,', 'time': 1526182052040, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151652.geojson', 'updated': 1526182231480, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-116.7926667, 33.5008333, 6.03], 'type': 'Point'}, 'id': 'ci38171880', 'type': 'Feature', 'properties': {'dmin': 0.07928, 'code': '38171880', 'sources': ',ci,', 'tz': -480, 'mmi': None, 'type': 'earthquake', 'title': 'M 1.1 - 9km NE of Aguanga, CA', 'magType': 'ml', 'nst': 45, 'sig': 17, 'tsunami': 0, 'mag': 1.06, 'alert': None, 'gap': 33, 'rms': 0.17, 'place': '9km NE of Aguanga, CA', 'net': 'ci', 'types': ',geoserve,nearby-cities,origin,phase-data,scitech-link,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ci38171880', 'ids': ',ci38171880,', 'time': 1526181774210, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci38171880.geojson', 'updated': 1526181999799, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-155.2850037, 19.4099998, -0.07], 'type': 'Point'}, 'id': 'hv70151642', 'type': 'Feature', 'properties': {'dmin': 0.00767, 'code': '70151642', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 1.7 - 5km WSW of Volcano, Hawaii', 'magType': 'md', 'nst': 16, 'sig': 44, 'tsunami': 0, 'mag': 1.7, 'alert': None, 'gap': 120, 'rms': 0.23, 'place': '5km WSW of Volcano, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151642', 'ids': ',hv70151642,', 'time': 1526181579080, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151642.geojson', 'updated': 1526181755430, 'status': 'automatic'}}
Got message: {'geometry': {'coordinates': [-119.7308, 39.4008, 6.4], 'type': 'Point'}, 'id': 'nn00634779', 'type': 'Feature', 'properties': {'dmin': 0.029, 'code': '00634779', 'sources': ',nn,', 'tz': -480, 'mmi': None, 'type': 'earthquake', 'title': 'M 0.8 - 12km NW of Virginia City, Nevada', 'magType': 'ml', 'nst': 14, 'sig': 10, 'tsunami': 0, 'mag': 0.8, 'alert': None, 'gap': 96.84, 'rms': 0.2038, 'place': '12km NW of Virginia City, Nevada', 'net': 'nn', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nn00634779', 'ids': ',nn00634779,', 'time': 1526180978443, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nn00634779.geojson', 'updated': 1526181714754, 'status': 'reviewed'}}
Got message: {'geometry': {'coordinates': [-154.8246613, 19.4416676, -0.14], 'type': 'Point'}, 'id': 'hv70151617', 'type': 'Feature', 'properties': {'dmin': 0.03403, 'code': '70151617', 'sources': ',hv,', 'tz': -600, 'mmi': None, 'type': 'earthquake', 'title': 'M 3.4 - 10km ESE of Leilani Estates, Hawaii', 'magType': 'ml', 'nst': 21, 'sig': 177, 'tsunami': 0, 'mag': 3.39, 'alert': None, 'gap': 256, 'rms': 0.34, 'place': '10km ESE of Leilani Estates, Hawaii', 'net': 'hv', 'types': ',geoserve,origin,phase-data,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/hv70151617', 'ids': ',hv70151617,', 'time': 1526180928460, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv70151617.geojson', 'updated': 1526181263370, 'status': 'automatic'}}

```


--------------------
