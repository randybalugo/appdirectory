from django.views.generic.list import ListView
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404

from models import Application

class BaseAppListView(ListView):
    """ Base view for application lists on the main page. """
    
    template_name = "index.html"
    paginate_by = settings.RESULTS_PAGE_LENGTH
    context_object_name = 'applications'
    
    
class DeviceAppListView(BaseAppListView):
    def get_context_data(self, **kwargs):
        
        context =  super(DeviceAppListView, self).get_context_data(**kwargs)
        context['device'] = self.kwargs['device']
        return context
    
    def get_queryset(self):
        
        device = self.kwargs['device']
        
        return Application.objects.apps_by_device(device)

class SearchAppListView(BaseAppListView):
    def get_queryset(self):
        keywords = self.request.GET.get("keyword", "")
        
        return Application.objects.filter(Q(title__search=keywords) | 
                                          Q(description__search=keywords)).distinct()

class CategoryAppListView(BaseAppListView):
    
    def get_context_data(self, **kwargs):
        
        context =  super(CategoryAppListView, self).get_context_data(**kwargs)
        context['selected_category'] = self.kwargs['category']
        return context
    
    def get_queryset(self):
        category = self.kwargs['category']
        return Application.objects.apps_by_category(category)

class ArtistAppListView(BaseAppListView):
    
    def get_queryset(self):
        artist_name = self.kwargs['artist_name']
        return Application.objects.filter(artist_name=artist_name)

#FIXME make class based
def detail(request, id):
    application = get_object_or_404(Application, application_id=id)
    view_data = dict(app=application, selected_category=application.get_category())
    return render_to_response("app_detail.html", view_data)
