CREATE OR REPLACE PROCEDURE update_reg_pop19()
LANGUAGE SQL
AS $$
    UPDATE REGION R
    SET population_2019 = (
        SELECT SUM(S.VALEUR) as habitants FROM COMMUNE C, STATSCOMANNEE S, STATS T 
        WHERE R.CREG = C.CREG 
        AND C.CCOM = S.IDCOM 
        AND T.IDSTAT = 'P19_POP'
        AND S.IDSTAT = T.IDSTAT 
    );
$$;

CALL update_reg_pop19();