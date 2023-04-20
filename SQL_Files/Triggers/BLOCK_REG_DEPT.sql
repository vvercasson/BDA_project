CREATE OR REPLACE FUNCTION raise_exception()
RETURNS TRIGGER AS $$
BEGIN    
    -- Lever une exception pour empêcher la modification
    RAISE EXCEPTION 'Modification non autorisée sur la table %', TG_TABLE_NAME;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER empecher_modifications_region
BEFORE INSERT OR UPDATE OR DELETE ON REGION
FOR EACH ROW
EXECUTE FUNCTION raise_exception();

CREATE TRIGGER empecher_modifications_departements
BEFORE INSERT OR UPDATE OR DELETE ON DEPARTEMENT
FOR EACH ROW
EXECUTE FUNCTION raise_exception();