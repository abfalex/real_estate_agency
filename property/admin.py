from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatFilter(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony', 'active')
    raw_id_fields = ['liked_by', 'owners']


@admin.register(Complaint)
class Complaint(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )
    search_fields = ('name', 'owners_phonenumber', 'owner_pure_phone')
