from django.shortcuts import render
from .models import VideoTutorial, Certificate, Project
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    '''video_list = VideoTutorial.objects.all().order_by('id')
    paginator = Paginator(video_list, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)'''
    videos = VideoTutorial.objects.all()

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    videos = VideoTutorial.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(youtube_link__icontains=q)
    )

    paginator = Paginator(videos, 6)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    certificate = Certificate.objects.all()
    projects = Project.objects.all()
    paginators = Paginator(certificate, 6)  # Show 25 contacts per page.
    page_numbers = request.GET.get('page')
    page_object = paginators.get_page(page_numbers)

    context ={'videos': videos, 'certificate':certificate, 'page_obj': page_obj, 'page_object':page_object,
              'projects':projects}
    return render(request, 'index.html', context)