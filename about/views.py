from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


def about_me(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

            
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )

def about_view(request):
    if request.method == 'POST':
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Collaboration request received! I endeavour to respond within 2 working days.")
            return redirect('about')  # Redirect to prevent re-submission on page refresh
    else:
        form = CollaborateForm()
    
    return render(request, 'about.html', {'form': form})    