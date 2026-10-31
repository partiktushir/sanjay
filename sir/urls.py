from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "gallery/",
        views.gallery,
        name="gallery"
    ),

    path(
        "result/",
        views.result,
        name="result"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "admission/",
        views.admission,
        name="admission"
    ),

    path(
        "admission/success/",
        views.admission_success,
        name="admission_success"
    ),
    path("facilities/",
    views.facilities,
    name="facilities"),

    path("academics/",
    views.academics,
    name="academics"),

    path("sports/", 
    views.sports,
    name="sports"),
]