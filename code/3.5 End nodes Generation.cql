##Generating End nodes.csv
with "MATCH p=(a:node)-[:HAS_CHILD*]->(b:node)
WHERE NOT (b)-[:HAS_CHILD]->(:node)
return distinct b.id as tax_id, b.rank as rank" AS query 
call apoc.export.csv.query(query, "endnode.csv", {})
yield file,source,format, nodes, relationships,properties
return file,source,format, nodes, relationships,properties;