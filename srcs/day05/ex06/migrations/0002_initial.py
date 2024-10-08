# Generated by Django 4.2.14 on 2024-08-11 18:28

from django.db import migrations, connection

def update_changetimestamp_column_trigger(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE OR REPLACE FUNCTION update_changetimestamp_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
        ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
        update_changetimestamp_column();
        """)

class Migration(migrations.Migration):

    dependencies = [
       ('ex06', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_changetimestamp_column_trigger),
    ]
