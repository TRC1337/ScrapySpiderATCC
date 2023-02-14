import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags, replace_escape_chars, strip_html5_whitespace, replace_entities
from util import *


class atcc_scraper_item(scrapy.Item):
    _productInfo = scrapy.Field(input_processor=MapCompose(build_information_dict))
    productName = scrapy.Field(
        input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace, replace_entities),
        output_processor=TakeFirst())
    productNumber = scrapy.Field(
        input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace, replace_entities),
        output_processor=TakeFirst())
    productPrice = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_multi_white_spaces),
        output_processor=TakeFirst())

    # Biosafety information
    bslNumber = scrapy.Field(
        input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace, replace_entities),
        output_processor=TakeFirst())
    bslLC = scrapy.Field(
        input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace, replace_entities,
                                   replace_semicolon),
        output_processor=TakeFirst())
    bslP = scrapy.Field(
        input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace, replace_entities),
        output_processor=TakeFirst())

    # Product information list
    productCategory = scrapy.Field(
        input_processor=MapCompose(remove_multi_white_spaces, find_product_category, replace_escape_chars),
        output_processor=TakeFirst())
    strainDesignation = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_strain_designation, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    typeStrain = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_type_strain, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    genomeSequencedStrain = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_genome_sequenced_train, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    applications = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_applications, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    productFormat = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_product_format, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    isolationSource = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_isolation_source, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    geographicalIsolation = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_geographical_isolation, remove_multi_white_spaces,
                                   replace_escape_chars, replace_semicolon),
        output_processor=TakeFirst())
    shippingInformation = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_shipping_information, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    storageConditions = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_storage_conditions, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    source = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_source, remove_multi_white_spaces,
                                   replace_escape_chars, replace_semicolon),
        output_processor=TakeFirst())
    immunogenSpecies = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_immunogen_species, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    immunogenStrain = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_immunogen_species, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())

    # Detailed product information list
    # General
    specificApplications = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_specific_applications, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    preceptrol = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_preceptrol, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    animal = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_animal, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    propagationHost = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_propagation_host, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    materialDevelopment = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_material_development, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())

    # Characteristics
    comments = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_comments, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    matingType = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_mating_type, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    ploidy = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_ploidy, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    genotype = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_genotype, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    mycoplasmaContamination = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_mycoplasma_contamination, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())

    # Handling information
    medium = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_medium, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    temperature = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_temperature, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    handlingProcedure = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_handling_procedure, remove_multi_white_spaces,
                                   replace_escape_chars, replace_semicolon),
        output_processor=TakeFirst())
    handlingNotes = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_handling_notes, remove_multi_white_spaces,
                                   replace_escape_chars, replace_semicolon),
        output_processor=TakeFirst())

    # Quality control specifications
    qualityControlSpecifications = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_quality_control_specifications, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())

    # History
    depositedAs = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_deposited_as, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    depositors = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_depositors, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    synonyms = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_synonyms, remove_multi_white_spaces,
                                   replace_escape_chars, replace_semicolon),
        output_processor=TakeFirst())
    specialCollection = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace, find_special_collection, remove_multi_white_spaces,
                                   replace_escape_chars),
        output_processor=TakeFirst())
    # chainOfCustody = scrapy.Field(
    #     input_processor=MapCompose(find_chain_of_custody, remove_multi_white_spaces,
    #                                replace_escape_chars),
    #     output_processor=TakeFirst())

    # Additional information
    crawlingDate = scrapy.Field(input_processor=MapCompose(readable_date))
    link = scrapy.Field()
