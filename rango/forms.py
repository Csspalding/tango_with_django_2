from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Please enter the category name.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  slug = forms.CharField(widget=forms.HiddenInput(), required=False)
  
  
  #visible fields displayed to user
  class Meta:
    #provides link from modelForm to a model
    model = Category
    #includes this field from Category in rango/models.py
    fields = ('name',)

class PageForm(forms.ModelForm):
  title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
  url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

  #visible fields displayed to user  
  class Meta:
    model = Page
    exclude = ('category',)


#override ModelForm clean() HANDY FOR PARTICULAR FORMS FIELDS HAVE TO HAVE DEFAULT VALUES, OR DATA FROM A FORM IS MISSING, IT NEEDS TO BE HANDLEDED
  def clean(self):
    cleaned_data = self.cleaned_data
    url = cleaned_data.get('url')#get() will return None if user enters nothing as new form will not exist

    #TODO ALSO CONSIDER HANDLING SECURE https:// too!
    #if the url is not empty and doesn't start with 'http://' then prepend 'http://'
    if url and not url.startswith('http://'):
      url = 'http://'+ url
      cleaned_data['url'] = url
      #always end clean() by returning a reference to the cleaned_data dictionary
      return cleaned_data

