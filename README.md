# ScrapySpiderATCC
## Srapper für die Online Plattform atcc.org

Dieses Tool ist dafür gedacht via Sitemap verschiedene Informationen über alle Produkte die in der Sitemap vorhanden sind strukturiert in eine .CSV-Datei zu bringen.

Dafür muss in der Datei _sitemapReader.py_ das Array erweitert und die Datei dann ausgeführt werden.

Darauffolgend kann über die CLI einer der folgenden Befehle ausgeführt werden:


```shell
scrapy runspyder .\atcc_spider.py -o <Name der .CSV-Datei>
```

## Einstellungen
In der Datei _atcc\_spider.py_ können unter _custom_settings_ verschiedene Einstellungen getroffen werden.
