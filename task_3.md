If you see that a SQL SELECT query is slow - what would you do to improve it?

1. Use `explain` or `explain analyze` to verify the scanning of the tables. If there is sequential scanning, we can use an index to improve it.
2. Use early filtering. Sometimes, we process an unnecessary amount of information. We can limit the initial dataset and use this to guide subsequent computations.
3. Optimize indexes. Analyze the queries and verify the fields we use to read or retrieve table rows.
4. Refactor the query using subqueries, temporary tables, CTEs, or materialized views.
5. Denormalize some fields using arrays in strings, Array fields, or JSON fields. This is feasible using PostgreSQL.
6. We can cache some results that don´t change frequently and refresh them occasionally.