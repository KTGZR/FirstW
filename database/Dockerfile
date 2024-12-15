FROM postgres:16-alpine
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=postgres
COPY users.sql /docker-entrypoint-initdb.d/