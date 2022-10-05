from django.urls import path
from . import views
from .views import GeneratePDF

urlpatterns = [
    path('resumefill/', views.resumeFill, name='resume_fill'),
    path('resumeview/', views.resumeView, name='resume_view'),
    path('pdfgen/', GeneratePDF.as_view(), name='gen'),#honest is the key to unlock 
    path('resume_fill/', views.resumefill, name='resumefill'),
    path('resume_view/', views.resumeview, name='resumeview'),
    path('pdf_gen/', GeneratePDF.as_view(), name='gen1'),


]