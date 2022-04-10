from django.db import models


# Create your models here.

vehicle_status = [
    ('R & D', 'run & drive'),
    ('S', 'start'),
    ('N/W', 'not working'),
]

damage_code = [
    ('AO', 'All Over - AO'),
    ('BC', 'Biohazard/Chemical - BC'),
    ('BN', 'Burn - BN'),
    ('BE', 'Burn - Engine - BE'),
    ('BI', 'Burn - Interior - BI'),
    ('CC', 'Cash for Clunkers - CC'),
    ('DH', 'Damage History - DH'),
    ('FD', 'Frame Damage Reported - FD'),
    ('FR', 'Front End - FR'),
    ('HL', 'Hail - HL'),
    ('MC', 'Mechanical - MC'),
    ('MW', 'Minor Dents/Scratches - MN'),
    ('NW', 'Normal Wear - NW'),
    ('PR', 'Partial/Incomplete Repair - PR'),
    ('RJ', 'Rejected Repair - RJ'),
    ('RO', 'Rollover - RO'),
    ('RR', 'Rear end - RR'),
    ('SD', 'Side Damage - SD'),
    ('ST', 'Stripped - ST'),
    ('TP', 'Top/Roof Damage - TP'),
    ('UK', 'Unknown - UK'),
    ('UN', 'Undercarriage - UN'),
    ('VN', 'Vandalism - VN'),
    ('VI', 'VIN - Missing/Altered - VI'),
    ('VP', 'VIN - Replaced - VP'),
    ('WA', 'Water/Flood - WA'),
]

color_choice = [
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Orange', 'Orange'),
    ('White', 'White'),
    ('Black', 'Black'),
    ('Yellow', 'Yellow'),
    ('Purple', 'Purple'),
    ('Silver', 'Silver'),
    ('Brown', 'Brown'),
    ('Grey', 'Grey'),
    ('Pink', 'Pink'),
    ('Olive', 'Olive'),
    ('Maroon', 'Maroon'),
    ('Violet', 'Violet'),
    ('Charcoal', 'Charcoal'),
    ('Magenta', 'Magenta'),
    ('Bronze', 'Bronze'),
    ('Cream', 'Cream'),
    ('Gold', 'Gold'),
    ('Tan', 'Tan'),
    ('Teal', 'Teal'),
    ('Mustard', 'Mustard'),
    ('Navy Blue', 'Navy Blue'),
    ('Coral', 'Coral'),
    ('Burgundy', 'Burgundy'),
    ('Lavender', 'Lavender'),
    ('Mauve', 'Mauve'),
    ('Peach', 'Peach'),
    ('Rust', 'Rust'),
    ('Indigo', 'Indigo'),
    ('Ruby', 'Ruby'),
    ('Clay', 'Clay'),
    ('Cyan', 'Cyan'),
    ('Azure', 'Azure'),
    ('Beige', 'Beige'),
    ('Off White', 'Beige'),
    ('Turquoise', 'Turquoise'),
    ('Amber', 'Amber'),
    ('Mint', 'Mint'),
]


class Vehicle(models.Model):

    vin = models.CharField(max_length=17, default='WDB2110281A301836')
    odometer = models.IntegerField()
    year = models.DateField()
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=vehicle_status)
    seller = models.CharField(max_length=30)
    primary_damage = models.CharField(max_length=10, choices=damage_code)
    secondary_damage = models.CharField(max_length=10, choices=damage_code)
    retail_value = models.IntegerField()
    body_style = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)
    color = models.CharField(max_length=9, choices=color_choice)
    engine_type = models.CharField(max_length=10)
    cylinders = models.CharField(max_length=10)
    transmission_type = models.CharField(max_length=10)
    drive_type = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    keys = models.CharField(max_length=3)
    notes = models.TextField()
    image = models.ImageField(upload_to='images/auction', null=True, blank=True)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.vin


motorcycle_type = [
    ('Standard', 'Standard'),
    ('Cruiser', 'Cruiser'),
    ('Sport Bike', 'Sport Bike'),
    ('Touring', 'Touring'),
    ('Sport Touring', 'Sport Touring'),
    ('Dual Sport', 'Dual Sport'),
    ('Scooter', 'Scooter'),
    ('Moped', 'Moped'),
    ('Off-road', 'Off-road'),
]

eng_cycle = [
    ('2T', '2T'),
    ('4T', '4T'),
]

eng_layout = [
    ('Single', 'Single'),
    ('Inline', 'Inline'),
    ('V', 'V'),
    ('L-Twin', 'L-Twin'),
    ('Flat', 'Flat'),
]

eng_cylinders = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
]

cooling_system = [
    ('Air Cooling', 'Air Cooling'),
    ('Liquid Cooling', 'Liquid Cooling'),
]

trans_type = [
    ('Sequential', 'Sequential'),
    ('CVT', 'CVT'),
    ('Dual Clutch', 'Dual Clutch'),
    ('Centrifugal Clutch', 'Centrifugal Clutch'),
]


class Motorcycle(models.Model):

    vin = models.CharField(max_length=17, default='WDB2110281A301836')
    odometer = models.CharField(max_length=10)
    year = models.DateField()
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=vehicle_status)
    seller = models.CharField(max_length=10)
    primary_damage = models.CharField(max_length=10, choices=damage_code)
    secondary_damage = models.CharField(max_length=10, choices=damage_code)
    retail_value = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=13, choices=motorcycle_type)
    color = models.CharField(max_length=9, choices=color_choice)
    engine_type = models.CharField(max_length=10, choices=eng_layout)
    engine_cycle = models.CharField(max_length=10, choices=eng_cycle)
    cylinders = models.CharField(max_length=10, choices=eng_cylinders)
    cooling = models.CharField(max_length=14, choices=cooling_system)
    transmission_type = models.CharField(max_length=18, choices=trans_type)
    notes = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.vin


trailer_body_types = [
    ('Van Trailer', 'Van Trailer'),
    ('Dump Trailer', 'Dump Trailer'),
    ('Livestock Trailer', 'Livestock Trailer'),
    ('Logging Trailer', 'Logging Trailer'),
    ('Travel Trailer', 'Travel Trailer'),
    ('Utility Trailer', 'Utility Trailer'),
    ('Tank Trailer', 'Tank Trailer'),
]


class Trailer(models.Model):

    vin = models.CharField(max_length=17, default='WDB2110281A301836')
    year = models.DateField()
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=vehicle_status)
    seller = models.CharField(max_length=10)
    primary_damage = models.CharField(max_length=10, choices=damage_code)
    secondary_damage = models.CharField(max_length=10, choices=damage_code)
    retail_value = models.CharField(max_length=10)
    body_style = models.CharField(max_length=17, choices=trailer_body_types)
    color = models.CharField(max_length=9, choices=color_choice)
    notes = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.vin


class SparePart(models.Model):

    type = models.CharField(max_length=10)
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    year = models.DateField()
    status = models.CharField(max_length=10, choices=vehicle_status)
    seller = models.CharField(max_length=10)
    primary_damage = models.CharField(max_length=10, choices=damage_code)
    secondary_damage = models.CharField(max_length=10, choices=damage_code)
    retail_value = models.CharField(max_length=10)
    notes = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class OtherItem(models.Model):

    type = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=vehicle_status)
    seller = models.CharField(max_length=20, null=True, blank=True)
    primary_damage = models.CharField(max_length=10, choices=damage_code)
    secondary_damage = models.CharField(max_length=10, choices=damage_code)
    retail_value = models.CharField(max_length=10, null=True, blank=True)
    notes = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='images/auction', null=True, blank=True)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.type
