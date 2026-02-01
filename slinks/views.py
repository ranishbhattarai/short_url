from os import link
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from slinks.forms import ShortLinkForm
from slinks.models import ShortLink
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'slinks/home.html')

@login_required
def dashboard(request):
    links = ShortLink.objects.filter(user=request.user)
    return render(request, 'slinks/dashboard.html', {'links': links})

@login_required
def create(request):
    if request.method == 'POST':
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            short_url = request.build_absolute_uri(f'{link.short_key}/')
            messages.success(request, f'Short URL: {short_url}')
            return redirect('slinks:dashboard')
    else:
        form = ShortLinkForm()
    return render(request, 'slinks/create.html', {'form': form})

def redirect_view(request, short_key):
    short_link = get_object_or_404(ShortLink, short_key=short_key)
    short_link.clicks += 1
    short_link.save(update_fields=['clicks'])
    return redirect(short_link.original_url)

@login_required
def edit(request, short_key):
    link = get_object_or_404(ShortLink, short_key=short_key, user=request.user)
    if request.method == 'POST':
        form = ShortLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated.')
            return redirect('slinks:dashboard')
    else:
        form = ShortLinkForm(instance=link)
    return render(request, 'slinks/edit.html', {'form': form, 'link': link})

@login_required
def delete(request, short_key):
    link = get_object_or_404(ShortLink, short_key=short_key, user=request.user)
    if request.method == 'POST':
        link.delete()
        messages.success(request, 'Deleted.')
        return redirect('slinks:dashboard')
    return render(request, 'slinks/delete.html', {'link': link})