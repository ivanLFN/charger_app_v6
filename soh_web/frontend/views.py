from django.shortcuts import redirect, render, get_object_or_404
from frontend.models import Partnership, Image, Product
from frontend.forms import OrderOrQuestionForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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


def store(request):
    product_list = Product.objects.filter(dev='False')
    product_dev_list = Product.objects.filter(dev='True')
    data = {
        'product_list': product_list,
        'product_dev_list': product_dev_list
    }
    return render(request, 'store/store.html', data)


def product_detail(request, product_title):
    product = Product.objects.get(title=product_title)
    return render(request, 'store/product_detail.html', {'product': product})



def personal_data(request):
    return render(request, 'general_elements/personal_data.html', {})


def create_order_or_question(request):
    if request.method == 'POST':
        form = OrderOrQuestionForm(request.POST)
        if form.is_valid():


            
            

            form.save()

            context = form.data

            html_message = render_to_string('general_elements/email_template.html', context)

            plain_message = strip_tags(html_message)

            send_mail('Отправитель', plain_message, 'LFN.current@yandex.com', ['LFN.current@yandex.com'])

            return redirect('success_send')
    else:
        form = OrderOrQuestionForm()
    
    return render(request, 'general_elements/form_template.html', {'form': form})


def success_send(request):
    return render(request, 'general_elements/success_send.html', {})


def partnership_page(request):
    partners_list = Partnership.objects.all()
    return render(request, 'general_elements/partnership_page.html', {'partners_list': partners_list})


def contacts(request):
    return render(request, 'general_elements/contacts.html', {})

