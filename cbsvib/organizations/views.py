from django.shortcuts import render


def organizations(request):
    main_data = {
        'title': 'Организации'
    }
    return render(request, 'organizations/organizations.html', main_data)
