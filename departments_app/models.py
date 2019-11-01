from django.db import models
from employees_app.models import Employees

class Departments(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    def __str__(self):
        return f"{self.dept_no} | {self.dept_name}"

    class Meta:
        managed = False
        db_table = 'departments'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class DeptManager(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.emp_no.emp_no} - {self.emp_no.first_name} {self.emp_no.last_name} | {self.dept_no.dept_no} - {self.dept_no.dept_name}"

    class Meta:
        managed = False
        db_table = 'dept_manager'
        unique_together = (('emp_no', 'dept_no'),)
        verbose_name = 'Department Manager'
        verbose_name_plural = 'Department Managers'

class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.emp_no.emp_no} - {self.emp_no.first_name} {self.emp_no.last_name} | {self.dept_no.dept_no} - {self.dept_no.dept_name} | {self.from_date} | {self.to_date}"

    class Meta:
        managed = False
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)
        verbose_name = 'Department Employee Relation'
        verbose_name_plural = 'Department employee Relations'
