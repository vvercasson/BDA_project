CREATE OR REPLACE PROCEDURE update_reg_pop19()
LANGUAGE SQL
AS $$
    UPDATE REG_POP R
    SET habitants = (
        SELECT habitants FROM populations_regions P
        WHERE IDSTAT = R.IDSTAT
        AND CREG = R.IDREG
    );
$$;

CALL update_reg_pop19();