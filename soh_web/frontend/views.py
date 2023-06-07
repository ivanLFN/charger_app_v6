from django.shortcuts import render, get_object_or_404
from frontend.models import Partnership

def main_app(request):
    partners_list = Partnership.objects.all()
    data = {
        'partners_list': partners_list
    }
    return render(request, 'main_app.html', data)


def partner_detail(request, partner_title):
    partner = get_object_or_404(Partnership, title=partner_title)
    return render(request, 'general_elements/partner_detail.html', {'partner': partner})
