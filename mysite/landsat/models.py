from django.db import models

# Create your models here.
from django.db import models
from django.core.files.storage import FileSystemStorage

msavioutput = FileSystemStorage(location='/MSAVI_output')
ndvioutput = FileSystemStorage(location='/NDVI_output')
toaoutput = FileSystemStorage(location='/TOA_output')
msavithumb = FileSystemStorage(location='/MSAVI_thumb')
ndvithumb = FileSystemStorage(location='/NDVI_thumb')
toathumb = FileSystemStorage(location='/TOA_thumb')
		
class file_storage(models.Model):
	MSAVI_output = models.FileField(storage=msavioutput)
	NDVI_output = models.FileField(storage=ndvioutput)
	TOA_output = models.FileField(storage=toaoutput)
	MSAVI_thumb = models.ImageField(storage=msavithumb)
	NDVI_thumb = models.ImageField(storage=ndvithumb)
	TOA_thumb = models.ImageField(storage=toathumb)