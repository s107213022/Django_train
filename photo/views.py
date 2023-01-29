from django.shortcuts import render
from .models import Photo
#from .forms import PhotoForm # my write module
from django.views.generic import UpdateView,ListView,DetailView,CreateView
from django import forms
# Create your views here.

#def showtemplate(request):
 #   photo_list = Photo.objects.all() #take all data from photo table
 #   context = {'photo_list':photo_list} #build {} to match Photo table data(one to one)
 #   return render(request, 'photo\detail_all.html',context)

# build form(Add new photo) 
def photo_create_view(request):
    form = PhotoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PhotoForm() # clear form

    context = {
        'form' : form
    }
    return render(request, 'photo\photo_create.html',context)

# singlePhoto can't route to their own site(wait for fix) OK
#def singlePhoto(request,id):
 #   photo_list = Photo.objects.get(id=id)
 #   context = {'photo_list':photo_list} #build {} to match Photo table data(one to one)
 #   return render(request, 'photo\detail.html',context)

class PhotoListView(ListView): #OK
    model = Photo
    template_name = 'photo\photo_list.html'

class PhotoDetailView(DetailView): 
    model = Photo
    # queryset = Vendor.objects.all()
    template_name = 'photo\photo_detail.html'

class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoCreateView(CreateView):
    form_class = PhotoModelForm
    template_name = 'photo\photo_create.html'

# no finish
class PhotoUpdateView(UpdateView):
    form_class = PhotoModelForm
    template_name = 'photo\photo_create.html'
    queryset = Photo.objects.all() # 這很重要
