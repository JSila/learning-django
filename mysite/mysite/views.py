from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime
from mysite.forms import ContactForm


def hello(request):
	return HttpResponse("Hello world!")


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'datetime': now}))
    # return HttpResponse(html)
    return render_to_response("current_datetime.html", dict(datetime=now))

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def display_browser(request):
    browser = request.META.get("HTTP_USER_AGENT", "unknown")
    return HttpResponse("Your browser is %s" % browser)

def display_meta(request):
    meta = request.META.items()
    return render_to_response("display_meta.html", dict(meta=meta))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET["q"]:
        message = 'You searched for: %s. What is this?' % request.GET['q']
    else:
        message = 'Y U NO SEARCH for sth??'
    return HttpResponse(message)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial='I love your site!'
        )
    return render_to_response('contact_form.html', {'form': form})