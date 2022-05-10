from django.contrib import admin

from apps.military_unit.models import MilitaryUnit, MilitaryUnitInfo, Person, Staff, Personnel

admin.site.register(MilitaryUnit)
admin.site.register(MilitaryUnitInfo)
admin.site.register(Person)
admin.site.register(Staff)
admin.site.register(Personnel)
