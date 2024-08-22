from django.contrib import admin

# Register your models here.

from hatch.models import HatchInfo
from gecko.models import Gecko


# mother 은 gender = female 만 표시
# father 은 gender = male 만 표시

class HatchInfoAdmin(admin.ModelAdmin):
    list_display = ('id','father', 'mother', 'format_spawn_date', 'set_temperature')
    list_filter = ( 'father', 'mother', 'spawn_date')
    search_fields = ('father__name', 'mother__name')
    sortable_by = ('father', 'mother', 'format_spawn_date', 'set_temperature')

    # spawn_date format 변경
    def format_spawn_date(self, obj):
        return obj.spawn_date.strftime('%Y-%m-%d')

    format_spawn_date.short_description = '해칭일'
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'father':
            kwargs['queryset'] = Gecko.objects.filter(gender=Gecko.Gender.MALE)
        elif db_field.name == 'mother':
            kwargs['queryset'] = Gecko.objects.filter(gender=Gecko.Gender.FEMALE)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(HatchInfo, HatchInfoAdmin)
