from django.db import models

# Create your models here.
from cng import settings

class Cngmodel(models.Model):
    license_no = models.CharField(max_length=50)
    report_no = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=50)
    test_date = models.DateField()
    test_due_date = models.DateField()
    vehicle_type = models.CharField(max_length=50)
    fuel_type =models.CharField(max_length=50)
    cylinder_no = models.CharField(max_length=50)
    cylinder_make = models.CharField(max_length=50)
    last_testing_date = models.DateField()
    manufacturing_date = models.DateField()
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    valve_inspection = models.CharField(max_length=50)
    visual_inspection = models.CharField(max_length=50)
    internal_inspection = models.CharField(max_length=50)
    plate_no = models.CharField(max_length=50)
    as_pr_making = models.FloatField()
    actual_wt = models.FloatField()
    wall_thick_min = models.FloatField()
    wall_thick_max = models.FloatField()
    vol_cap = models.FloatField()
    working_press = models.IntegerField()
    testing_press = models.IntegerField()
    total_expen = models.IntegerField()
    cylinder_threading = models.CharField(max_length=30)
    cylinder_spec = models.CharField(max_length=30)
    permanent_expen = models.FloatField()
    loss_wt = models.FloatField()
    diff_wt = models.FloatField()
    image = models.ImageField(null=True,blank=True)

    def __str(self):
        return self.vehicle_no

    