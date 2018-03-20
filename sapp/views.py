from django.shortcuts import render
from .models import user
import schedule
import urllib.request
import urllib.parse
import datetime
import pytz
# Create your views here.
def main(request):
	if request.method == 'POST':
		myuser = user.objects.all().first()
		continent = request.POST['continent'].title()
		country = request.POST['country'].title()
		myuser.name = continent+'/'+country
		myuser.contact = request.POST['number']
		myuser.save()
		return render(request,'index.html',{'msg':'Successful!'})
	return render(request,'index.html',{'msg':''})

def sendSMS(apikey, numbers, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message,})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

users = user.objects.all().first()
def my_job():
	resp =  sendSMS('Esp0XGYVec0-s0BnsJ6KhNJcBFeaU57YO0UkzDafhz', users.contact, 'Your name is John!')
	print(resp)

pytz.timezone('US/Pacific')

schedule.every().hour.do(my_job)
def fun(request):
	min_time = "23:50:00.0"
	max_time = "06:00:00.0"
	unaware = datetime.datetime.now()
	amsterdam = pytz.timezone(users.name)
	print(users.name)
	current_time = unaware.replace(tzinfo=amsterdam)
	d = current_time.astimezone(pytz.UTC)
	while True :
		if not (str(d) >= min_time and str(d) <= max_time):
			schedule.run_pending()