# Create your views here.

from evmini.models import Election

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    return HttpResponse("Hello, world. You're at the evmini index.")
    
def elections(request):
	
	elections = Election.objects.all()
	
	# Assemble that shit
	template = loader.get_template('elections.html')
	
	context = RequestContext(request, { 'elections' : elections } )
	
	rendered_template = template.render(context)
	
	
	return HttpResponse(rendered_template)
	

