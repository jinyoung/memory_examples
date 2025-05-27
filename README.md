# memory_examples
This repository will have all my explorations related to memory


## Run neo4j using docker
```
docker run --rm -p 7474:7474 -p 7687:7687   -v $PWD/plugins:/plugins   -e NEO4J_dbms_security_procedures_unrestricted=apoc.*   -e NEO4J_dbms_security_procedures_allowlist=apoc.*   -e NEO4J_apoc_import_file_enabled=true   neo4j:5.25.1
```


