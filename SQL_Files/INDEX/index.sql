EXPLAIN ANALYZE SELECT * FROM REG_POP P, REGION R
WHERE P.habitants < 500000
AND P.IDSTAT = 'P19_POP'
AND P.IDREG = R.CREG;

-- SANS INDEX
--  Planning Time: 0.121 ms
--  Execution Time: 0.059 ms

CREATE INDEX index_habitants_reg ON REG_POP (habitants);

EXPLAIN SELECT * FROM REG_POP P, REGION R
WHERE P.habitants < 500000
AND P.IDSTAT = 'P19_POP'
AND P.IDREG = R.CREG;

-- AVEC INDEX
--  Planning Time: 0.242 ms
--  Execution Time: 0.048 ms






------------------------------------------------------

EXPLAIN ANALYZE SELECT * FROM DEPT_POP P, DEPARTEMENT D
WHERE habitants < 500000
AND P.IDDEPT = D.CDEPT;

-- SANS INDEX
--  Planning Time: 0.143 ms
--  Execution Time: 0.184 ms


CREATE INDEX index_habitants_dept ON DEPT_POP (habitants);


EXPLAIN ANALYZE SELECT * FROM DEPT_POP P, DEPARTEMENT D
WHERE habitants < 500000
AND P.IDDEPT = D.CDEPT;

-- AVEC INDEX
--  Planning Time: 0.202 ms
--  Execution Time: 0.130 ms


---------------------------------------------------------



EXPLAIN ANALYZE SELECT C.* FROM COMMUNE C, STATSCOMANNEE S
WHERE S.valeur < 5000
AND C.CCOM = S.IDCOM
AND S.IDSTAT = 'P19_POP';

-- SANS INDEX
--  Hash Join  (cost=1174.26..5947.53 rows=33873 width=54) (actual time=8.149..34.369 rows=32746 loops=1)
--    Hash Cond: ((s.idcom)::text = (c.ccom)::text)
--    ->  Seq Scan on statscomannee s  (cost=0.00..4684.34 rows=33873 width=6) (actual time=0.008..18.993 rows=32746 loops=1)
--          Filter: ((valeur < '5000'::double precision) AND ((idstat)::text = 'P19_POP'::text))
--          Rows Removed by Filter: 176810
--    ->  Hash  (cost=737.45..737.45 rows=34945 width=54) (actual time=7.919..7.920 rows=34945 loops=1)
--          Buckets: 65536  Batches: 1  Memory Usage: 3599kB
--          ->  Seq Scan on commune c  (cost=0.00..737.45 rows=34945 width=54) (actual time=0.007..2.787 rows=34945 loops=1)
--  Planning Time: 0.178 ms
--  Execution Time: 35.374 ms


CREATE INDEX index_valeur_statannee ON STATSCOMANNEE (valeur);

EXPLAIN ANALYZE SELECT C.* FROM COMMUNE C, STATSCOMANNEE S
WHERE S.valeur < 5000
AND C.CCOM = S.IDCOM
AND S.IDSTAT = 'P19_POP';

-- AVEC INDEX
--  Hash Join  (cost=1174.26..5947.53 rows=33873 width=54) (actual time=6.362..32.714 rows=32746 loops=1)
--    Hash Cond: ((s.idcom)::text = (c.ccom)::text)
--    ->  Seq Scan on statscomannee s  (cost=0.00..4684.34 rows=33873 width=6) (actual time=0.008..19.135 rows=32746 loops=1)
--          Filter: ((valeur < '5000'::double precision) AND ((idstat)::text = 'P19_POP'::text))
--          Rows Removed by Filter: 176810
--    ->  Hash  (cost=737.45..737.45 rows=34945 width=54) (actual time=6.322..6.323 rows=34945 loops=1)
--          Buckets: 65536  Batches: 1  Memory Usage: 3599kB
--          ->  Seq Scan on commune c  (cost=0.00..737.45 rows=34945 width=54) (actual time=0.003..3.036 rows=34945 loops=1)
--  Planning Time: 0.312 ms
--  Execution Time: 33.529 ms
