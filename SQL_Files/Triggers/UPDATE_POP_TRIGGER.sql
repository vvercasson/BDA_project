CREATE OR REPLACE FUNCTION refresh_pop_on_both_tables()
RETURNS TRIGGER AS $$
        DECLARE totalNewPop INTEGER;
        DECLARE totalPrevPop INTEGER;
        BEGIN
            IF NOT EXISTS(SELECT idcom FROM statscomannee where idstat = new.idstat and valeur is null) THEN
                totalNewPop := (SELECT COUNT(idstat)
                FROM statscomannee
                WHERE idstat = new.idstat);

                totalPrevPop := (SELECT COUNT(idstat)
                FROM statscomannee
                WHERE idstat = 'P13_POP');

                IF (totalNewPop = totalPrevPop) THEN
                    CALL update_dept_pop19();
                    CALL update_reg_pop19();
                END IF;
            END IF;
            RETURN NEW;
        END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_population_on_statsAnnee_update AFTER UPDATE OR INSERT ON STATSCOMANNEE
FOR EACH ROW
WHEN (new.idstat LIKE '%POP%')
EXECUTE FUNCTION refresh_pop_on_both_tables();
