from django.db import migrations

def add_egyptian_cities(apps, schema_editor):
    City = apps.get_model('weather', 'City')
    egyptian_cities = ["Cairo", "Alexandria", "Giza"]
    for city in egyptian_cities:
        City.objects.get_or_create(name=city)

class Migration(migrations.Migration):
    dependencies = [
        ('weather', '0002_add_default_cities'),
    ]

    operations = [
        migrations.RunPython(add_egyptian_cities),
    ]
