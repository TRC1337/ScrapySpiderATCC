import re
from bs4 import BeautifulSoup
import json

REGEX_PRICE_PATTERN = '([0-9]*\.[0-9]*)'
PRODUCT_INFORMATION_LIST_DICT = {}
REPLACEMENT_SEMICOLON = ':SEMICOLON:'


def price_cast(value):
    if value:
        # return re.search(REGEX_PRICE_PATTERN, value, 0).group()
        return value
    return 'N.A'


def replace_semicolon(value):
    return value.replace(';', REPLACEMENT_SEMICOLON)


def build_information_dict(value):
    if value:
        title = []
        data = []
        soup = BeautifulSoup(value, features='lxml')
        dt = soup.find_all('dt')
        for item in dt:
            title.append(item.text)
        dd = soup.find_all('dd')
        for item in dd:
            data.append(item.text)
        for i in range(len(title)):
            PRODUCT_INFORMATION_LIST_DICT[title[i]] = data[i]
            # with open('output/dict.txt', 'a') as f:
            #     f.write(json.dumps(PRODUCT_INFORMATION_LIST_DICT))
        return


def find_info(info):
    if PRODUCT_INFORMATION_LIST_DICT.get(info):
        return PRODUCT_INFORMATION_LIST_DICT.get(info)
    return


def find_product_category(value):
    return find_info('Product category')


def find_type_strain(value):
    return find_info('Type strain')


def find_strain_designation(value):
    return find_info('Strain designation')


def find_genome_sequenced_train(value):
    return find_info('Genome sequenced strain')


def find_applications(value):
    return find_info('Applications')


def find_product_format(value):
    return find_info('Product format')


def find_isolation_source(value):
    return find_info('Isolation source')


def find_geographical_isolation(value):
    return find_info('Geographical isolation')


def find_shipping_information(value):
    return find_info('Shipping information')


def find_storage_conditions(value):
    return find_info('Storage conditions')


def find_source(value):
    return find_info('Source')


def find_immunogen_species(value):
    return find_info('Immunogen species')


def find_immunogen_strain(value):
    return find_info('Immunogen strain')


def remove_multi_white_spaces(value):
    if value:
        return " ".join(value.split())
    return


# Detailed product information list
# General


def find_specific_applications(value):
    return find_info('Specific applications')


def find_preceptrol(value):
    return find_info('Preceptrol')


def find_animal(value):
    return find_info('Animal')


def find_propagation_host(value):
    return find_info('Propagation host')


def find_material_development(value):
    return find_info('Material development')


# Characteristics

def find_comments(value):
    return find_info('Comments')


def find_mating_type(value):
    return find_info('Mating type')


def find_ploidy(value):
    return find_info('Ploidy')


def find_genotype(value):
    return find_info('Genotype')


def find_mycoplasma_contamination(value):
    return find_info('Mycoplasma contamination')


# Handling information


def find_medium(value):
    return find_info('Medium')


def find_temperature(value):
    return find_info('Temperature')


def find_handling_procedure(value):
    return find_info('Handling procedure')


def find_handling_notes(value):
    return find_info('Handling notes')


# Quality control specifications

def find_quality_control_specifications(value):
    return find_info('Quality control specifications')


# History


def find_deposited_as(value):
    return find_info('Deposited as')


def find_depositors(value):
    return find_info('Depositors')


def find_chain_of_custody(value):
    return find_info('Chain of custody')


def find_synonyms(value):
    return find_info('Synonyms')


def find_special_collection(value):
    return find_info('Special collection')


# Additional information


def readable_date(value):
    return value.strftime('%d.%m.%Y %H:%M:%S')
