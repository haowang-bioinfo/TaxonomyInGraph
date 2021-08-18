## Creating constraint to avoid duplicate node creation
CREATE CONSTRAINT nodeconstraint ON (c:node) ASSERT c.id IS UNIQUE

##Load all the tax_id first
:auto using periodic commit 5000 load csv with headers from 'file:///Neo4j.csv' as row
merge (c:node {id: toInteger(row.tax_id), rank: row.child_rank, scientific_name: row.scientific_name
, common_name: row.common_name})


##Load all the parent tax_id. This should return updation of just one row
:auto using periodic commit load csv with headers from 'file:///Neo4j.csv' 
as row with toInteger(row.`parent tax_id`) as parentId, 
row.parent_rank as parentrank, row.scientific_name as scientific_name, 
row.common_name as common_name
merge (p:node {id: parentId, rank: parentrank, scientific_name: scientific_name
, common_name: common_name})

##Creating one-to-one relationship
:auto using periodic commit 5000 load csv with headers from 
'file:///Neo4j.csv' as row
match (p:node {id:toInteger(row.`parent tax_id`) }), 
(c:node {id: toInteger(row.tax_id)})
merge (p)-[:HAS_CHILD]->(c)
