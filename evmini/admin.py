from django.contrib import admin
from evmini.models import Election, Constituency

for model in [Election, Constituency]:
	
	admin.site.register(model)
