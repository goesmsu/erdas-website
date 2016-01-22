from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render
from django.core.context_processors import csrf
#from books.erdas import main
from mysite.forms import create_download_batch
#from final_website.script_edited import main
#from django.contrib.auth.models import User
from django.http import HttpResponse
import time
from datetime import date

def test(request):
	return HttpResponse("what")
	

def data_entry(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('download.html', c)
	
def data_compile(request):
	if request.method == 'POST':
		landsat = request.POST.get('landsat', '')
		year = request.POST.get('year', '')
		day = request.POST.get('day', '')
		scene1 = request.POST.get('scene1', '')
		scene2 = request.POST.get('scene2', '')
		
		list = 'cd C:/Users/bairdb/Desktop/website/landsat_download_script \npython download_landsat_scene.py -o scene -b %s -d %s%s -s %s%s -u usgs.txt --output C:/Users/bairdb/Desktop/website/mysite' % (landsat, year, day, scene1, scene2)
		f = open('C:/Users/bairdb/Desktop/website/mysite/download_landsat.bat', 'w')
		f.write(list)
		f.close()
		print list
		
		run = 'cd C:/Users/bairdb/Desktop/website/mysite \npython script_edited.py'
		erdas = open('C:/Users/bairdb/Desktop/website/mysite/run_erdas.bat', 'w')
		erdas.write(run)
		erdas.close()
		print run
		
		
		
		day_adjusted = str(day)
		month = day_adjusted[0:2]
		day_actual = day_adjusted[2:5]
		day_of_year_setup = date(int(year), int(month), int(day_actual))
		t = day_of_year_setup.timetuple()
		day_of_year = t[7]
		imagename = str(landsat) + str(scene1) + str(scene2) + str(year) + str(day_of_year) + 'LGN00'
		
		text = '<html><head></head><body><img src="C:/Users/bairdb/Desktop/website/mysite/static/' + imagename + '/ndvi_histogram.png"' + ' ' + 'style="width:500px;height:500px;">''</body></html>'
		page = open('C:/Users/bairdb/Desktop/website/mysite/mysite/templates/' + str(landsat) + str(scene1) + str(scene2) + str(year) + str(day_of_year) + 'LGN00.html', 'w')
		page.write(text)
		page.close()
		
		webpage = str(landsat) + str(scene1) + str(scene2) + str(year) + str(day_of_year) + 'LGN00.html'
		
		
		try:
			from subprocess import Popen
			p = Popen("C:/Users/bairdb/Desktop/website/mysite/download_landsat.bat")
			stdout, stderr = p.communicate()
			
			from subprocess import Popen
			e = Popen("C:/Users/bairdb/Desktop/website/mysite/run_erdas.bat")
			stdout, stderr = e.communicate()
			
			return render(request, webpage)
			
			
		except WindowsError:
			return HttpResponse("The batchfile wouldn't open")
		
	else:
		return render(request, 'download.html')
	
	
	
	

	
	

	
	
