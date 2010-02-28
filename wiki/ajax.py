from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from yourwiki.wiki.models import Section, SectionForm

def section_edit(request):
	section = get_object_or_404(Section, pk=request.GET['section_id'])
	
	if request.method == 'POST':
		print section
		form = SectionForm(request.POST, instance=section)
		if form.is_valid():
			cd = form.cleaned_data
			section.title = cd['title']
			section.text = cd['text']
			section.save()
			return render_to_response('wiki/section.html', {'section': section})
	else:
		form = SectionForm(instance=section)
		return render_to_response('wiki/section_edit_form.html', {'section_form': form})

def process_sections(request):
	sections = dict((y, x) for x,y in enumerate(request.GET.getlist('section[]')))
	for key, value in sections.items():
		section = Section.objects.get(pk=key)
		print section, value
		section.position = value
		section.save()
	
	return HttpResponse("Done! :D")

def show_section(request):
	section = get_object_or_404(Section, pk=request.GET['section_id'])
	return render_to_response('wiki/section.html', {'section': section})
