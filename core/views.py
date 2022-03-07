from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Scholarship, Type

def BootstrapFilterView(request):
    qs = Scholarship.objects.all()
    types = Type.objects.all()
    name_contains_query = request.GET.get('name_contains')
    name_exact_query = request.GET.get('name_exact')
    name_or_organization_query = request.GET.get('name_or_organization')
    type = request.GET.get('type_name')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    if name_contains_query != '' and name_contains_query is not None:
        qs = qs.filter(title__icontains = name_contains_query)

    if name_exact_query!= '' and name_exact_query is not None: 
            qs = qs.filter(title__iexact = name_exact_query)

    if name_or_organization_query!= '' and name_or_organization_query is not None: 
            qs = qs.filter(Q(title__icontains = name_or_organization_query) | Q(organization__name__icontains = name_or_organization_query)).distinct()

    if type!= '' and type is not None and type != 'Choose...': 
        qs = qs.filter(type__name = type)

    if reviewed == 'on':
        qs = qs.filter(reviewed = True)
    
    elif not_reviewed == 'on':
        qs = qs.filter(reviewed = False)

    context = {
        'queryset': qs,
        'types': types
    }

    return render(request, "bootstrap_form.html", context)