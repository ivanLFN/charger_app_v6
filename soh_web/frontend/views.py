from django.shortcuts import render, get_object_or_404
from frontend.models import Partnership, Image

def main_app(request):
    partners_list = Partnership.objects.all()
    available_images = Image.objects.filter(type_img='gallary_type')
    data = {
        'partners_list': partners_list,
        'available_images': available_images
    }
    return render(request, 'main_app.html', data)


def partner_detail(request, partner_title):
    partner = get_object_or_404(Partnership, title=partner_title)
    segments_of_work = list(partner.segmets_of_work.all())

    tabs = []
    for segment in segments_of_work:
        tab = {
            'id': f'tab{segment.pk}',
            'title': segment.title,
            'content': segment.about,
            'image': segment.image,
            'active': False, 
        }
        tabs.append(tab)

    if tabs:
        tabs[0]['active'] = True

    return render(request, 'general_elements/partner_detail.html', {'partner': partner, 'tabs': tabs})

    




