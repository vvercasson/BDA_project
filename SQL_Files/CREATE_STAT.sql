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