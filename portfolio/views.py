from django.shortcuts import render, get_object_or_404
from .models import Project,Report


# retorna un diccionario con todos los proyectos creados en admin
def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

def render_report(request):
    reports = Report.objects.all()
    return render(request,'report.html', {"reports": reports})

def report_detail(request,report_id):
    report = get_object_or_404(Report,pk=report_id)
    return render(request,'report_detail.html',{"report":report})
