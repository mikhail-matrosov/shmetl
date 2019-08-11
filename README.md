# Shmetl
Versioned ETL pipelines - a platform to author, schedule and monitor data
processing workflows.

This project is in a **very early development stage!**

Shmetl is a long running service, that keeps track of all your code and data
history. It handles dependency resolution, workflow management, failures, etc.

## Planned features
- Function versions and tags
- Data tags
- Call on aggregates (e.g. call `f` for each group of items with the same
  attribute value)
- Real-time and batch processing
- Preview results of pipeline execution (e.g. what will be `f(g(x))` for my
  `x`)
- Current state is always accessible as an SQL table
- Web UI for visualizing computational graph and exectution statistics
- Integration with Kubernetes
- Pruning old data

Shmetl is written in Python and relies on external relational DB to store its
data. By default it's a built-in sqlite3, but you can use any DB of your
choice.

## TODO: Comparison to related projects
- Shmetl vs Airflow
- Shemtl vs Apache ETL
- Shmetl vs Luigi
- Shmetl vs Bonobo