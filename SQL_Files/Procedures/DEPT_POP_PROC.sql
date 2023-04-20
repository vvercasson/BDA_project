
CREATE OR REPLACE PROCEDURE update_dept_pop19()
LANGUAGE SQL
AS $$
    UPDATE DEPT_POP D
    SET habitants = (
        SELECT habitants FROM populations_departements
        WHERE IDSTAT = D.IDSTAT
        AND CDEPT = D.IDDEPT
    );
$$;

CALL update_dept_pop19();