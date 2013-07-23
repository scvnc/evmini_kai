from django.contrib import admin
from evmini.models import Constituency, Election, Office, User, Candidate, Comment

for model in [Constituency, Election, Office, User, Candidate, Comment]:
	admin.site.register(model)
