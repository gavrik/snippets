# snippets

Some useful snippets for daily coding

## queue.sql

Queue mechanism over the PostgreSQL database.
[The Medium Article](https://medium.com/@thegavrikstory/queue-on-postgresql-7e49cb50e114) with some explanations.

### Limitation

- Keep the queue table as small as possible. While using “for update skip locked” PostgreSQL scan whole table for row locks. It may be a performance issue.
- Does the order matter? If yes, this solution will not work for you.

## ATU

*Administrative structure of Ukraine*

- atu_parse.py - python library for parse XML file to CSV
- atu_load.sql - SQL statement for load data to PostgreSQL.
