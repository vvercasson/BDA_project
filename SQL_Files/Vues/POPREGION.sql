CREATE OR REPLACE VIEW populations_regions
AS
    SELECT T.IDSTAT, T.LABEL, R.CREG, SUM(S.VALEUR) as habitants FROM REGION R, COMMUNE C, STATSCOMANNEE S, STATS T 
    WHERE R.CREG = C.CREG 
    AND C.CCOM = S.IDCOM 
    AND T.IDSTAT LIKE '%POP%'
    AND S.IDSTAT = T.IDSTAT 
    GROUP BY(T.IDSTAT, T.LABEL, R.CREG) 
    ORDER BY habitants;