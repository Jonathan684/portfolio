from django.urls import path
from .views import render_report,home,report_detail

app_name = "report"

urlpatterns = [
   path("",home,name="home"),
   path("report/",render_report,name="report"),
   path("<int:report_id>",report_detail,name="report_detail"),
   #path("<int:report_id>",report_detail),
]