# Administrative structure of Ukraine

Parse XML file to CSV file for fast load data to PostgreSQL database.

- atu_parse.py - python library for parse XML file to CSV
- atu_load.sql - SQL statement for load data to PostgreSQL

## Source Link

[ATU source file](https://data.gov.ua/dataset/a2d6c060-e7e6-4471-ac67-42cfa1742a19) from [data.gov.ua](data.gov.ua)

## XML file structure

```xml
    <RECORD>
        <OBL_NAME>Автономна Республіка Крим</OBL_NAME>
        <REGION_NAME></REGION_NAME>
        <CITY_NAME>м.Сімферополь</CITY_NAME>
        <CITY_REGION_NAME></CITY_REGION_NAME>
        <STREET_NAME>вул.Генічеська</STREET_NAME>
    </RECORD>
```

### CSV file structure

```
"Автономна Республіка Крим"|"None"|"м.Сімферополь"|"None"|"вул.Дніпровська"
```

### Execution

```bash
> atu_parse.py --input <path_to_XML_file> --output <path_to_CSV_file>
```

Change <path_to_the_CSV_file> to the real path in SQL file.

```bash
> psql <database_credentials> -f atu_load.sql
```
