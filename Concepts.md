ETL - Extract Transform Load
DAG - Directed acyclic graph
Datomic - db
Apache Airflow
Airflow+Versioning?

What is versioning? How to define it?
1. Version is stated in the job description, e.g.
```yaml
processor:
  call:
    235: http://processor-235.svc
    234: http://processor-234.svc
  input:
    scan.image: string
  output:
    cs3: cs3.yaml
```

2. Version is returned with the call result
```
processor:
  call: http://processor.svc
  ...
```

3. Version is fetched from the service meta (e.g. k8s.rs.name or container.tag)

4. Combined - major version is stated, minor is returned with the call result (the most general?)

5. Version is guaranteed by container tag+hash

6. Kubernetes: Detect from container name

7. !!! Kubernetes: Control deployments by itself - becomes a deployment system by itself

---

1. Table of functions

Table functions
columns:
- *function_id
- namespace
- function_name
- version

- selectors
- call
- inputs
- input_format
- group_by
- outputs
- schemas

- trigger
- batching
- backoff_limit
- timeout
- created

Table results
columns:
- *result_id = sha256(output)
- function_id
- input_ids
- data
- created

Table labels
columns:
- result_id
- key
- value
- created


F23A 67BB 14D8 238E  # 64-bit


functions:
| id | function | version | inputs | outputs |
|----|----------|---------|--------|---------|
| 42 | sin      | 1       | [x]    | [y]     |
| 43 | sum      | 4       | [a, b] | [c]     |

data:
| id | function_id | call_id | is_output | key | value |
|----|-------------|---------|-----------|-----|-------|
| 24 | 42          | 17      | 0         | x   | pi/6  |
| 25 | 42          | 17      | 1         | y   | 0.5   |
| 26 | 42          | 18      | 0         | x   | pi/3  |
| 27 | 42          | 18      | 1         | y   | 0.866 |
| 28 | 43          | 19      | 0         | a   | 0.5   |
| 29 | 43          | 19      | 0         | b   | 0.866 |
| 30 | 43          | 19      | 1         | c   | 1.366 |
