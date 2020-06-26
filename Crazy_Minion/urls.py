from django.urls import path
from Crazy_Minion import views

app_name = "Crazy_Minion"
urlpatterns = [
    path('', views.home, name="home"),
    path('tutorials', views.tutorials, name="tutorials"),
    path('about_us', views.about_us, name="about_us"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('gettous', views.get_to_us, name="get_to_us"),
    path('tutorial', views.tutorial_post, name="tutorial_post"),

]
