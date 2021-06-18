from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from .models import view
from .models import look
from .models import studing
from .models import exp
from .models import achivment
from .models import course
from .models import one
from .models import onet
from .models import two
from .models import twot
from .models import three
from .models import threet
from .forms import CustomerForm
from django.views.decorators.csrf import csrf_exempt


backup_n = []
backup_m = []
backup_msg = []

def test(request):
    print(backup_n,backup_m,backup_msg)
    context = {
        "backup_n": backup_n,
        'backup_m': backup_n,
        'backup_msg': backup_msg,
    }
    return render(request, 'mainapp/test.html', context)


def firstpage(request):
    # view_list = view.objects.all()
    # context = {
    #   'view_list': view_list,
    # }
    return render(request, 'mainapp/firstpage.html')


@csrf_exempt
def intro(request):
    looks_list = look.objects.all()
    studing_list = studing.objects.all()
    exp_list = exp.objects.all()
    ach_list = achivment.objects.all()
    cou_list = course.objects.all()
    one_list = one.objects.all()
    two_list = two.objects.all()
    three_list = three.objects.all()

    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            backup_n.append(form.cleaned_data['Name'])
            backup_m.append(form.cleaned_data['Mail'])
            backup_msg.append(form.cleaned_data['Your_Message'])
            return HttpResponseRedirect("/intro/#contact")

    context = {
        'looks_list': looks_list,
        'studing_list': studing_list,
        'exp_list': exp_list,
        'cou_list': cou_list,
        'ach_list': ach_list,
        'one_list': one_list,
        'two_list': two_list,
        'three_list': three_list,
        'form': form
    }
    return render(request, 'mainapp/intro.html', context)


def project_one(request):
    one_list = one.objects.all()
    onet_list = onet.objects.all()
    context = {
        "c": 1,
        'one_list': one_list,
        'onet_list': onet_list,
    }
    return render(request, 'mainapp/project.html', context)


def project_two(request):
    two_list = two.objects.all()
    twot_list = twot.objects.all()
    context = {
        "c": 2,
        'two_list': two_list,
        'twot_list': twot_list,
    }
    return render(request, 'mainapp/project.html', context)


def project_three(request):
    three_list = three.objects.all()
    threet_list = threet.objects.all()
    context = {
        "c": 3,
        'three_list': three_list,
        'threet_list': threet_list,
    }
    return render(request, 'mainapp/project.html', context)
