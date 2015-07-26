from django.shortcuts import render_to_response, get_object_or_404
from .forms import UploadFileForm

def home(request):
  context = {'name':'world'}
  return render_to_response('splitbill/index.html', context)
  
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
