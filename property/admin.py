from django.contrib import admin

from .models import Flat, Complaint, Owner

class MembershipInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner', 'flat')

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('address', 'town', 'pk',)
    readonly_fields = ["created_at"]
    list_display = ('pk', 'address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )
    inlines = [MembershipInline, ]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('owner',)
    raw_id_fields = ('flat',)
    inlines = [MembershipInline,]
    exclude = ['flat']



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
