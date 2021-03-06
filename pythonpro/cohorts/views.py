from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rolepermissions.checkers import has_permission

from pythonpro.cohorts import facade
from pythonpro.core.roles import access_cohorts
from pythonpro.mailchimp.facade import tag_as


@login_required
def detail(request, slug):
    return render(request, 'cohorts/cohort_detail.html', {'cohort': facade.find_cohort(slug=slug)})


@login_required
def webinars(request):
    return render(request, 'cohorts/webinars.html', {'webinars': facade.find_webinars()})


@login_required
def webinar(request, slug):
    if not has_permission(request.user, access_cohorts):
        tag_as(request.user.email, 'potencial-member')
        return render(request, 'cohorts/webinar_landing_page.html')
    return render(request, 'cohorts/webinar_detail.html', {'webinar': facade.find_webinar(slug=slug)})


@login_required
def live_class(request, pk):
    if not has_permission(request.user, access_cohorts):
        tag_as(request.user.email, 'potencial-member')
        return render(request, 'cohorts/live_class_landing_page.html')
    return render(request, 'cohorts/live_class_detail.html', {'live_class': facade.find_live_class(pk=pk)})
