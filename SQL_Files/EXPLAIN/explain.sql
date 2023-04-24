-- Deux grosses tables
EXPLAIN SELECT S.* FROM STATSCOMANNEE S, COMMUNE C
WHERE S.IDCOM = C.CCOM;

--  Hash Join  (cost=1174.26..5360.97 rows=209556 width=26)
--    Hash Cond: ((s.idcom)::text = (c.ccom)::text)
--    ->  Seq Scan on statscomannee s  (cost=0.00..3636.56 rows=209556 width=26)
--    ->  Hash  (cost=737.45..737.45 rows=34945 width=6)
--          ->  Seq Scan on commune c  (cost=0.00..737.45 rows=34945 width=6)


-- Une petite et une grande table
EXPLAIN SELECT CO.LIBELLE FROM CLREG C, COMMUNE CO
WHERE C.CCOM = CO.CCOM;

--  Hash Join  (cost=1174.26..1202.57 rows=1450 width=13)
--    Hash Cond: ((c.ccom)::text = (co.ccom)::text)
--    ->  Seq Scan on clreg c  (cost=0.00..24.50 rows=1450 width=24)
--    ->  Hash  (cost=737.45..737.45 rows=34945 width=19)
        --  ->  Seq Scan on commune co  (cost=0.00..737.45 rows=34945 width=19)


-- Deux petites tables
EXPLAIN SELECT * FROM REG_POP P, REGION R
WHERE P.habitants = 384239
AND P.IDSTAT = 'P19_POP'
AND P.IDREG = R.CREG;

--  Nested Loop  (cost=0.14..10.50 rows=1 width=1282)
--    ->  Seq Scan on reg_pop p  (cost=0.00..2.08 rows=1 width=20)
--          Filter: ((habitants = '384239'::double precision) AND ((idstat)::text = 'P19_POP'::text))
--    ->  Index Scan using cle_region on region r  (cost=0.14..8.16 rows=1 width=1262)
--          Index Cond: (creg = p.idreg)

