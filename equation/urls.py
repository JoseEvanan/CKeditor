""" URLs for Exam Application """
from django.conf.urls import url
from equation.views import *

app_name = 'equation'

urlpatterns = [
    url(r'^save/$', SaveEquation.as_view()),
    url(r'^data/$', AjaxSaveData.as_view()),
    url(r'^getdata/$', AjaxGetData.as_view()),
    url(r'^upload/$', AjaxUpload.as_view()),
    url(r'^browser/$', AjaxBrowser.as_view()),
]