from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        ),
    car_name = models.CharField(max_length=30, primary_key=True)
    # ...
    SPORTS = 'SP'
    SUV = 'SUV'
    SEDAN = 'SD'
    TRUCKS = 'TR'
    STATIONWAGON = 'SW'
    car_menu = [
        ('SP', 'Sports'),
        ('SUV', 'SUV'),
        ('SD', "Sedan"),
        ('TR', "Trucks"),
        ('SW', "StationWagon"),
    ]

    car_drive = [
    ('前輪駆動','FF'),
    ('後輪駆動','FR'),
    ('4輪駆動','4WD'),
    ('ミッドシップ','MR'),
    ]


    car_name = models.CharField('車名',max_length=60, primary_key=True)
    car_menu = models.CharField('タイプ',max_length=3, choices=car_menu,)
    car_drive = models.CharField('駆動方式',max_length=6, choices=car_drive,)
    def __str__(self):
        return self.car_name



#class Entry(models.Model):
    #manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    #headline = models.CharField(max_length=255)
    #body_text = models.TextField()
    #pub_date = models.DateField()
    #mod_date = models.DateField()
    #authors = models.ManyToManyField(Car)
    #number_of_comments = models.IntegerField()
    #number_of_pingbacks = models.IntegerField()
    #rating = models.IntegerField()

    #def __str__(self):
        #return self.headline


INSTALLED_APPS = [

    'myapp',

    ]
