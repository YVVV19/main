from django.contrib import admin
from .models import Profile, Product, Review, Stuff, Person, Admin_Table

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Stuff)
admin.site.register(Person)
admin.site.register(Admin_Table)