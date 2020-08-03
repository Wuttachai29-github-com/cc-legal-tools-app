# Generated by Django 2.2.13 on 2020-07-02 12:52
from django.db import migrations

from licenses.import_metadata_from_rdf import MetadataImporter


def import_license_data(apps, schema_editor):
    LegalCode = apps.get_model("licenses.LegalCode")
    License = apps.get_model("licenses.License")
    LicenseLogo = apps.get_model("licenses.LicenseLogo")
    TranslatedLicenseName = apps.get_model("licenses.TranslatedLicenseName")
    MetadataImporter(LegalCode, License, LicenseLogo, TranslatedLicenseName).import_metadata(open("index.rdf", "rb"))


class Migration(migrations.Migration):

    dependencies = [
        ("licenses", "0001_initial"),
    ]

    operations = [migrations.RunPython(import_license_data, migrations.RunPython.noop)]
