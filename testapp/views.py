from django.shortcuts import render
from .models import Rubric


def test(request):
    context = {
        'rubrics': Rubric.objects.all()
    }
    return render(request, template_name='testapp/test.html', context=context)


def get_rubric(request):
    pass
