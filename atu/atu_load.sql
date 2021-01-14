create table public.atu (
    id serial not null primary key,
    state text,
    region text,
    city text,
    city_region text,
    street text
);

copy public.atu (
    state,
    region,
    city,
    city_region,
    street
)
from '<path_to_the_CSV_file>' (
    FORMAT csv,
    DELIMITER '|',
    NULL 'None',
    HEADER false,
    ESCAPE '\',
    QUOTE '"'
);
