<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Zaawansowane Django &ndash; Snippety
> Krótkie kawałki kodu, które pokazują zależności, rozwiązują popularne problemy oraz pokazują jak używać niektórych funkcji.


#### 1. Pizza and Toppings models
```python
class Toppings(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()

    
class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Toppings)
```

#### 2. Band model
```python
GENRE_TYPES = (
    (-1, "not defined"),
    (0, "rock"),
    (1, "metal"),
    (2, "pop"),
    (3, "hip-hop"),
    (4, "electronic"),
    (5, "reggae"),
    (6, "other")
)


class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genere = models.IntegerField(choices=GENRE_TYPES, default=-1)

```

#### 3. Article model
```python
WRITING_STATUS = (
    (1, "w trakcie pisania"),
    (2, "czeka na akceptację redaktora"),
    (3, "opublikowany")
)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=WRITING_STATUS, default=1)
    start_emission = models.DateField(null=True)
    stop_emission = models.DateField(null=True)
    category = models.ManyToManyField(Category)
	
    def __str__(self):
    	return"{}, {}".format(self.title, self.author) 
```

#### 3. Album model, view and template

* models.py
```python
class Album(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    rating = models.IntegerField()
    band = models.ForeignKey(Band)

    def __str__(self):
	return "{} {}".format(self.title, self.year)
```


* views.py
```python
from django.views.generic.list import ListView
from .models import Album

class AlbumListView(ListView):
	
    model = Album
```


* album_list.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% for album in object_list %}
        <li>{{album}}</li>
    {% endfor %}
</body>
</html>
```
