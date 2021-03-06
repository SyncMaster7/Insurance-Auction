# Generated by Django 4.0.3 on 2022-04-09 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odometer', models.CharField(max_length=10)),
                ('year', models.DateField()),
                ('make', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('R & D', 'run & drive'), ('S', 'start'), ('N/W', 'not working')], max_length=10)),
                ('seller', models.CharField(max_length=10)),
                ('primary_damage', models.CharField(choices=[('AO', 'All Over'), ('BC', 'Biohazard/Chemical'), ('BN', 'Burn'), ('BE', 'Burn - Engine'), ('BI', 'Burn - Interior'), ('CC', 'Cash for Clunkers'), ('DH', 'Damage History'), ('FD', 'Frame Damage Reported - FD'), ('FR', 'Front End - FR'), ('HL', 'Hail - HL'), ('MC', 'Mechanical - MC'), ('MW', 'Minor Dents/Scratches - MN'), ('NW', 'Normal Wear - NW'), ('PR', 'Partial/Incomplete Repair - PR'), ('RJ', 'Rejected Repair - RJ'), ('RO', 'Rollover - RO'), ('RR', 'Rear end - RR'), ('SD', 'Side Damage - SD'), ('ST', 'Stripped - ST'), ('TP', 'Top/Roof Damage - TP'), ('UK', 'Unknown - UK'), ('UN', 'Undercarriage - UN'), ('VN', 'Vandalism - VN'), ('VI', 'VIN - Missing/Altered - VI'), ('VP', 'VIN - Replaced - VP'), ('WA', 'Water/Flood - WA')], max_length=10)),
                ('secondary_damage', models.CharField(choices=[('AO', 'All Over'), ('BC', 'Biohazard/Chemical'), ('BN', 'Burn'), ('BE', 'Burn - Engine'), ('BI', 'Burn - Interior'), ('CC', 'Cash for Clunkers'), ('DH', 'Damage History'), ('FD', 'Frame Damage Reported - FD'), ('FR', 'Front End - FR'), ('HL', 'Hail - HL'), ('MC', 'Mechanical - MC'), ('MW', 'Minor Dents/Scratches - MN'), ('NW', 'Normal Wear - NW'), ('PR', 'Partial/Incomplete Repair - PR'), ('RJ', 'Rejected Repair - RJ'), ('RO', 'Rollover - RO'), ('RR', 'Rear end - RR'), ('SD', 'Side Damage - SD'), ('ST', 'Stripped - ST'), ('TP', 'Top/Roof Damage - TP'), ('UK', 'Unknown - UK'), ('UN', 'Undercarriage - UN'), ('VN', 'Vandalism - VN'), ('VI', 'VIN - Missing/Altered - VI'), ('VP', 'VIN - Replaced - VP'), ('WA', 'Water/Flood - WA')], max_length=10)),
                ('retail_value', models.CharField(max_length=10)),
                ('body_style', models.CharField(max_length=10)),
                ('vehicle_type', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('engine_type', models.CharField(max_length=10)),
                ('cylinders', models.CharField(max_length=10)),
                ('transmission_type', models.CharField(max_length=10)),
                ('drive_type', models.CharField(max_length=10)),
                ('fuel', models.CharField(max_length=10)),
                ('keys', models.CharField(max_length=3)),
                ('notes', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('location', models.CharField(max_length=10)),
                ('vin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auction.vin')),
            ],
        ),
    ]
