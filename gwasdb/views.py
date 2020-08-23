from django.http                        import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts                   import get_object_or_404, render, redirect
from django.urls                        import reverse
from django.views.decorators.csrf       import csrf_exempt
from django.conf                        import settings
# from .forms                             import DataTrackForm
# from .runbash                           import ManageGiveData
# from .models                            import Track, Coordinates

import json
import re
import os
import glob


def find(request):
    return render(request,'gwasdb/find.html',{'title':'Find LD SNPs'})