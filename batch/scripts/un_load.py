import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    # fhand = open('unesco/test_data.csv')
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        # tidy the empty values up
        # year
        try:
            year_clean = int(row[3])
        except:
            year_clean = None
        # area_hectares
        try:
            area_hectares_clean = float(row[6])
        except:
            area_hectares_clean = None
        # state
        try:
            state_clean = str(row[8])
        except:
            state_clean = None

        row_category, created = Category.objects.get_or_create(name=row[7])
        row_state, created = State.objects.get_or_create(name=state_clean)  # row[8]
        row_region, created = Region.objects.get_or_create(name=row[9])
        row_iso, created = Iso.objects.get_or_create(name=row[10])

        site = Site(name=row[0],
                    description=row[1],
                    justification=row[2],
                    year=year_clean,
                    longitude=row[4],
                    latitude=row[5],
                    area_hectares=area_hectares_clean,
                    category=row_category,
                    state=row_state,
                    region=row_region,
                    iso=row_iso)
        site.save()
