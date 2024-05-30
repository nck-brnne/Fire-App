from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        # Number of instances to create
        num_locations = 10
        num_incidents = 10
        num_fire_stations = 5
        num_firefighters = 20
        num_fire_trucks = 10
        num_weather_conditions = 10

        # Create fake Locations
        self.stdout.write('Creating locations...')
        locations = []
        for _ in range(num_locations):
            location = Locations.objects.create(
                name=fake.city(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            locations.append(location)

        # Create fake Fire Stations
        self.stdout.write('Creating fire stations...')
        fire_stations = []
        for _ in range(num_fire_stations):
            fire_station = FireStation.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            fire_stations.append(fire_station)

        # Create fake Incidents
        self.stdout.write('Creating incidents...')
        incidents = []
        for _ in range(num_incidents):
            incident = Incident.objects.create(
                location=fake.random_element(locations),
                date_time=fake.date_time(),
                severity_level=fake.random_element(elements=('Minor Fire', 'Moderate Fire', 'Major Fire')),
                description=fake.sentence(nb_words=10)
            )
            incidents.append(incident)

        # Create fake Firefighters
        self.stdout.write('Creating firefighters...')
        firefighters = []
        for _ in range(num_firefighters):
            firefighter = Firefighters.objects.create(
                name=fake.name(),
                rank=fake.random_element(elements=('Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief')),
                experience_level=fake.random_element(elements=('Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief')),
                station=fake.word()
            )
            firefighters.append(firefighter)

        # Create fake Fire Trucks
        self.stdout.write('Creating fire trucks...')
        fire_trucks = []
        for _ in range(num_fire_trucks):
            fire_truck = FireTruck.objects.create(
                truck_number=fake.bothify(text='Truck-###'),
                model=fake.word(),
                capacity=fake.random_number(digits=4, fix_len=True),
                station=fake.random_element(fire_stations)
            )
            fire_trucks.append(fire_truck)

        # Create fake Weather Conditions
        self.stdout.write('Creating weather conditions...')
        weather_conditions = []
        for _ in range(num_weather_conditions):
            weather_condition = WeatherConditions.objects.create(
                incident=fake.random_element(incidents),
                temperature=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                humidity=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                wind_speed=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                weather_description=fake.word()
            )
            weather_conditions.append(weather_condition)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))
