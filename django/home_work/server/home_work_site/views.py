from django.shortcuts import render


def main_page(request):
    return render(request, 'home_work/index.html', {})


def catalog(request):
    return render(request, 'home_work/catalog.html', {})


def contacts(request):
    return render(request, 'home_work/contacts.html', {})


def adidas_performance(request):
    return render(request, 'home_work/pages_with_boots/Adidas_performance.html', {})


def asics_gel_pulse(request):
    return render(request, 'home_work/pages_with_boots/Asics_Gel_Pulse_9.html', {})


def asics_gel_solution_speed(request):
    return render(request, 'home_work/pages_with_boots/asics_gel_solution_speed.html', {})


def nike_flex_contact(request):
    return render(request, 'home_work/pages_with_boots/Nike_Flex_Contact.html', {})
