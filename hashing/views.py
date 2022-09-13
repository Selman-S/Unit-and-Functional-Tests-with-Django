from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib

def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                # If this object already exists, no need to save it again
                Hash.objects.get(hash=text_hash)
            # If there is no object for the text, need to create an object:
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash', hash=text_hash)
        
    form = HashForm()
    context = {
        'form': form
    }
    return render(request, 'hashing/home.html', context)

def hash(request, hash):
    hash = Hash.objects.get(hash=hash)
    return render(request, 'hashing/hash.html', {'hash':hash})