import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, Region, State, Iso


def run():
    fhand = open('unesco/sites.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()


    for row in reader:
        print(row)

        category, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            area = float(row[6])
        except:
            area = None

        site = Site(name=row[0], description=row[1], justification=row[2], year=y,
                    longitude=row[4], latitude=row[5], area_hectares=area,
                    category=category, state=state, region=region, iso=iso)
        site.save()
