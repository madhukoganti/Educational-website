from django.shortcuts import render,redirect
from app1.forms import StudentForm, ContactForm
from app1.models import Student, Contact


def homeview(request):
    return render(request, 'app1/home.html')


def aboutview(request):
    return render(request, 'app1/about.html')


def parentregview(request):
    f = StudentForm()

    if request.method == 'POST':
        f = StudentForm(request.POST)

        if f.is_valid():
            f.save()
        return redirect('/thanks')

    return render(request, 'app1/parent reg.html', {'forms': f})


def classesview(request):
    return render(request, 'app1/classes.html')


def galleryview(request):
    return render(request, 'app1/gallery.html')


def latestnewsview(request):
    return render(request, 'app1/latest news.html')


def contactview(request):
    f = ContactForm()

    if request.method == 'POST':
        f = ContactForm(request.POST)

        if f.is_valid():
            f.save()
        return redirect('/thanks')    
            

    return render(request, 'app1/contact.html', {'form': f})


def class8view(request):
    return render(request, 'app1/class8.html')


def class9view(request):
    return render(request, 'app1/class9.html')


def class10view(request):
    return render(request, 'app1/class10.html')


def parentview(request):
    return render(request, 'app1/parent reg.html')


def photosview(request):
    return render(request, 'app1/photos.html')


def videosview(request):
    return render(request, 'app1/videos.html')


def adminsview(request):
    parents = Student.objects.all()
    contacts = Contact.objects.all()

    return render(
        request,
        'app1/admins.html',
        {
            'parents': parents,
            'contacts': contacts
        }
    )
def thanksview(request):
    return render(request,'app1/thanks.html')