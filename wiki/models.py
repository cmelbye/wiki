from django.contrib import admin
from django.db import models
from django import forms

class Page(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title

class Section(models.Model):
	page = models.ForeignKey(Page, editable=False)
	title = models.CharField(max_length=200)
	text = models.TextField()
	position = models.IntegerField(default=0, editable=False)
	created = models.DateTimeField(auto_now_add=True, editable=False)
	modified = models.DateTimeField(auto_now=True, editable=False)
	
	def __unicode__(self):
		return self.title

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
	
	def __init__(self, *args, **kwargs):
		super(SectionForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['class'] = "title"

class SectionInline(admin.StackedInline):
	model = Section
	extra = 1

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'slug']
	list_display = ['title']
	search_fields = ['title']
	date_hierarchy = 'created'
	prepopulated_fields = {"slug": ("title",)}
	inlines = [SectionInline]

admin.site.register(Page, PageAdmin)
