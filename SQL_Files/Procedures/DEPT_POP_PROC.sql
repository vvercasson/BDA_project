
CREATE OR REPLACE PROCEDURE update_dept_pop19()
LANGUAGE SQL
AS $$
    UPDATE DEPARTEMENT D
    SET population_2019 = (
        SELECT SUM(S.VALEUR) as habitants FROM COMMUNE C, STATSCOMANNEE S, STATS T 
        WHERE D.CDEPT = C.CDEPT 
        AND C.CCOM = S.IDCOM 
        AND T.IDSTAT = 'P19_POP'
        AND S.IDSTAT = T.IDSTAT 
    );
$$;

CALL update_dept_pop19();