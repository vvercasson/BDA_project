CREATE OR REPLACE FUNCTION refresh_pop_on_both_tables()
RETURNS TRIGGER AS $$
BEGIN
    CALL update_reg_pop19();
    CALL update_dept_pop19();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_population_on_statsAnnee_update
AFTER UPDATE ON STATSCOMANNEE
FOR EACH ROW
WHEN (OLD.valeur IS DISTINCT FROM NEW.valeur AND OLD.IDSTAT = 'P19_POP')
EXECUTE FUNCTION refresh_pop_on_both_tables();

CREATE TRIGGER update_population_on_statsInter_update
AFTER UPDATE ON STATSCOMINTER
FOR EACH ROW
WHEN (OLD.valeur IS DISTINCT FROM NEW.valeur AND OLD.IDSTAT = 'P19_POP')
EXECUTE FUNCTION refresh_pop_on_both_tables();