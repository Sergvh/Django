# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'i': 1,
        'first_name': u'Максим',
        'last_name': u'Потапенко',
        'ticket': 235,
        'image': 'img / me.jpeg'},
        {'id': 2,
        'first_name': u'Олег',
        'last_name': u'Синюткін',
        'ticket': 2123,
        'image': 'img / piv.png'},
        {'id': 3,
         'first_name': u'Андрійко',
         'last_name': u'Задовий',
         'ticket': 5332,
         'image': 'img / piv.png'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups_list(request):
    return render(request, 'students/groups_list.html', {})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)