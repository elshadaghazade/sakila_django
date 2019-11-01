from django.db import models

class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()


    def __str__(self):
        return f"{self.emp_no} | {self.first_name} {self.last_name} | {self.gender} | {self.hire_date} | {self.birth_date}"

    class Meta:
        managed = False
        db_table = 'employees'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

class Titles(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.emp_no.emp_no} - {self.emp_no.first_name} {self.emp_no.last_name} | {self.title} | {self.from_date} | {self.to_date}"

    class Meta:
        managed = False
        db_table = 'titles'
        unique_together = (('emp_no', 'title', 'from_date'),)
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
