CREATE TABLE DEPT_POP (
    idDept varchar(3),
    idStat varchar(15),
    habitants float,
    PRIMARY KEY(idDept, idStat),
    constraint fk_stat
        FOREIGN KEY(idStat)
            REFERENCES STATS(idStat),
    constraint fk_dept
        FOREIGN KEY(idDept)
            REFERENCES DEPARTEMENT(CDept)
);

CREATE TABLE REG_POP (
    idReg integer,
    idStat varchar(15),
    habitants float,
    PRIMARY KEY(idReg, idStat),
    constraint fk_stat
        FOREIGN KEY(idStat)
            REFERENCES STATS(idStat),
    constraint fk_reg
        FOREIGN KEY(idReg)
            REFERENCES REGION(CReg)
);