from django.http                        import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts                   import get_object_or_404, render, redirect
from django.urls                        import reverse
from django.views.decorators.csrf       import csrf_exempt
from django.conf                        import settings
from .forms                             import *
# from .runbash                           import ManageGiveData
from .models                            import *

import json
import re
import os
import glob


def find(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LargeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'gwasdb/find.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        
        form1 = LargeForm()
        form2 = ChrSNPForm()
        form3 = UploadSNPs()
        

    context = {
        'title':'Find LD SNPs', 
        'form1': form1,
        'form2': form2,
        'form3': form3,
    }
    return render(request, 'gwasdb/find.html', context)