from django.shortcuts import  render_to_response
from Joshua import settings


# Create your views here.

def home(request):
    #go ahead pass setting context to template
    supportedLangs=settings.JOSHUA_WEB_API_SUPPORT_LANGUAGES.split()
    context = {'JOSHUA_WEB_API_URL': settings.JOSHUA_WEB_API_URL, 
               'JOSHUA_WEB_API_SUPPORT_LANGUAGES': supportedLangs}
    
    return render_to_response( 'home.html', context)
    # return render(request, 'home.html')