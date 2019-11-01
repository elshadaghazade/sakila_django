from django.db import models
from employees_app.models import Employees

class Salaries(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.emp_no.emp_no} - {self.emp_no.first_name} {self.emp_no.last_name} | {self.salary} | {self.from_date} | {self.to_date}"

    class Meta:
        managed = False
        db_table = 'salaries'
        unique_together = (('emp_no', 'from_date'),)
        verbose_name = 'Salary'
        verbose_name_plural = 'Salaries'