CREATE TABLE REGION(
    CReg integer constraint cle_region PRIMARY KEY,
    TNCC integer,
    NCC varchar(200) not null,
    NCCENR varchar(200) not null,
    LIBELLE varchar(200) not null
);

CREATE TABLE DEPARTEMENT(
    CDept varchar(2) constraint cle_dept PRIMARY KEY,
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
    CDept varchar(2),
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
    CDept varchar(2),
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
)