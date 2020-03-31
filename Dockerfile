FROM mysql
COPY init.sql /docker-entrypoint-initdb.d
COPY stored_procedures.sql /docker-entrypoint-initdb.d