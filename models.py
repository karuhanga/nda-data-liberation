class Drug:
    def __init__(self, identifier, nda_reg_number, license_holder, local_technical_rep, name_of_drug, manufacturer, country_of_manufacture, dosage_form, pack_size):
        self.identifier = identifier
        self.nda_reg_number = nda_reg_number
        self.license_holder = license_holder
        self.local_technical_rep = local_technical_rep
        self.name_of_drug = name_of_drug
        self.manufacturer = manufacturer
        self.country_of_manufacture = country_of_manufacture
        self.dosage_form = dosage_form
        self.pack_size = pack_size

    def __str__(self):
        return "{}: {}".format(self.name_of_drug, self.nda_reg_number)

    def to_csv(self):
        return "{identifier}, {nda_reg_number}, {license_holder}, {local_technical_rep}, {name_of_drug}, {manufacturer}, {country_of_manufacture}, {dosage_form}, {pack_size}".format(
            identifier=self.identifier, nda_reg_number=self.nda_reg_number, license_holder=self.license_holder,
            local_technical_rep=self.local_technical_rep, name_of_drug=self.name_of_drug,
            manufacturer=self.manufacturer, country_of_manufacture=self.country_of_manufacture,
            dosage_form=self.dosage_form, pack_size=self.pack_size)


class LicensedOutlet:
    def __init__(self, identifier, premises_name, premises_number, premises_category, application_date, psu_registration_number, supervising_pharmacist, district, region, street_or_road):
        self.identifier = identifier
        self.premises_name = premises_name
        self.premises_number = premises_number
        self.premises_category = premises_category
        self.application_date = application_date
        self.psu_registration_number = psu_registration_number
        self.supervising_pharmacist = supervising_pharmacist
        self.district = district
        self.region = region
        self.street_or_road = street_or_road

    def __str__(self):
        return "{}: {}".format(self.premises_number, self.premises_name)

    def to_csv(self):
        return "{identifier}, {premises_name}, {premises_number}, {premises_category}, {application_date}, {psu_registration_number}, {supervising_pharmacist}, {district}, {region}, {street_or_road}".format(
            identifier=self.identifier, premises_name=self.premises_name, premises_number=self.premises_number,
            premises_category=self.premises_category,
            application_date=self.application_date, psu_registration_number=self.psu_registration_number,
            supervising_pharmacist=self.supervising_pharmacist, district=self.district, region=self.region,
            street_or_road=self.street_or_road)
