-- create schema
create schema queue;

set search_path='queue';

-- create type
create type t_queue_status as enum (
    'NEW',
    'LOCKED',
    'DELETED'
);

-- create queue table
create table queue (
    id bigserial primary key,
    object bigint,
    status t_queue_status default 'NEW',
    created_ts timestamp default now()
);

-- push_message function.
-- push massages to the queue table.
create or replace function push_message( IN p_object bigint )
    returns boolean as
$funcbody$
DECLARE
    l_push_status boolean default false;
BEGIN

    insert into queue(object) values (p_object);

    l_push_status := true;

    return l_push_status;

END;
$funcbody$
language plpgsql;

-- get_message function
-- get message from queue table.
-- get only one unique messange per request.
create or replace function get_message()
    returns bigint as
$funcbody$
DECLARE
    l_object bigint;
    l_id bigint;
BEGIN

    begin
        update queue q1 set status = 'LOCKED'
         where q1.id = (
                select q2.id from queue q2
                where q2.status = 'NEW'
                for update skip locked limit 1 -- lock row for update. Another process will not get this row while reading table.
            )
        returning q1.id, q1.object into l_id, l_object;
        commit;
    end;
    -- PERFORM pg_sleep(10); -- <- for debug only
    -- additional logic can be here
    delete from queue where id = l_id;

    return l_object;

END
$funcbody$
language plpgsql;

-- select * from push_message(15);
-- select * from get_message();

-- TESTS
-- Generate messages
DO $$
<<block>>
DECLARE
    l_msg_count integer default 100;
    l_i integer default 11;
BEGIN
loop
    exit when l_i = l_msg_count + 1;
    perform push_message(l_i);
    l_i := l_i + 1;
end loop;
END block $$;

-- Get messages
-- Execute next code in parallel
DO $$
<<get_block>>
DECLARE
    l_result_id bigint default 0;
BEGIN

loop
    begin
        select * from get_message() into l_result_id;
    commit;
    end;
    if l_result_id is null
    then
        raise notice 'Sleep';
        -- perform pg_sleep(1);
    else
        raise notice 'Result: %', l_result_id;
    end if;
end loop;

END get_block $$;

