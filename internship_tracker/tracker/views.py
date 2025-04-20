from django.shortcuts import render, redirect  # Added redirect import
from django.db.models import Q  # Added Q import for query filtering
from .forms import InternshipForm  # Ensure your form is defined
from .models import Internship  # Ensure your Internship model is defined
from rest_framework import generics
from .serializers import InternshipSerializer  # Ensure InternshipSerializer is defined
from .serializers import InternshipSerializer


# Home page view
def home(request):
    return render(request, 'home.html')

# View to submit internship
def submit_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record')  
    else:
        form = InternshipForm()
    return render(request, 'submit.html', {'form': form})

# View to display internship records
def internship_records(request):
    query = request.GET.get('q')  # Retrieve query from GET request
    if query:
        internships = Internship.objects.filter(
            Q(student_name__icontains=query) |  
            Q(department__icontains=query) |  
            Q(company__icontains=query) | 
            Q(roll_no__icontains=query) | 
            Q(role__icontains=query)
        )
    else:
        internships = Internship.objects.all()  # Show all internships if no query
    return render(request, 'record.html', {'internships': internships})

# API view to list and create internships
class InternshipListCreateAPI(generics.ListCreateAPIView):
    queryset = Internship.objects.all()  # Use Internship model to fetch data
    serializer_class = InternshipSerializer  # Serialize the Internship data
