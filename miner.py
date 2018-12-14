import requests
import requests_cache

from bs4 import BeautifulSoup

from models import Drug, LicensedOutlet

requests_cache.install_cache(backend='sqlite', expire_after=3600)

DRUG_REGISTER_URL = "https://www.nda.or.ug/drug-register/"
LICENSE_OUTLET_URL = "https://www.nda.or.ug/licensed-outlets/"


def mine_drug_register():
    drugs = []
    print("Fetching drug data...")
    response = requests.get(DRUG_REGISTER_URL)
    print("Done.")
    if not response.ok:
        print("Failed to fetch data.")
        return

    print("Setting up data...")
    drug_register_html = response.content
    drug_register = BeautifulSoup(drug_register_html, 'html.parser')

    for line_break in drug_register.find_all('br'):
        line_break.extract()

    data_table = drug_register.find(id="tablepress-42").tbody
    rows = data_table.find_all('tr')
    print("Done.")
    print("Parsing...")
    for row in rows:
        data = [str(item.string) for item in row.find_all('td')]
        drug = Drug(*data)
        drugs.append(drug)
    print("Done.")
    print("Writing to file...")

    drug_data = '\n'.join([drug.to_csv() for drug in drugs])
    headers = "identifier, nda_reg_number, license_holder, local_technical_rep, name_of_drug, manufacturer, country_of_manufacture, dosage_form, pack_size"
    drug_data = headers + "\n" + drug_data
    with open("data/drugs.csv", 'w') as file:
        file.write(drug_data)
    print("Done.")
    print("Complete!")
    print("\n")


def mine_licensed_outlet():
    outlet_list = []
    print("Fetching outlet data...")
    response = requests.get(LICENSE_OUTLET_URL)
    print("Done.")
    if not response.ok:
        print("Failed to fetch data.")
        return

    print("Setting up data...")
    outlet_html = response.content
    outlets = BeautifulSoup(outlet_html, 'html.parser')

    for line_break in outlets.find_all('br'):
        line_break.extract()

    data_table = outlets.find(id="tablepress-55").tbody
    rows = data_table.find_all('tr')
    print("Done.")
    print("Parsing...")
    for row in rows:
        data = [str(item.string) for item in row.find_all('td')]
        outlet = LicensedOutlet(*data)
        outlet_list.append(outlet)
    print("Done.")
    print("Writing to file...")

    outlet_data = '\n'.join([outlet.to_csv() for outlet in outlet_list])
    headers = "identifier, premises_name, premises_number, premises_category, application_date, psu_registration_number, supervising_pharmacist, district, region, street_or_road"
    outlet_data = headers + "\n" + outlet_data
    with open("data/licensed_outlets.csv", 'w') as file:
        file.write(outlet_data)
    print("Done.")
    print("Complete!")


if __name__ == "__main__":
    mine_drug_register()
    mine_licensed_outlet()
