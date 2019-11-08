from django.shortcuts import render
from .models import Employees
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Avg, Count, StdDev, Min, Max

def show_employees(request):
    search_by_full_name = request.GET.get('full_name')
    search_by_year = request.GET.get('b_year')
    search_by_month = request.GET.get('b_month')
    search_by_day = request.GET.get('b_day')
    search_by_gender = request.GET.get('gender')

    order_by = request.GET.get('order_by')

    current_page = request.GET.get('page', '')
    try:
        current_page = int(current_page) - 1
    except:
        current_page = 0

    limit = 100
    start = current_page * limit
    
    emps = Employees.objects.all().values('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date', 'titles__title', 'deptmanager__dept_no__dept_name', 'deptemp__dept_no__dept_name')
    # SELECT * FROM employees

    if search_by_full_name:
        search_by_full_name = search_by_full_name.split(" ")
        emps = emps.filter(Q(first_name__in=search_by_full_name) | Q(last_name__in=search_by_full_name))
        # SELECT * FROM employees WHERE first_name like '%asdas%' or last_name like '%asdas%'

    if search_by_year:
        emps = emps.filter(birth_date__year=search_by_year)

    if search_by_month:
        emps = emps.filter(birth_date__month=search_by_month)

    if search_by_day:
        emps = emps.filter(birth_date__day=search_by_day)
        

    if search_by_gender == "F" or search_by_gender == "M":
        emps = emps.filter(Q(gender=search_by_gender))
        # SELECT * FROM employees WHERE (first_name like '%asdas%' or last_name like '%asdas%') and birth_date = '1955-05-25' and gender = 'F'

    if order_by == 'emp_no_desc':
        emps = emps.order_by('-emp_no')
    elif order_by == 'emp_no_asc':
        emps = emps.order_by('emp_no')
    elif order_by == 'full_name_desc':
        emps = emps.order_by('-first_name', '-last_name')
    elif order_by == 'full_name_asc':
        emps = emps.order_by('first_name', 'last_name')
    elif order_by == 'b_date_desc':
        emps = emps.order_by('-birth_date')
    elif order_by == 'b_date_asc':
        emps = emps.order_by('birth_date')
    elif order_by == 'gender_desc':
        emps = emps.order_by('-gender')
    elif order_by == 'gender_asc':
        emps = emps.order_by('gender')
    elif order_by == 'hire_date_desc':
        emps = emps.order_by('-hire_date')
    elif order_by == 'hire_date_asc':
        emps = emps.order_by('hire_date')
    elif order_by == 'title_desc':
        emps = emps.order_by('-titles__title')
    elif order_by == 'title_asc':
        emps = emps.order_by('titles__title')
    elif order_by == 'dept_manager_desc':
        emps = emps.order_by('-deptmanager__dept_no__dept_name')
    elif order_by == 'dept_manager_asc':
        emps = emps.order_by('deptmanager__dept_no__dept_name')
    elif order_by == 'department_desc':
        emps = emps.order_by('-deptemp__dept_no__dept_name')
    elif order_by == 'department_asc':
        emps = emps.order_by('deptemp__dept_no__dept_name')

    page_count = (emps.count() // limit) + 1
    pages = range(1, page_count)

    return render(request, 'employees.html', context={
        'employees': emps[start:start+limit],
        'query_string': request.GET.urlencode(),
        'pages': pages
    })


def reports(request):
    field = request.GET.get('field')
    operator = request.GET.get('operator')
    value = request.GET.get('value')

    aggregate = request.GET.get('aggregate')
    agg_field = request.GET.get('agg_field')
    group_by = request.GET.get('group_by')

    context = {}

    emps = Employees.objects.all()

    fields = {
        '1': 'birth_date', 
        '2': 'hire_date', 
        '3': 'salaries__from_date', 
        '4': 'salaries__to_date'
    }

    field = fields.get(field)

    operators = ['gt', 'gte', 'lt', 'lte', 'exact']
    if operator not in operators:
        operator = None

    aggregates = {
        'count': Count,
        'avg': Avg,
        'stddev': StdDev,
        'min': Min,
        'max': Max
    }

    aggregate = aggregates.get(aggregate)

    agg_fields = {
        '1': 'emp_no',
        '2': 'salaries__salary'
    }

    agg_field = agg_fields.get(agg_field)

    groups = {
        '1': 'emp_no',
        '2': 'salaries__salary',
        '3': 'first_name',
        '4': 'birth_date',
        '5': 'gender',
        '6': 'hire_date',
        '7': 'titles__title',
        '8': 'deptmanager__dept_no__dept_name',
        '9': 'deptemp__dept_no__dept_name'
    }

    group_by = groups.get(group_by)

    if field and operator and value:
        lookup = {
            field + "__" + operator: value
        }

        emps = Employees.objects.filter(**lookup).values('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date', 'titles__title', 'deptmanager__dept_no__dept_name', 'deptemp__dept_no__dept_name')

        if not group_by:
            emps = emps.aggregate(aggregate(agg_field))
        else:
            emps = emps.annotate(agg_field=aggregate(agg_field))
            #.distinct('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date', 'titles__title', 'deptmanager__dept_no__dept_name', 'deptemp__dept_no__dept_name')
    else:
        emps = []

    print(emps)

    context = {
        'employees': emps,
        'template': ''
    }



    

    return render(request, "reports.html", context=context)