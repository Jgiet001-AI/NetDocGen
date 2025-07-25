api-1  | INFO:     Shutting down
api-1  | INFO:     Waiting for application shutdown.
api-1  | 2025-07-24 20:22:54,617 - app.main - INFO - Shutting down application...
api-1  | INFO:     Application shutdown complete.
api-1  | INFO:     Finished server process [68]
api-1  | INFO:     Started server process [73]
api-1  | INFO:     Waiting for application startup.
api-1  | 2025-07-24 20:22:55,356 - app.main - INFO - Starting application lifespan...
api-1  | 2025-07-24 20:22:55,383 - sqlalchemy.engine.Engine - INFO - select pg_catalog.version()
api-1  | 2025-07-24 20:22:55,383 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:22:55,383 INFO sqlalchemy.engine.Engine select pg_catalog.version()
api-1  | 2025-07-24 20:22:55,383 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:22:55,384 - sqlalchemy.engine.Engine - INFO - select current_schema()
api-1  | 2025-07-24 20:22:55,384 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:22:55,384 INFO sqlalchemy.engine.Engine select current_schema()
api-1  | 2025-07-24 20:22:55,384 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:22:55,385 INFO sqlalchemy.engine.Engine show standard_conforming_strings
api-1  | 2025-07-24 20:22:55,385 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:22:55,385 - sqlalchemy.engine.Engine - INFO - show standard_conforming_strings
api-1  | 2025-07-24 20:22:55,385 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:22:55,386 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:22:55,386 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:22:55,387 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:22:55,387 INFO sqlalchemy.engine.Engine [generated in 0.00011s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,387 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:22:55,387 - sqlalchemy.engine.Engine - INFO - [generated in 0.00011s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,390 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:22:55,390 INFO sqlalchemy.engine.Engine [cached since 0.002822s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,390 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:22:55,390 - sqlalchemy.engine.Engine - INFO - [cached since 0.002822s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,391 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:22:55,391 INFO sqlalchemy.engine.Engine [cached since 0.003204s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,391 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:22:55,391 - sqlalchemy.engine.Engine - INFO - [cached since 0.003204s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,391 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | 2025-07-24 20:22:55,391 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:22:55,391 - sqlalchemy.engine.Engine - INFO - [generated in 0.00008s] ('projectstatus', 'pg_catalog')
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:22:55,391 INFO sqlalchemy.engine.Engine [generated in 0.00008s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,392 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:22:55,392 INFO sqlalchemy.engine.Engine [cached since 0.0007652s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,392 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:22:55,392 - sqlalchemy.engine.Engine - INFO - [cached since 0.0007652s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:22:55,393 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:22:55,393 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:22:55,393 - app.main - INFO - Initializing storage service...
api-1  | 2025-07-24 20:22:55,393 - app.services.storage - INFO - Initializing storage buckets...
api-1  | 2025-07-24 20:22:55,403 - app.services.storage - INFO - Storage buckets initialized successfully
api-1  | 2025-07-24 20:22:55,403 - app.main - INFO - Connecting to message queue...
api-1  | 2025-07-24 20:22:55,403 - app.services.message_queue - INFO - Connecting to RabbitMQ at amqp://guest:guest@rabbitmq:5672
api-1  | 2025-07-24 20:22:55,411 - app.services.message_queue - INFO - Successfully connected to RabbitMQ
api-1  | 2025-07-24 20:22:55,411 - app.main - INFO - Setting up message queue completion handlers...
api-1  | 2025-07-24 20:22:55,411 - app.services.message_queue - INFO - Setting up completion handlers...
api-1  | 2025-07-24 20:22:55,413 - shared.messaging.queue - INFO - Started consuming from api_parse_complete with routing key document.parse.complete
api-1  | 2025-07-24 20:22:55,414 - shared.messaging.queue - INFO - Started consuming from api_generate_complete with routing key document.generate.complete
api-1  | 2025-07-24 20:22:55,414 - app.services.message_queue - INFO - Completion handlers registered successfully
api-1  | 2025-07-24 20:22:55,414 - app.main - INFO - Application startup complete
api-1  | INFO:     Application startup complete.
api-1  | WARNING:  WatchFiles detected changes in 'app/routers/documents.py'. Reloading...
api-1  | INFO:     Shutting down
api-1  | INFO:     Waiting for application shutdown.
api-1  | 2025-07-24 20:23:33,509 - app.main - INFO - Shutting down application...
api-1  | INFO:     Application shutdown complete.
api-1  | INFO:     Finished server process [73]
api-1  | INFO:     Started server process [78]
api-1  | INFO:     Waiting for application startup.
api-1  | 2025-07-24 20:23:34,343 - app.main - INFO - Starting application lifespan...
api-1  | 2025-07-24 20:23:34,369 INFO sqlalchemy.engine.Engine select pg_catalog.version()
api-1  | 2025-07-24 20:23:34,369 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:23:34,369 - sqlalchemy.engine.Engine - INFO - select pg_catalog.version()
api-1  | 2025-07-24 20:23:34,369 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:23:34,370 INFO sqlalchemy.engine.Engine select current_schema()
api-1  | 2025-07-24 20:23:34,370 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:23:34,370 - sqlalchemy.engine.Engine - INFO - select current_schema()
api-1  | 2025-07-24 20:23:34,370 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:23:34,370 INFO sqlalchemy.engine.Engine show standard_conforming_strings
api-1  | 2025-07-24 20:23:34,371 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:23:34,370 - sqlalchemy.engine.Engine - INFO - show standard_conforming_strings
api-1  | 2025-07-24 20:23:34,371 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:23:34,371 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:23:34,371 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:23:34,373 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:34,373 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,373 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:34,373 - sqlalchemy.engine.Engine - INFO - [generated in 0.00010s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,375 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:34,375 - sqlalchemy.engine.Engine - INFO - [cached since 0.002184s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,375 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:34,375 INFO sqlalchemy.engine.Engine [cached since 0.002184s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,375 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:34,375 INFO sqlalchemy.engine.Engine [cached since 0.002657s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,375 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:34,375 - sqlalchemy.engine.Engine - INFO - [cached since 0.002657s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,376 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:34,376 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,376 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:34,376 - sqlalchemy.engine.Engine - INFO - [generated in 0.00007s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,377 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:34,377 INFO sqlalchemy.engine.Engine [cached since 0.0008106s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,377 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:34,377 - sqlalchemy.engine.Engine - INFO - [cached since 0.0008106s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:34,377 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:23:34,377 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:23:34,378 - app.main - INFO - Initializing storage service...
api-1  | 2025-07-24 20:23:34,378 - app.services.storage - INFO - Initializing storage buckets...
api-1  | 2025-07-24 20:23:34,392 - app.services.storage - INFO - Storage buckets initialized successfully
api-1  | 2025-07-24 20:23:34,392 - app.main - INFO - Connecting to message queue...
api-1  | 2025-07-24 20:23:34,392 - app.services.message_queue - INFO - Connecting to RabbitMQ at amqp://guest:guest@rabbitmq:5672
api-1  | 2025-07-24 20:23:34,398 - app.services.message_queue - INFO - Successfully connected to RabbitMQ
api-1  | 2025-07-24 20:23:34,398 - app.main - INFO - Setting up message queue completion handlers...
api-1  | 2025-07-24 20:23:34,398 - app.services.message_queue - INFO - Setting up completion handlers...
api-1  | 2025-07-24 20:23:34,400 - shared.messaging.queue - INFO - Started consuming from api_parse_complete with routing key document.parse.complete
api-1  | 2025-07-24 20:23:34,401 - shared.messaging.queue - INFO - Started consuming from api_generate_complete with routing key document.generate.complete
api-1  | 2025-07-24 20:23:34,401 - app.services.message_queue - INFO - Completion handlers registered successfully
api-1  | 2025-07-24 20:23:34,401 - app.main - INFO - Application startup complete
api-1  | INFO:     Application startup complete.
api-1  | WARNING:  WatchFiles detected changes in 'app/routers/documents.py'. Reloading...
api-1  | INFO:     Shutting down
api-1  | INFO:     Waiting for application shutdown.
api-1  | 2025-07-24 20:23:52,782 - app.main - INFO - Shutting down application...
api-1  | INFO:     Application shutdown complete.
api-1  | INFO:     Finished server process [78]
api-1  | INFO:     Started server process [83]
api-1  | INFO:     Waiting for application startup.
api-1  | 2025-07-24 20:23:53,689 - app.main - INFO - Starting application lifespan...
api-1  | 2025-07-24 20:23:53,709 - sqlalchemy.engine.Engine - INFO - select pg_catalog.version()
api-1  | 2025-07-24 20:23:53,709 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:23:53,709 INFO sqlalchemy.engine.Engine select pg_catalog.version()
api-1  | 2025-07-24 20:23:53,709 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:23:53,710 - sqlalchemy.engine.Engine - INFO - select current_schema()
api-1  | 2025-07-24 20:23:53,710 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:23:53,710 INFO sqlalchemy.engine.Engine select current_schema()
api-1  | 2025-07-24 20:23:53,710 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:23:53,711 INFO sqlalchemy.engine.Engine show standard_conforming_strings
api-1  | 2025-07-24 20:23:53,711 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:23:53,711 - sqlalchemy.engine.Engine - INFO - show standard_conforming_strings
api-1  | 2025-07-24 20:23:53,711 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:23:53,712 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:23:53,712 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:23:53,714 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:53,714 INFO sqlalchemy.engine.Engine [generated in 0.00012s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,714 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:53,714 - sqlalchemy.engine.Engine - INFO - [generated in 0.00012s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,718 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:53,718 INFO sqlalchemy.engine.Engine [cached since 0.003556s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,718 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:53,718 - sqlalchemy.engine.Engine - INFO - [cached since 0.003556s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,718 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:53,718 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:23:53,718 INFO sqlalchemy.engine.Engine [cached since 0.004044s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,718 - sqlalchemy.engine.Engine - INFO - [cached since 0.004044s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,720 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:53,720 - sqlalchemy.engine.Engine - INFO - [generated in 0.00008s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,720 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:53,720 INFO sqlalchemy.engine.Engine [generated in 0.00008s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,721 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:53,721 INFO sqlalchemy.engine.Engine [cached since 0.001224s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,721 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:23:53,721 - sqlalchemy.engine.Engine - INFO - [cached since 0.001224s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:23:53,722 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:23:53,722 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:23:53,723 - app.main - INFO - Initializing storage service...
api-1  | 2025-07-24 20:23:53,723 - app.services.storage - INFO - Initializing storage buckets...
api-1  | 2025-07-24 20:23:53,733 - app.services.storage - INFO - Storage buckets initialized successfully
api-1  | 2025-07-24 20:23:53,733 - app.main - INFO - Connecting to message queue...
api-1  | 2025-07-24 20:23:53,733 - app.services.message_queue - INFO - Connecting to RabbitMQ at amqp://guest:guest@rabbitmq:5672
api-1  | 2025-07-24 20:23:53,740 - app.services.message_queue - INFO - Successfully connected to RabbitMQ
api-1  | 2025-07-24 20:23:53,740 - app.main - INFO - Setting up message queue completion handlers...
api-1  | 2025-07-24 20:23:53,740 - app.services.message_queue - INFO - Setting up completion handlers...
api-1  | 2025-07-24 20:23:53,741 - shared.messaging.queue - INFO - Started consuming from api_parse_complete with routing key document.parse.complete
api-1  | 2025-07-24 20:23:53,742 - shared.messaging.queue - INFO - Started consuming from api_generate_complete with routing key document.generate.complete
api-1  | 2025-07-24 20:23:53,742 - app.services.message_queue - INFO - Completion handlers registered successfully
api-1  | 2025-07-24 20:23:53,742 - app.main - INFO - Application startup complete
api-1  | INFO:     Application startup complete.
api-1  | WARNING:  WatchFiles detected changes in 'app/routers/documents.py'. Reloading...
api-1  | INFO:     Shutting down
api-1  | INFO:     Waiting for application shutdown.
api-1  | 2025-07-24 20:24:19,744 - app.main - INFO - Shutting down application...
api-1  | INFO:     Application shutdown complete.
api-1  | INFO:     Finished server process [83]
api-1  | INFO:     Started server process [88]
api-1  | INFO:     Waiting for application startup.
api-1  | 2025-07-24 20:24:20,534 - app.main - INFO - Starting application lifespan...
api-1  | 2025-07-24 20:24:20,552 - sqlalchemy.engine.Engine - INFO - select pg_catalog.version()
api-1  | 2025-07-24 20:24:20,552 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:24:20,552 INFO sqlalchemy.engine.Engine select pg_catalog.version()
api-1  | 2025-07-24 20:24:20,552 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:24:20,553 INFO sqlalchemy.engine.Engine select current_schema()
api-1  | 2025-07-24 20:24:20,553 - sqlalchemy.engine.Engine - INFO - select current_schema()
api-1  | 2025-07-24 20:24:20,553 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:24:20,553 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:24:20,553 INFO sqlalchemy.engine.Engine show standard_conforming_strings
api-1  | 2025-07-24 20:24:20,553 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:24:20,553 - sqlalchemy.engine.Engine - INFO - show standard_conforming_strings
api-1  | 2025-07-24 20:24:20,553 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:24:20,554 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:24:20,554 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:24:20,556 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:20,556 - sqlalchemy.engine.Engine - INFO - [generated in 0.00010s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,556 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:20,556 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,558 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:20,558 INFO sqlalchemy.engine.Engine [cached since 0.002237s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,558 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:20,558 - sqlalchemy.engine.Engine - INFO - [cached since 0.002237s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,558 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:20,558 INFO sqlalchemy.engine.Engine [cached since 0.002635s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,558 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:20,558 - sqlalchemy.engine.Engine - INFO - [cached since 0.002635s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,559 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:20,559 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:20,559 - sqlalchemy.engine.Engine - INFO - [generated in 0.00007s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,559 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,560 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | 2025-07-24 20:24:20,560 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:20,560 - sqlalchemy.engine.Engine - INFO - [cached since 0.0007476s ago] ('documentstatus', 'pg_catalog')
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:20,560 INFO sqlalchemy.engine.Engine [cached since 0.0007476s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:20,560 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:24:20,560 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:24:20,560 - app.main - INFO - Initializing storage service...
api-1  | 2025-07-24 20:24:20,560 - app.services.storage - INFO - Initializing storage buckets...
api-1  | 2025-07-24 20:24:20,580 - app.services.storage - INFO - Storage buckets initialized successfully
api-1  | 2025-07-24 20:24:20,580 - app.main - INFO - Connecting to message queue...
api-1  | 2025-07-24 20:24:20,580 - app.services.message_queue - INFO - Connecting to RabbitMQ at amqp://guest:guest@rabbitmq:5672
api-1  | 2025-07-24 20:24:20,591 - app.services.message_queue - INFO - Successfully connected to RabbitMQ
api-1  | 2025-07-24 20:24:20,591 - app.main - INFO - Setting up message queue completion handlers...
api-1  | 2025-07-24 20:24:20,591 - app.services.message_queue - INFO - Setting up completion handlers...
api-1  | 2025-07-24 20:24:20,593 - shared.messaging.queue - INFO - Started consuming from api_parse_complete with routing key document.parse.complete
api-1  | 2025-07-24 20:24:20,594 - shared.messaging.queue - INFO - Started consuming from api_generate_complete with routing key document.generate.complete
api-1  | 2025-07-24 20:24:20,594 - app.services.message_queue - INFO - Completion handlers registered successfully
api-1  | 2025-07-24 20:24:20,594 - app.main - INFO - Application startup complete
api-1  | INFO:     Application startup complete.
api-1  | WARNING:  WatchFiles detected changes in 'app/main.py'. Reloading...
api-1  | INFO:     Shutting down
api-1  | INFO:     Waiting for application shutdown.
api-1  | 2025-07-24 20:24:38,164 - app.main - INFO - Shutting down application...
api-1  | INFO:     Application shutdown complete.
api-1  | INFO:     Finished server process [88]
api-1  | INFO:     Started server process [93]
api-1  | INFO:     Waiting for application startup.
api-1  | 2025-07-24 20:24:38,964 - app.main - INFO - Starting application lifespan...
api-1  | 2025-07-24 20:24:38,984 - sqlalchemy.engine.Engine - INFO - select pg_catalog.version()
api-1  | 2025-07-24 20:24:38,984 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:24:38,984 INFO sqlalchemy.engine.Engine select pg_catalog.version()
api-1  | 2025-07-24 20:24:38,984 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:24:38,985 - sqlalchemy.engine.Engine - INFO - select current_schema()
api-1  | 2025-07-24 20:24:38,985 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:24:38,985 INFO sqlalchemy.engine.Engine select current_schema()
api-1  | 2025-07-24 20:24:38,985 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:24:38,985 INFO sqlalchemy.engine.Engine show standard_conforming_strings
api-1  | 2025-07-24 20:24:38,985 INFO sqlalchemy.engine.Engine [raw sql] ()
api-1  | 2025-07-24 20:24:38,985 - sqlalchemy.engine.Engine - INFO - show standard_conforming_strings
api-1  | 2025-07-24 20:24:38,985 - sqlalchemy.engine.Engine - INFO - [raw sql] ()
api-1  | 2025-07-24 20:24:38,986 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:24:38,986 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:24:38,987 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:38,988 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,987 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:38,988 - sqlalchemy.engine.Engine - INFO - [generated in 0.00010s] ('users', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,989 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | 2025-07-24 20:24:38,989 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:38,989 - sqlalchemy.engine.Engine - INFO - [cached since 0.002031s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:38,989 INFO sqlalchemy.engine.Engine [cached since 0.002031s ago] ('projects', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,990 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:38,990 INFO sqlalchemy.engine.Engine [cached since 0.002365s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,990 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_class.relname 
api-1  | FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
api-1  | WHERE pg_catalog.pg_class.relname = $1::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[$2::VARCHAR, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != $7::VARCHAR
api-1  | 2025-07-24 20:24:38,990 - sqlalchemy.engine.Engine - INFO - [cached since 0.002365s ago] ('documents', 'r', 'p', 'f', 'v', 'm', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,991 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:38,991 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,991 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:38,991 - sqlalchemy.engine.Engine - INFO - [generated in 0.00009s] ('projectstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,991 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:38,991 INFO sqlalchemy.engine.Engine [cached since 0.000807s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,991 - sqlalchemy.engine.Engine - INFO - SELECT pg_catalog.pg_type.typname 
api-1  | FROM pg_catalog.pg_type JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_type.typnamespace 
api-1  | WHERE pg_catalog.pg_type.typname = $1::VARCHAR AND pg_catalog.pg_type_is_visible(pg_catalog.pg_type.oid) AND pg_catalog.pg_namespace.nspname != $2::VARCHAR
api-1  | 2025-07-24 20:24:38,991 - sqlalchemy.engine.Engine - INFO - [cached since 0.000807s ago] ('documentstatus', 'pg_catalog')
api-1  | 2025-07-24 20:24:38,992 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:24:38,992 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:24:38,992 - app.main - INFO - Initializing storage service...
api-1  | 2025-07-24 20:24:38,992 - app.services.storage - INFO - Initializing storage buckets...
api-1  | 2025-07-24 20:24:39,004 - app.services.storage - INFO - Storage buckets initialized successfully
api-1  | 2025-07-24 20:24:39,004 - app.main - INFO - Connecting to message queue...
api-1  | 2025-07-24 20:24:39,004 - app.services.message_queue - INFO - Connecting to RabbitMQ at amqp://guest:guest@rabbitmq:5672
api-1  | 2025-07-24 20:24:39,011 - app.services.message_queue - INFO - Successfully connected to RabbitMQ
api-1  | 2025-07-24 20:24:39,011 - app.main - INFO - Setting up message queue completion handlers...
api-1  | 2025-07-24 20:24:39,011 - app.services.message_queue - INFO - Setting up completion handlers...
api-1  | 2025-07-24 20:24:39,013 - shared.messaging.queue - INFO - Started consuming from api_parse_complete with routing key document.parse.complete
api-1  | 2025-07-24 20:24:39,014 - shared.messaging.queue - INFO - Started consuming from api_generate_complete with routing key document.generate.complete
api-1  | 2025-07-24 20:24:39,014 - app.services.message_queue - INFO - Completion handlers registered successfully
api-1  | 2025-07-24 20:24:39,014 - app.main - INFO - Application startup complete
api-1  | INFO:     Application startup complete.
api-1  | INFO:     192.168.65.1:36533 - "OPTIONS /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:30067 - "OPTIONS /api/projects HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:36533 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:26:19,883 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:26:19,883 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:26:19,894 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:19,894 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:19,894 INFO sqlalchemy.engine.Engine [generated in 0.00035s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:19,894 - sqlalchemy.engine.Engine - INFO - [generated in 0.00035s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:36533 - "OPTIONS /api/projects/ HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:26:19,909 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:26:19,909 INFO sqlalchemy.engine.Engine [generated in 0.00017s] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:26:19,909 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:26:19,909 - sqlalchemy.engine.Engine - INFO - [generated in 0.00017s] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:26:19,931 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:26:19,931 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:26:19,932 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:19,932 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:19,932 INFO sqlalchemy.engine.Engine [cached since 0.03794s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:19,932 - sqlalchemy.engine.Engine - INFO - [cached since 0.03794s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:19,935 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | 2025-07-24 20:26:19,935 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:26:19,935 INFO sqlalchemy.engine.Engine [generated in 0.00008s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:26:19,935 - sqlalchemy.engine.Engine - INFO - [generated in 0.00008s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:19,940 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:26:19,940 INFO sqlalchemy.engine.Engine [generated in 0.00017s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:26:19,940 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:26:19,940 - sqlalchemy.engine.Engine - INFO - [generated in 0.00017s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | INFO:     192.168.65.1:60682 - "GET /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:26:19,958 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:26:19,958 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:26:19,980 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:26:19,980 INFO sqlalchemy.engine.Engine [generated in 0.00014s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:26:19,980 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:26:19,980 - sqlalchemy.engine.Engine - INFO - [generated in 0.00014s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:26:19,980 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:26:19,980 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:30067 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:26:43,849 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:26:43,849 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:26:43,854 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:43,854 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:43,855 - sqlalchemy.engine.Engine - INFO - [cached since 23.96s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:43,855 INFO sqlalchemy.engine.Engine [cached since 23.96s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:39050 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:26:43,871 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:26:43,871 - sqlalchemy.engine.Engine - INFO - [cached since 23.96s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:26:43,871 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:26:43,871 INFO sqlalchemy.engine.Engine [cached since 23.96s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:26:43,872 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:26:43,872 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:26:43,873 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:43,873 - sqlalchemy.engine.Engine - INFO - [cached since 23.98s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:43,873 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:26:43,873 INFO sqlalchemy.engine.Engine [cached since 23.98s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:64595 - "GET /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:26:43,877 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:26:43,877 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:26:43,879 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | 2025-07-24 20:26:43,879 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:26:43,879 INFO sqlalchemy.engine.Engine [cached since 23.94s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:26:43,879 - sqlalchemy.engine.Engine - INFO - [cached since 23.94s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:26:43,882 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:26:43,882 INFO sqlalchemy.engine.Engine [generated in 0.00021s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:26:43,882 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:26:43,882 - sqlalchemy.engine.Engine - INFO - [generated in 0.00021s] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:26:43,885 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:26:43,885 - sqlalchemy.engine.Engine - INFO - [cached since 23.91s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:26:43,885 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:26:43,885 INFO sqlalchemy.engine.Engine [cached since 23.91s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:26:43,885 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:26:43,885 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:39050 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:27:17,860 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:27:17,860 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:27:17,865 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:27:17,865 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:27:17,865 INFO sqlalchemy.engine.Engine [cached since 57.97s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:27:17,865 - sqlalchemy.engine.Engine - INFO - [cached since 57.97s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:58675 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:27:17,880 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:27:17,880 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:27:17,880 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:27:17,880 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:27:17,880 INFO sqlalchemy.engine.Engine [cached since 57.99s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:27:17,880 - sqlalchemy.engine.Engine - INFO - [cached since 57.99s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:27:17,891 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:27:17,891 INFO sqlalchemy.engine.Engine [cached since 57.98s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:27:17,891 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:27:17,891 - sqlalchemy.engine.Engine - INFO - [cached since 57.98s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:27:17,894 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | 2025-07-24 20:27:17,894 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:27:17,894 - sqlalchemy.engine.Engine - INFO - [cached since 57.96s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:27:17,894 INFO sqlalchemy.engine.Engine [cached since 57.96s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:63009 - "GET /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:27:17,896 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:27:17,896 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:27:17,896 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:27:17,896 INFO sqlalchemy.engine.Engine [cached since 34.01s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:27:17,896 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:27:17,896 - sqlalchemy.engine.Engine - INFO - [cached since 34.01s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:27:17,898 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:27:17,898 INFO sqlalchemy.engine.Engine [cached since 57.92s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:27:17,898 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:27:17,898 - sqlalchemy.engine.Engine - INFO - [cached since 57.92s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:27:17,898 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:27:17,898 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:58675 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:27,260 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,260 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,262 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,262 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,262 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,262 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:36082 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:36082 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:27,271 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,272 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,272 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,271 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,272 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,272 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,281 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:27,281 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:27,281 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:27,281 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:27,284 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:27,284 - sqlalchemy.engine.Engine - INFO - [cached since 187.3s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,284 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:27,284 INFO sqlalchemy.engine.Engine [cached since 187.3s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:45048 - "GET /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:27,286 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:27,286 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:27,287 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:27,287 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:27,287 INFO sqlalchemy.engine.Engine [cached since 163.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:27,287 - sqlalchemy.engine.Engine - INFO - [cached since 163.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:27,289 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,289 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,289 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,289 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,289 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,289 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,295 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:27,295 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | 2025-07-24 20:29:27,295 INFO sqlalchemy.engine.Engine [cached since 187.3s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:27,295 - sqlalchemy.engine.Engine - INFO - [cached since 187.3s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:27,296 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:27,296 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:36082 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:40883 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:27,313 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:27,313 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:27,313 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:27,313 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:27,317 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,318 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,318 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,317 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,318 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,318 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:45048 - "GET /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:27,320 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:27,320 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:27,325 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:27,325 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:27,326 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,326 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,328 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,328 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,328 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,328 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,329 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,329 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,333 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | 2025-07-24 20:29:27,333 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:27,333 - sqlalchemy.engine.Engine - INFO - [cached since 163.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:27,333 INFO sqlalchemy.engine.Engine [cached since 163.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:27,335 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:27,335 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:27,335 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:27,335 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('6e83827a-8e3b-4f4a-a110-08812f66fef6'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:27,337 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:27,337 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:27,337 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:27,337 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:27,337 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:27,337 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:27,339 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:45048 - "GET /api/documents/6e83827a-8e3b-4f4a-a110-08812f66fef6 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:27,339 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:36082 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:27,355 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,355 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,355 - sqlalchemy.engine.Engine - INFO - [cached since 187.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,355 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:27,355 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:27,355 INFO sqlalchemy.engine.Engine [cached since 187.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,358 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:27,358 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:27,359 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,359 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:27,361 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:27,361 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:27,361 INFO sqlalchemy.engine.Engine [cached since 163.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:27,361 - sqlalchemy.engine.Engine - INFO - [cached since 163.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:27,364 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:27,364 - sqlalchemy.engine.Engine - INFO - [cached since 187.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:27,364 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:27,364 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:27,364 INFO sqlalchemy.engine.Engine [cached since 187.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:27,364 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:45048 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:53008 - "OPTIONS /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:41619 - "OPTIONS /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:42532 - "OPTIONS /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:64932 - "OPTIONS /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:29,475 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:29,475 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:29,476 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:29,476 INFO sqlalchemy.engine.Engine [cached since 189.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:29,476 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:29,476 - sqlalchemy.engine.Engine - INFO - [cached since 189.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:65531 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:29,489 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:29,489 - sqlalchemy.engine.Engine - INFO - [generated in 0.00026s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:29,489 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:29,489 INFO sqlalchemy.engine.Engine [generated in 0.00026s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:65531 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:29,512 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:29,513 INFO sqlalchemy.engine.Engine [generated in 0.00036s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:29,512 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:29,513 - sqlalchemy.engine.Engine - INFO - [generated in 0.00036s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:53008 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:29,517 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:29,517 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:29,518 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:29,518 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:29,518 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:29,519 INFO sqlalchemy.engine.Engine [cached since 189.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:29,518 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:29,519 - sqlalchemy.engine.Engine - INFO - [cached since 189.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:29,520 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:29,520 - sqlalchemy.engine.Engine - INFO - [cached since 0.03065s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:29,520 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:29,520 INFO sqlalchemy.engine.Engine [cached since 0.03065s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:29,522 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:29,522 INFO sqlalchemy.engine.Engine [cached since 0.01012s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:29,522 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:29,522 - sqlalchemy.engine.Engine - INFO - [cached since 0.01012s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:53008 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:29,540 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:29,540 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:61059 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:61059 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:30,707 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:30,707 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:30,708 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:30,708 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:30,708 - sqlalchemy.engine.Engine - INFO - [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,708 INFO sqlalchemy.engine.Engine [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,716 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:30,716 INFO sqlalchemy.engine.Engine [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,716 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:30,716 - sqlalchemy.engine.Engine - INFO - [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,721 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:30,721 INFO sqlalchemy.engine.Engine [cached since 166.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:30,721 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:30,721 - sqlalchemy.engine.Engine - INFO - [cached since 166.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:30,727 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:30,727 - sqlalchemy.engine.Engine - INFO - [cached since 190.7s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:30,727 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:30,727 INFO sqlalchemy.engine.Engine [cached since 190.7s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:30,727 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:30,727 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:43592 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:30,733 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:30,733 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:30,733 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:30,733 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:30,733 - sqlalchemy.engine.Engine - INFO - [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,733 INFO sqlalchemy.engine.Engine [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,735 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:30,735 - sqlalchemy.engine.Engine - INFO - [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,735 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:30,735 INFO sqlalchemy.engine.Engine [cached since 190.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:30,736 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:30,736 INFO sqlalchemy.engine.Engine [cached since 166.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:30,736 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:30,736 - sqlalchemy.engine.Engine - INFO - [cached since 166.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:30,737 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:30,737 INFO sqlalchemy.engine.Engine [cached since 190.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:30,737 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:30,737 - sqlalchemy.engine.Engine - INFO - [cached since 190.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:30,737 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:30,737 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:61059 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:30997 - "OPTIONS /api/documents/upload?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:35,508 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:35,508 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:35,509 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:35,509 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:35,510 INFO sqlalchemy.engine.Engine [cached since 195.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:35,510 - sqlalchemy.engine.Engine - INFO - [cached since 195.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:35,515 - app.routers.documents - INFO - Received upload request from user 4370f178-0e62-4eec-aada-fe76a4382961 for project 5ac5b233-265f-4a89-aafa-c54a2bb010a9
api-1  | 2025-07-24 20:29:35,515 - app.routers.documents - DEBUG - File details - name: CTL-Belmont Park Arena-Diagram.vsdx, content_type: application/octet-stream, size: 9023847
api-1  | 2025-07-24 20:29:35,515 - app.services.document - INFO - Starting document upload for project 5ac5b233-265f-4a89-aafa-c54a2bb010a9, user 4370f178-0e62-4eec-aada-fe76a4382961, file: CTL-Belmont Park Arena-Diagram.vsdx
api-1  | 2025-07-24 20:29:35,517 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:35,517 - sqlalchemy.engine.Engine - INFO - [generated in 0.00013s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:35,517 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:35,517 INFO sqlalchemy.engine.Engine [generated in 0.00013s] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:35,530 - sqlalchemy.engine.Engine - INFO - INSERT INTO documents (id, project_id, filename, original_filename, file_path, file_size, content_type, status, error_message, parsed_data_path, shape_count, connection_count, page_count, uploaded_by, parsed_at, completed_at, ai_analysis_completed) VALUES ($1::UUID, $2::UUID, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::INTEGER, $7::VARCHAR, $8::documentstatus, $9::VARCHAR, $10::VARCHAR, $11::INTEGER, $12::INTEGER, $13::INTEGER, $14::UUID, $15::TIMESTAMP WITH TIME ZONE, $16::TIMESTAMP WITH TIME ZONE, $17::BOOLEAN) RETURNING documents.uploaded_at
api-1  | 2025-07-24 20:29:35,530 INFO sqlalchemy.engine.Engine INSERT INTO documents (id, project_id, filename, original_filename, file_path, file_size, content_type, status, error_message, parsed_data_path, shape_count, connection_count, page_count, uploaded_by, parsed_at, completed_at, ai_analysis_completed) VALUES ($1::UUID, $2::UUID, $3::VARCHAR, $4::VARCHAR, $5::VARCHAR, $6::INTEGER, $7::VARCHAR, $8::documentstatus, $9::VARCHAR, $10::VARCHAR, $11::INTEGER, $12::INTEGER, $13::INTEGER, $14::UUID, $15::TIMESTAMP WITH TIME ZONE, $16::TIMESTAMP WITH TIME ZONE, $17::BOOLEAN) RETURNING documents.uploaded_at
api-1  | 2025-07-24 20:29:35,530 INFO sqlalchemy.engine.Engine [generated in 0.00057s] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), 'CTL-Belmont Park Arena-Diagram.vsdx', 'CTL-Belmont Park Arena-Diagram.vsdx', None, 9023847, 'application/octet-stream', 'UPLOADED', None, None, None, None, None, UUID('4370f178-0e62-4eec-aada-fe76a4382961'), None, None, False)
api-1  | 2025-07-24 20:29:35,530 - sqlalchemy.engine.Engine - INFO - [generated in 0.00057s] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), 'CTL-Belmont Park Arena-Diagram.vsdx', 'CTL-Belmont Park Arena-Diagram.vsdx', None, 9023847, 'application/octet-stream', 'UPLOADED', None, None, None, None, None, UUID('4370f178-0e62-4eec-aada-fe76a4382961'), None, None, False)
api-1  | 2025-07-24 20:29:35,535 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:29:35,535 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:29:35,541 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:35,541 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:35,541 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.id = $1::UUID
api-1  | 2025-07-24 20:29:35,541 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.id = $1::UUID
api-1  | 2025-07-24 20:29:35,541 - sqlalchemy.engine.Engine - INFO - [generated in 0.00007s] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'),)
api-1  | 2025-07-24 20:29:35,541 INFO sqlalchemy.engine.Engine [generated in 0.00007s] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'),)
api-1  | 2025-07-24 20:29:35,543 - app.services.storage - INFO - Uploading Visio file for document 08a8f790-ffa1-429a-8aae-616dde9d5976, filename: CTL-Belmont Park Arena-Diagram.vsdx
api-1  | 2025-07-24 20:29:35,543 - app.services.storage - DEBUG - Storage filename: 08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx
api-1  | 2025-07-24 20:29:35,543 - app.services.storage - INFO - Uploading to MinIO bucket 'uploads' with object name: 08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx
api-1  | 2025-07-24 20:29:35,690 - shared.storage.minio_client - INFO - Uploaded 08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx to netdocgen-uploads
api-1  | 2025-07-24 20:29:35,691 - app.services.storage - INFO - File uploaded successfully to: netdocgen-uploads/08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx
api-1  | 2025-07-24 20:29:35,692 INFO sqlalchemy.engine.Engine UPDATE documents SET file_path=$1::VARCHAR, status=$2::documentstatus WHERE documents.id = $3::UUID
api-1  | 2025-07-24 20:29:35,692 - sqlalchemy.engine.Engine - INFO - UPDATE documents SET file_path=$1::VARCHAR, status=$2::documentstatus WHERE documents.id = $3::UUID
api-1  | 2025-07-24 20:29:35,692 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ('netdocgen-uploads/08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx', 'PARSING', UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'))
api-1  | 2025-07-24 20:29:35,692 - sqlalchemy.engine.Engine - INFO - [generated in 0.00009s] ('netdocgen-uploads/08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx', 'PARSING', UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'))
api-1  | 2025-07-24 20:29:35,696 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:29:35,696 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:29:35,698 - app.services.message_queue - INFO - Publishing parse request for document 08a8f790-ffa1-429a-8aae-616dde9d5976
api-1  | 2025-07-24 20:29:35,698 - app.services.message_queue - DEBUG - File path: netdocgen-uploads/08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx, Project ID: 5ac5b233-265f-4a89-aafa-c54a2bb010a9
api-1  | 2025-07-24 20:29:35,698 - app.services.message_queue - DEBUG - Publishing message: {'document_id': '08a8f790-ffa1-429a-8aae-616dde9d5976', 'file_path': 'netdocgen-uploads/08a8f790-ffa1-429a-8aae-616dde9d5976.vsdx', 'project_id': '5ac5b233-265f-4a89-aafa-c54a2bb010a9'}
api-1  | 2025-07-24 20:29:35,707 - shared.messaging.queue - INFO - Published message to document.parse.visio
api-1  | 2025-07-24 20:29:35,707 - app.services.message_queue - INFO - Parse request published successfully for document 08a8f790-ffa1-429a-8aae-616dde9d5976
api-1  | 2025-07-24 20:29:35,707 - app.services.document - INFO - Document upload completed successfully: 08a8f790-ffa1-429a-8aae-616dde9d5976
api-1  | 2025-07-24 20:29:35,707 - app.routers.documents - INFO - Upload successful. Document ID: 08a8f790-ffa1-429a-8aae-616dde9d5976, Status: DocumentStatus.PARSING
api-1  | INFO:     192.168.65.1:30997 - "POST /api/documents/upload?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:36,925 - app.services.message_queue - INFO - Received parse complete message for document 08a8f790-ffa1-429a-8aae-616dde9d5976
api-1  | 2025-07-24 20:29:36,926 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:36,926 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:36,927 INFO sqlalchemy.engine.Engine UPDATE documents SET status=$1::documentstatus, parsed_data_path=$2::VARCHAR, shape_count=$3::INTEGER, connection_count=$4::INTEGER, page_count=$5::INTEGER, parsed_at=$6::TIMESTAMP WITH TIME ZONE WHERE documents.id = $7::UUID
api-1  | 2025-07-24 20:29:36,927 - sqlalchemy.engine.Engine - INFO - UPDATE documents SET status=$1::documentstatus, parsed_data_path=$2::VARCHAR, shape_count=$3::INTEGER, connection_count=$4::INTEGER, page_count=$5::INTEGER, parsed_at=$6::TIMESTAMP WITH TIME ZONE WHERE documents.id = $7::UUID
api-1  | 2025-07-24 20:29:36,927 INFO sqlalchemy.engine.Engine [generated in 0.00008s] ('PARSED', None, 0, 0, 15, datetime.datetime(2025, 7, 24, 20, 29, 36, 925426), UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'))
api-1  | 2025-07-24 20:29:36,927 - sqlalchemy.engine.Engine - INFO - [generated in 0.00008s] ('PARSED', None, 0, 0, 15, datetime.datetime(2025, 7, 24, 20, 29, 36, 925426), UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'))
api-1  | 2025-07-24 20:29:36,928 INFO sqlalchemy.engine.Engine COMMIT
api-1  | 2025-07-24 20:29:36,928 - sqlalchemy.engine.Engine - INFO - COMMIT
api-1  | 2025-07-24 20:29:36,932 - app.services.message_queue - INFO - Updated document 08a8f790-ffa1-429a-8aae-616dde9d5976 after parsing
api-1  | INFO:     192.168.65.1:30997 - "OPTIONS /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:37,763 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,763 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,764 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,764 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,764 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,764 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:43852 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:43852 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:37,782 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,782 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,782 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,782 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,782 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,782 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,784 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:37,784 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:37,784 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:37,784 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:37,792 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:37,792 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,792 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:37,792 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:30997 - "GET /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:37,798 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:37,798 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:37,799 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:37,799 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:37,799 INFO sqlalchemy.engine.Engine [cached since 173.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:37,799 - sqlalchemy.engine.Engine - INFO - [cached since 173.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:37,801 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,801 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,801 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,801 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,802 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,802 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,804 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:37,804 INFO sqlalchemy.engine.Engine [cached since 197.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:37,804 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:37,804 - sqlalchemy.engine.Engine - INFO - [cached since 197.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:37,804 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:37,804 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:37,807 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:37,807 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:37,807 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:37,807 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:38965 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:30997 - "GET /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:37,816 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:37,816 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:37,819 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,819 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:37,820 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,820 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:37,820 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,820 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,823 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:37,823 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:37,823 - sqlalchemy.engine.Engine - INFO - [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,823 INFO sqlalchemy.engine.Engine [cached since 197.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:37,825 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:37,825 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:37,825 - sqlalchemy.engine.Engine - INFO - [cached since 173.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:37,825 INFO sqlalchemy.engine.Engine [cached since 173.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:37,828 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:37,828 - sqlalchemy.engine.Engine - INFO - [cached since 197.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:37,828 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:37,828 INFO sqlalchemy.engine.Engine [cached since 197.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:37,828 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:37,828 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:43852 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:43145 - "OPTIONS /api/documents HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:43145 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | INFO:     192.168.65.1:18027 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:26900 - "OPTIONS /api/documents HTTP/1.1" 200 OK
api-1  | INFO:     192.168.65.1:18027 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:41,268 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:41,268 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:41,268 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:41,268 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:41,269 INFO sqlalchemy.engine.Engine [cached since 201.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,269 - sqlalchemy.engine.Engine - INFO - [cached since 201.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:32201 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:41,274 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:41,274 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:41,275 INFO sqlalchemy.engine.Engine [cached since 201.3s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,275 - sqlalchemy.engine.Engine - INFO - [cached since 201.3s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,276 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:41,277 INFO sqlalchemy.engine.Engine [cached since 177.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:41,276 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:41,277 - sqlalchemy.engine.Engine - INFO - [cached since 177.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:41,278 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:41,278 - sqlalchemy.engine.Engine - INFO - [cached since 201.3s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:41,278 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:41,278 INFO sqlalchemy.engine.Engine [cached since 201.3s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:41,279 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:41,279 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:43145 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:41,283 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:41,283 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:41,283 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:41,283 INFO sqlalchemy.engine.Engine [cached since 201.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,283 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:41,283 - sqlalchemy.engine.Engine - INFO - [cached since 201.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,284 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:41,284 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:41,284 - sqlalchemy.engine.Engine - INFO - [cached since 201.3s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,284 INFO sqlalchemy.engine.Engine [cached since 201.3s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:41,284 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:41,284 INFO sqlalchemy.engine.Engine [cached since 177.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:41,284 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:41,284 - sqlalchemy.engine.Engine - INFO - [cached since 177.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:41,285 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:41,285 INFO sqlalchemy.engine.Engine [cached since 201.3s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:41,285 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:41,285 - sqlalchemy.engine.Engine - INFO - [cached since 201.3s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:41,285 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:41,285 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:32201 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:24257 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:47047 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | INFO:     192.168.65.1:24257 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:47047 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:45,414 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:45,414 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:45,415 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:45,415 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:45,415 INFO sqlalchemy.engine.Engine [cached since 205.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,415 - sqlalchemy.engine.Engine - INFO - [cached since 205.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,422 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:45,422 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:45,422 INFO sqlalchemy.engine.Engine [cached since 205.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,422 - sqlalchemy.engine.Engine - INFO - [cached since 205.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,423 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:45,423 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:45,423 INFO sqlalchemy.engine.Engine [cached since 181.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:45,423 - sqlalchemy.engine.Engine - INFO - [cached since 181.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:45,425 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | 2025-07-24 20:29:45,425 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:45,425 INFO sqlalchemy.engine.Engine [cached since 205.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:45,425 - sqlalchemy.engine.Engine - INFO - [cached since 205.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:45,425 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:45,425 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:37551 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:45,444 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:45,444 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:45,445 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:45,445 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:45,445 INFO sqlalchemy.engine.Engine [cached since 205.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,445 - sqlalchemy.engine.Engine - INFO - [cached since 205.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,448 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:45,448 INFO sqlalchemy.engine.Engine [cached since 205.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,448 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:45,448 - sqlalchemy.engine.Engine - INFO - [cached since 205.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:45,449 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  | 2025-07-24 20:29:45,449 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:45,449 INFO sqlalchemy.engine.Engine [cached since 181.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:45,449 - sqlalchemy.engine.Engine - INFO - [cached since 181.6s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:45,450 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:45,450 - sqlalchemy.engine.Engine - INFO - [cached since 205.5s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:45,450 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:45,450 INFO sqlalchemy.engine.Engine [cached since 205.5s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:45,451 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:45,451 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:47047 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:48,784 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,784 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,785 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,785 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,785 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,785 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:61347 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:48,794 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:48,794 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:48,794 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:48,794 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:61347 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:48,798 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,798 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,798 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,798 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,799 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,799 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:24257 - "GET /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:48,804 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:48,804 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:48,807 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,807 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,807 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,807 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,807 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,807 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,812 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:48,812 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:48,812 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,812 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,815 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:48,815 - sqlalchemy.engine.Engine - INFO - [cached since 184.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:48,815 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:48,815 INFO sqlalchemy.engine.Engine [cached since 184.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:48,815 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:48,815 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:48,815 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:48,815 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:48,817 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:48,817 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:48,817 INFO sqlalchemy.engine.Engine [cached since 208.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:48,817 - sqlalchemy.engine.Engine - INFO - [cached since 208.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:48,817 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:48,817 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:24257 - "GET /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:48,818 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:48,818 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:62285 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:48,824 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,824 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:48,825 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,825 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,825 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:48,825 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,828 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:48,828 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:48,828 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,828 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:48,829 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:48,829 INFO sqlalchemy.engine.Engine [cached since 184.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:48,829 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:48,829 - sqlalchemy.engine.Engine - INFO - [cached since 184.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:48,830 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:48,830 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:48,831 INFO sqlalchemy.engine.Engine [cached since 208.9s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:48,831 - sqlalchemy.engine.Engine - INFO - [cached since 208.9s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:48,831 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:48,831 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:24257 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:55833 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:51,837 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:51,837 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:51,843 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:51,843 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:51,843 - sqlalchemy.engine.Engine - INFO - [cached since 212s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:51,843 INFO sqlalchemy.engine.Engine [cached since 212s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:51,851 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:51,851 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:51,851 INFO sqlalchemy.engine.Engine [cached since 22.36s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:51,851 - sqlalchemy.engine.Engine - INFO - [cached since 22.36s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:55833 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:51,856 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:51,856 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:51,856 - sqlalchemy.engine.Engine - INFO - [cached since 22.34s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:51,856 INFO sqlalchemy.engine.Engine [cached since 22.34s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:64651 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:51,860 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:51,860 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:51,862 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:51,862 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:51,863 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:51,863 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:51,863 INFO sqlalchemy.engine.Engine [cached since 212s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:51,863 - sqlalchemy.engine.Engine - INFO - [cached since 212s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:51,865 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:51,865 INFO sqlalchemy.engine.Engine [cached since 22.38s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:51,865 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:51,865 - sqlalchemy.engine.Engine - INFO - [cached since 22.38s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:51,866 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:51,866 INFO sqlalchemy.engine.Engine [cached since 22.35s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:51,866 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:29:51,866 - sqlalchemy.engine.Engine - INFO - [cached since 22.35s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:64651 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:51,868 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:51,868 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:26804 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:38472 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | INFO:     192.168.65.1:26804 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:38472 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:29:55,867 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:55,867 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:55,868 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:55,868 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:55,869 INFO sqlalchemy.engine.Engine [cached since 216s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,869 - sqlalchemy.engine.Engine - INFO - [cached since 216s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,873 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:55,873 INFO sqlalchemy.engine.Engine [cached since 215.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,873 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:55,873 - sqlalchemy.engine.Engine - INFO - [cached since 215.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,874 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:55,874 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:55,874 - sqlalchemy.engine.Engine - INFO - [cached since 192s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:55,874 INFO sqlalchemy.engine.Engine [cached since 192s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:55,875 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:55,875 - sqlalchemy.engine.Engine - INFO - [cached since 215.9s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:55,875 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:55,875 INFO sqlalchemy.engine.Engine [cached since 215.9s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:55,875 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:55,875 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:26696 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:55,880 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:55,880 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:55,880 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:55,880 INFO sqlalchemy.engine.Engine [cached since 216s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,880 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:55,880 - sqlalchemy.engine.Engine - INFO - [cached since 216s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,882 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:55,882 INFO sqlalchemy.engine.Engine [cached since 215.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,882 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:55,882 - sqlalchemy.engine.Engine - INFO - [cached since 215.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:55,883 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:55,883 INFO sqlalchemy.engine.Engine [cached since 192s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:55,883 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:55,883 - sqlalchemy.engine.Engine - INFO - [cached since 192s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:55,883 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:55,883 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:55,884 - sqlalchemy.engine.Engine - INFO - [cached since 215.9s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:55,884 INFO sqlalchemy.engine.Engine [cached since 215.9s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:55,884 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:55,884 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | INFO:     192.168.65.1:38472 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:26804 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:26804 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:56,709 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:56,709 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:56,710 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:56,710 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:56,710 - sqlalchemy.engine.Engine - INFO - [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,710 INFO sqlalchemy.engine.Engine [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,717 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:56,717 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:56,717 - sqlalchemy.engine.Engine - INFO - [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,717 INFO sqlalchemy.engine.Engine [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,720 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:56,720 INFO sqlalchemy.engine.Engine [cached since 192.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:56,720 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:56,720 - sqlalchemy.engine.Engine - INFO - [cached since 192.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:56,723 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:56,723 - sqlalchemy.engine.Engine - INFO - [cached since 216.7s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:56,723 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:56,723 INFO sqlalchemy.engine.Engine [cached since 216.7s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:56,723 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:56,723 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:51604 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:56,731 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:56,731 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:56,731 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:56,731 INFO sqlalchemy.engine.Engine [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,731 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:56,731 - sqlalchemy.engine.Engine - INFO - [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,733 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:56,733 - sqlalchemy.engine.Engine - INFO - [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,733 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:56,733 INFO sqlalchemy.engine.Engine [cached since 216.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:56,735 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | 2025-07-24 20:29:56,735 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:56,735 - sqlalchemy.engine.Engine - INFO - [cached since 192.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:56,735 INFO sqlalchemy.engine.Engine [cached since 192.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:56,736 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:56,736 - sqlalchemy.engine.Engine - INFO - [cached since 216.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:56,736 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:56,736 INFO sqlalchemy.engine.Engine [cached since 216.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:56,736 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:56,736 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:26804 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:29081 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | INFO:     192.168.65.1:16700 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | INFO:     192.168.65.1:29081 - "GET /api/documents HTTP/1.1" 404 Not Found
api-1  | INFO:     192.168.65.1:16700 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:57,366 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:57,366 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:57,366 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:57,366 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:57,366 INFO sqlalchemy.engine.Engine [cached since 217.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,366 - sqlalchemy.engine.Engine - INFO - [cached since 217.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,368 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:57,368 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:57,368 INFO sqlalchemy.engine.Engine [cached since 217.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,368 - sqlalchemy.engine.Engine - INFO - [cached since 217.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,369 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:57,369 - sqlalchemy.engine.Engine - INFO - [cached since 193.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:57,369 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:57,369 INFO sqlalchemy.engine.Engine [cached since 193.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:57,371 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:57,371 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:57,371 INFO sqlalchemy.engine.Engine [cached since 217.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:57,371 - sqlalchemy.engine.Engine - INFO - [cached since 217.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:57,371 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:57,371 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:50057 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:57,380 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:57,380 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:57,381 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:57,381 INFO sqlalchemy.engine.Engine [cached since 217.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,381 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:57,381 - sqlalchemy.engine.Engine - INFO - [cached since 217.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,386 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:57,386 INFO sqlalchemy.engine.Engine [cached since 217.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,386 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:57,386 - sqlalchemy.engine.Engine - INFO - [cached since 217.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:57,389 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:57,390 INFO sqlalchemy.engine.Engine [cached since 193.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:57,389 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:57,390 - sqlalchemy.engine.Engine - INFO - [cached since 193.5s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:57,395 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:57,395 - sqlalchemy.engine.Engine - INFO - [cached since 217.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:57,395 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:57,395 INFO sqlalchemy.engine.Engine [cached since 217.4s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:57,396 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:57,396 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:16700 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:29:58,730 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,730 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,730 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,730 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,730 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,730 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:28805 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:58,736 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:58,736 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:58,736 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:58,736 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:28805 - "GET /api/projects HTTP/1.1" 307 Temporary Redirect
api-1  | 2025-07-24 20:29:58,740 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,740 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,740 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,740 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,740 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,740 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:29081 - "GET /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:58,743 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:58,743 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:58,746 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:58,746 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:58,746 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,746 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,748 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,748 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,748 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,748 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,748 INFO sqlalchemy.engine.Engine [cached since 218.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,748 - sqlalchemy.engine.Engine - INFO - [cached since 218.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,750 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:58,750 INFO sqlalchemy.engine.Engine [cached since 194.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:58,750 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:58,750 - sqlalchemy.engine.Engine - INFO - [cached since 194.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:58,751 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:58,751 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:58,751 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:58,751 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:58,751 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:58,751 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:58,752 - sqlalchemy.engine.Engine - INFO - SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:58,752 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:29:58,752 INFO sqlalchemy.engine.Engine SELECT documents.id, documents.project_id, documents.filename, documents.original_filename, documents.file_path, documents.file_size, documents.content_type, documents.status, documents.error_message, documents.parsed_data_path, documents.shape_count, documents.connection_count, documents.page_count, documents.generated_files, documents.uploaded_by, documents.uploaded_at, documents.parsed_at, documents.completed_at, documents.ai_analysis_completed 
api-1  | FROM documents JOIN projects ON projects.id = documents.project_id 
api-1  | WHERE documents.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:29:58,752 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('08a8f790-ffa1-429a-8aae-616dde9d5976'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:44429 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | INFO:     192.168.65.1:29081 - "GET /api/documents/08a8f790-ffa1-429a-8aae-616dde9d5976 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:29:58,756 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:58,756 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:29:58,757 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,757 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:29:58,757 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,757 - sqlalchemy.engine.Engine - INFO - [cached since 218.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,757 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:29:58,757 INFO sqlalchemy.engine.Engine [cached since 218.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,759 - sqlalchemy.engine.Engine - INFO - SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:58,759 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,759 INFO sqlalchemy.engine.Engine SELECT count(*) AS count_1 
api-1  | FROM (SELECT projects.id AS id, projects.name AS name, projects.description AS description, projects.status AS status, projects.owner_id AS owner_id, projects.created_at AS created_at, projects.updated_at AS updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID) AS anon_1
api-1  | 2025-07-24 20:29:58,759 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:29:58,759 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:58,759 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.owner_id = $1::UUID ORDER BY projects.created_at DESC 
api-1  |  LIMIT $2::INTEGER OFFSET $3::INTEGER
api-1  | 2025-07-24 20:29:58,759 INFO sqlalchemy.engine.Engine [cached since 194.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:58,759 - sqlalchemy.engine.Engine - INFO - [cached since 194.9s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'), 20, 0)
api-1  | 2025-07-24 20:29:58,760 INFO sqlalchemy.engine.Engine SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:58,760 INFO sqlalchemy.engine.Engine [cached since 218.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:58,760 - sqlalchemy.engine.Engine - INFO - SELECT documents.id AS documents_id, documents.project_id AS documents_project_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE $1::UUID = documents.project_id
api-1  | 2025-07-24 20:29:58,760 - sqlalchemy.engine.Engine - INFO - [cached since 218.8s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:29:58,760 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:29:58,760 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:28805 - "GET /api/projects/ HTTP/1.1" 500 Internal Server Error
api-1  | ERROR:    Exception in ASGI application
api-1  | Traceback (most recent call last):
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi
api-1  |     result = await app(  # type: ignore[func-returns-value]
api-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__
api-1  |     return await self.app(scope, receive, send)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/applications.py", line 1106, in __call__
api-1  |     await super().__call__(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/applications.py", line 122, in __call__
api-1  |     await self.middleware_stack(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 184, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 162, in __call__
api-1  |     await self.app(scope, receive, _send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 91, in __call__
api-1  |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 146, in simple_response
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
api-1  |     raise exc
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
api-1  |     await self.app(scope, receive, sender)
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 20, in __call__
api-1  |     raise e
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 17, in __call__
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__
api-1  |     await route.handle(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 276, in handle
api-1  |     await self.app(scope, receive, send)
api-1  |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 66, in app
api-1  |     response = await func(request)
api-1  |                ^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 274, in app
api-1  |     raw_response = await run_endpoint_function(
api-1  |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/fastapi/routing.py", line 191, in run_endpoint_function
api-1  |     return await dependant.call(**values)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/app/app/routers/projects.py", line 41, in list_projects
api-1  |     document_count=len(project.documents) if project.documents else 0,
api-1  |                                              ^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 566, in __get__
api-1  |     return self.impl.get(state, dict_)  # type: ignore[no-any-return]
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1086, in get
api-1  |     value = self._fire_loader_callables(state, key, passive)
api-1  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/attributes.py", line 1121, in _fire_loader_callables
api-1  |     return self.callable_(state, passive)
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 967, in _load_for_state
api-1  |     return self._emit_lazyload(
api-1  |            ^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/strategies.py", line 1130, in _emit_lazyload
api-1  |     result = session.execute(
api-1  |              ^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
api-1  |     return self._execute_internal(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
api-1  |     result: Result[Any] = compile_state_cls.orm_execute_statement(
api-1  |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
api-1  |     result = conn.execute(
api-1  |              ^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
api-1  |     return meth(
api-1  |            ^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
api-1  |     return connection._execute_clauseelement(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
api-1  |     ret = self._execute_context(
api-1  |           ^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
api-1  |     return self._exec_single_context(
api-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
api-1  |     self._handle_dbapi_exception(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2346, in _handle_dbapi_exception
api-1  |     raise exc_info[1].with_traceback(exc_info[2])
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
api-1  |     self.dialect.do_execute(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
api-1  |     cursor.execute(statement, parameters)
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/dialects/postgresql/asyncpg.py", line 591, in execute
api-1  |     self._adapt_connection.await_(
api-1  |   File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 116, in await_only
api-1  |     raise exc.MissingGreenlet(
api-1  | sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
api-1  | 2025-07-24 20:30:01,037 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:30:01,037 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:30:01,039 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:01,039 INFO sqlalchemy.engine.Engine [cached since 221.1s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:30:01,039 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:01,039 - sqlalchemy.engine.Engine - INFO - [cached since 221.1s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:17209 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:30:01,052 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:01,052 INFO sqlalchemy.engine.Engine [cached since 31.56s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:01,052 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:01,052 - sqlalchemy.engine.Engine - INFO - [cached since 31.56s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | INFO:     192.168.65.1:17209 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:30:01,056 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:01,056 - sqlalchemy.engine.Engine - INFO - [cached since 31.54s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:30:01,056 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:01,056 INFO sqlalchemy.engine.Engine [cached since 31.54s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:62731 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:30:01,059 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:30:01,059 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:30:01,061 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:30:01,061 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:30:01,061 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:01,061 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:01,061 - sqlalchemy.engine.Engine - INFO - [cached since 221.2s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:30:01,061 INFO sqlalchemy.engine.Engine [cached since 221.2s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:30:01,062 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:01,063 - sqlalchemy.engine.Engine - INFO - [cached since 31.57s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:01,062 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:01,063 INFO sqlalchemy.engine.Engine [cached since 31.57s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:01,063 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:01,063 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:01,063 INFO sqlalchemy.engine.Engine [cached since 31.55s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:30:01,063 - sqlalchemy.engine.Engine - INFO - [cached since 31.55s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:62731 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:30:01,064 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:30:01,064 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | INFO:     192.168.65.1:42134 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:30:05,294 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:30:05,294 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:30:05,294 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:05,294 - sqlalchemy.engine.Engine - INFO - [cached since 225.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:30:05,294 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:05,294 INFO sqlalchemy.engine.Engine [cached since 225.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | INFO:     192.168.65.1:42134 - "GET /api/documents?project_id=5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 404 Not Found
api-1  | 2025-07-24 20:30:05,297 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:05,297 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:05,297 INFO sqlalchemy.engine.Engine [cached since 35.81s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:05,297 - sqlalchemy.engine.Engine - INFO - [cached since 35.81s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:05,298 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:05,299 - sqlalchemy.engine.Engine - INFO - [cached since 35.79s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:30:05,298 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:05,299 INFO sqlalchemy.engine.Engine [cached since 35.79s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:49184 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:30:05,300 - sqlalchemy.engine.Engine - INFO - ROLLBACK
api-1  | 2025-07-24 20:30:05,300 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:30:05,302 INFO sqlalchemy.engine.Engine BEGIN (implicit)
api-1  | 2025-07-24 20:30:05,302 - sqlalchemy.engine.Engine - INFO - BEGIN (implicit)
api-1  | 2025-07-24 20:30:05,303 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:05,303 INFO sqlalchemy.engine.Engine [cached since 225.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:30:05,303 - sqlalchemy.engine.Engine - INFO - SELECT users.id, users.username, users.email, users.hashed_password, users.full_name, users.is_active, users.is_admin, users.created_at, users.updated_at 
api-1  | FROM users 
api-1  | WHERE users.id = $1::UUID
api-1  | 2025-07-24 20:30:05,303 - sqlalchemy.engine.Engine - INFO - [cached since 225.4s ago] (UUID('4370f178-0e62-4eec-aada-fe76a4382961'),)
api-1  | 2025-07-24 20:30:05,305 - sqlalchemy.engine.Engine - INFO - SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:05,305 - sqlalchemy.engine.Engine - INFO - [cached since 35.82s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:05,305 INFO sqlalchemy.engine.Engine SELECT projects.id, projects.name, projects.description, projects.status, projects.owner_id, projects.created_at, projects.updated_at 
api-1  | FROM projects 
api-1  | WHERE projects.id = $1::UUID AND projects.owner_id = $2::UUID
api-1  | 2025-07-24 20:30:05,305 INFO sqlalchemy.engine.Engine [cached since 35.82s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'), UUID('4370f178-0e62-4eec-aada-fe76a4382961'))
api-1  | 2025-07-24 20:30:05,306 INFO sqlalchemy.engine.Engine SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:05,306 INFO sqlalchemy.engine.Engine [cached since 35.79s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | 2025-07-24 20:30:05,306 - sqlalchemy.engine.Engine - INFO - SELECT documents.project_id AS documents_project_id, documents.id AS documents_id, documents.filename AS documents_filename, documents.original_filename AS documents_original_filename, documents.file_path AS documents_file_path, documents.file_size AS documents_file_size, documents.content_type AS documents_content_type, documents.status AS documents_status, documents.error_message AS documents_error_message, documents.parsed_data_path AS documents_parsed_data_path, documents.shape_count AS documents_shape_count, documents.connection_count AS documents_connection_count, documents.page_count AS documents_page_count, documents.generated_files AS documents_generated_files, documents.uploaded_by AS documents_uploaded_by, documents.uploaded_at AS documents_uploaded_at, documents.parsed_at AS documents_parsed_at, documents.completed_at AS documents_completed_at, documents.ai_analysis_completed AS documents_ai_analysis_completed 
api-1  | FROM documents 
api-1  | WHERE documents.project_id IN ($1::UUID)
api-1  | 2025-07-24 20:30:05,306 - sqlalchemy.engine.Engine - INFO - [cached since 35.79s ago] (UUID('5ac5b233-265f-4a89-aafa-c54a2bb010a9'),)
api-1  | INFO:     192.168.65.1:49184 - "GET /api/projects/5ac5b233-265f-4a89-aafa-c54a2bb010a9 HTTP/1.1" 200 OK
api-1  | 2025-07-24 20:30:05,307 INFO sqlalchemy.engine.Engine ROLLBACK
api-1  | 2025-07-24 20:30:05,307 - sqlalchemy.engine.Engine - INFO - ROLLBACK

api-1  | INFO:     192.168.65.1:33568 - "GET /api/documents/debug/connectivity HTTP/1.1" 401 Unauthorized

