FROM mysql:8.0
WORKDIR /app
COPY init.sql /app/
CMD ["mysqld", "--init-file=/app/init.sql"]