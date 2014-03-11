from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.template import loader, Context
from django.template.loader import get_template
from sell.models import Rules, MyUser

__author__ = 'kevin'


def home(request):
    t = get_template('index.html')
    c = Context({

    })

    html = t.render(c)
    return HttpResponse(html)

@permission_required("sell.view_task", login_url='/')
def view(request):
    t = get_template('views/view.html')
    c = Context({

    })

    html = t.render(c)
    return HttpResponse(html)

@login_required
def admin(request):
    user = request.user

    t = get_template('admin/admin.html')
    c = Context({

    })

    html = t.render(c)
    return HttpResponse(html)