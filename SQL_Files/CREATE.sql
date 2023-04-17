CREATE TABLE REGION(
    CReg integer constraint cle_region PRIMARY KEY,
    TNCC integer,
    NCC varchar(200) not null,
    NCCENR varchar(200) not null,
    LIBELLE varchar(200) not null
);

CREATE TABLE DEPARTEMENT(
    CDept varchar(3) constraint cle_dept PRIMARY KEY,
    CReg integer,
    TNCC integer,
    NCC varchar(200) not null,
    NCCENR varchar(200) not null,
    LIBELLE varchar(200) not null,
    constraint fk_reg
        FOREIGN KEY(CReg)
            REFERENCES REGION(CReg)
);

CREATE TABLE COMMUNE(
    CCom varchar(5) constraint cle_com PRIMARY KEY,
    CReg integer,
    CDept varchar(3),
    TNCC integer,
    NCC varchar(200) not null,
    NCCENR varchar(200) not null,
    LIBELLE varchar(200) not null,
    constraint fk_dept
        FOREIGN KEY(CDept)
            REFERENCES DEPARTEMENT(CDept),
    constraint fk_reg
        FOREIGN KEY(CReg)
            REFERENCES REGION(CReg)
);

CREATE TABLE CLDEPT(
    CCom varchar(5),
    CDept varchar(3),
    PRIMARY KEY(CCom, CDept),
    constraint fk_dept
        FOREIGN KEY(CDept)
            REFERENCES DEPARTEMENT(CDept),
    constraint fk_com
        FOREIGN KEY(CCom)
            REFERENCES COMMUNE(CCom)
);

CREATE TABLE CLREG(
    CCom varchar(5),
    CReg integer,
    PRIMARY KEY(CCom, CReg),
    constraint fk_reg
        FOREIGN KEY(CReg)
            REFERENCES REGION(CReg),
    constraint fk_com
        FOREIGN KEY(CCom)
            REFERENCES COMMUNE(CCom)
);

-- PARTIE STAT

CREATE TABLE STATS(
    idStat varchar(15) constraint cle_stat PRIMARY KEY,
    label varchar(100) constraint stat_label_non_null not null
);

CREATE TABLE STATSCOMANNEE(
    idCom varchar(5),
    idAnnee integer,
    idStat varchar(15),
    valeur float,
    PRIMARY KEY(idCom, idAnnee, idStat),
    constraint fk_com
        FOREIGN KEY(idCom)
            REFERENCES COMMUNE(CCom),
    constraint fk_stat
        FOREIGN KEY(idStat)
            REFERENCES STATS(idStat)
);

CREATE TABLE STATSCOMINTER(
    idCom varchar(5),
    debutInter integer,
    finInter integer,
    idStat varchar(15),
    valeur float,
    PRIMARY KEY(idCom, debutInter, finInter, idStat),
    constraint debut_inf_fin CHECK (finInter > debutInter),
    constraint fk_com
        FOREIGN KEY(idCom)
            REFERENCES COMMUNE(CCom),
    constraint fk_stat
        FOREIGN KEY(idStat)
            REFERENCES STATS(idStat)
);