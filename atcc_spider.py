import datetime

import scrapy
from scrapy.loader import ItemLoader
from items import atcc_scraper_item

DL_PRODUCT_INFORMATION_LIST = 'dl.product-information__list'
DL_PRODUCT_DETAILED_INFORMATION_LIST = 'div.generic-accordion__items'


class atcc_spider(scrapy.Spider):
    name = 'atcc'

    custom_settings = {
        'DOWNLOAD_DELAY': 2.5,
        'LOG_FILE': 'log/ATCC.log',
        'LOG_ENABLED': True,
        'LOG_LEVEL': 'INFO',
        'LOG_STDOUT': True
    }

    with open('data/sitemap.csv', 'r') as file:
        start_urls = [line.strip() for line in file]

    def parse(self, response, **kwargs):
        for article in response.css('main#main'):
            l = ItemLoader(item=atcc_scraper_item(), selector=article)

            l.add_css('_productInfo', DL_PRODUCT_INFORMATION_LIST)
            # l.add_css('_productDetailedInfo', DL_PRODUCT_DETAILED_INFORMATION_LIST) # Wahrscheinlich nicht benötigt

            l.add_css('productName', 'h1')
            l.add_css('productNumber', 'p.pdp-page-content__product-number')
            # l.add_css('productPrice', 'span.product-pricing__label')
            l.add_css('productPrice', 'div.product-pricing')
            l.add_css('bslNumber', 'h3.biosafety-callout__heading')
            l.add_css('bslLC', 'div.biosafety-callout__language-content')  # LC = language content
            l.add_css('bslP', 'div.biosafety-callout__precaution')  # P = Precaution
            # l.add_css('productInfo', DL_PRODUCT_INFORMATION_LIST)

            # Product information
            l.add_value('productCategory', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('strainDesignation', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('typeStrain', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('genomeSequencedStrain', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('applications', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('productFormat', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('isolationSource', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('geographicalIsolation', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('shippingInformation', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('storageConditions', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('source', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('immunogenSpecies', DL_PRODUCT_INFORMATION_LIST)
            l.add_value('immunogenStrain', DL_PRODUCT_INFORMATION_LIST)

            # Detailed product information list
            # General
            l.add_value('specificApplications', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('preceptrol', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('animal', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('propagationHost', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('materialDevelopment', DL_PRODUCT_DETAILED_INFORMATION_LIST)

            # Characteristics
            l.add_value('comments', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('matingType', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('mycoplasmaContamination', DL_PRODUCT_DETAILED_INFORMATION_LIST)

            # Handling information
            l.add_value('medium', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('temperature', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('handlingProcedure', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('handlingNotes', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('ploidy', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('genotype', DL_PRODUCT_DETAILED_INFORMATION_LIST)

            # Quality control specifications
            l.add_value('qualityControlSpecifications', DL_PRODUCT_DETAILED_INFORMATION_LIST)

            # History
            l.add_value('depositedAs', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('depositors', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('synonyms', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            l.add_value('specialCollection', DL_PRODUCT_DETAILED_INFORMATION_LIST)
            # l.add_value('chainOfCustody', DL_PRODUCT_DETAILED_INFORMATION_LIST)

            # Additional information
            l.add_value('crawlingDate', datetime.datetime.now())
            l.add_value('link', response.request.url)
            yield l.load_item()
