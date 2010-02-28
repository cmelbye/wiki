from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from yourwiki.wiki.models import Page

def index(request):
	return HttpResponse("Hello World.")

def detail(request, slug_name=None):
	p = None
	if slug_name:
		p = get_object_or_404(Page, slug=slug_name)
	sections = p.section_set.order_by('position')
	return render_to_response('wiki/detail.html', {'page': p, 'sections': sections})
