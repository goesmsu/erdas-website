from django import forms

		
class create_download_batch(forms.Form):
	landsat = forms.CharField(label="Landsat Version (LC8 or LE7)", max_length=3)
	year = forms.CharField(label="Year (ex: 2015)", max_length=4)
	day = forms.CharField(label="Month and Day (ex: 0917", max_length=4)
	scene1 = forms.CharField(label="WRS1 (ex: 024)", max_length=3)
	scene2 = forms.CharField(label="WRS2 (ex: 034)", max_length=3)
	
#class create_user(forms.Form):
#	username = forms.CharField(label="Username: ", max_length=30)
#	password = forms.CharField(label="Password: ", max_length=30)
#	email = forms.CharField(label="Email: ", max_length=30)
	
	
	

		

