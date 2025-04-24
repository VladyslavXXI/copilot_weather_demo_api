from django.db import migrations

def add_default_cities(apps, schema_editor):
    City = apps.get_model('weather', 'City')
    default_cities = [
        "Berlin", "Paris", "Madrid", "Rome", "Warsaw", "Vienna", "Budapest", "Prague", "Brussels", "Amsterdam",
        "Athens", "Dublin", "Lisbon", "Bucharest", "Sofia", "Stockholm", "Copenhagen", "Kyiv", "Lviv", "Odesa"
    ]
    for city in default_cities:
        City.objects.get_or_create(name=city)

class Migration(migrations.Migration):
    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_cities),
    ]
