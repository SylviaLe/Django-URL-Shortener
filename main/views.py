from django.shortcuts import redirect, render
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def createUrl(request):
    if request.method == 'POST':
        url = request.POST['link']  #get the link from POST ajax
        uid = str(uuid.uuid4())[:5]
        #Mental note: don't set a var name similar to a library or a function name
        new_url = Url(link=url, uuid=uid)
        new_url.save()

        return HttpResponse(uid)
        #At this point it should save to the database
        #Go to the page, enter an url, click submit. 
        #Come back to admin view, see the Url database. It should add a new one there

#dont do a class here since nothing really need to inherit from    
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)  #look in Url for an url that has the uuid = pk specified. If yes, then redirect to that original link
    return redirect(url_details.link)