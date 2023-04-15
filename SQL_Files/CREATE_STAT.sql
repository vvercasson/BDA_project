-- PARTIE STAT

CREATE TABLE STATS(
    idStat varchar(15) constraint cle_stat PRIMARY KEY,
    label varchar(30) constraint stat_label_non_null not null
);

CREATE TABLE ANNEE(
    idAnnee integer constraint cle_annee PRIMARY KEY,
    annee integer constraint annee_not_null not null
);

CREATE TABLE INTERVALLE(
    idInter integer constraint cle_intervalle PRIMARY KEY,
    debut integer not null,
    fin integer not null,
    constraint debut_inf_fin CHECK (fin > debut)
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
    constraint fk_annee
        FOREIGN KEY(idAnnee)
            REFERENCES ANNEE(idAnnee),
    constraint fk_stat
        FOREIGN KEY(idStat)
            REFERENCES STATS(idStat)
);

CREATE TABLE STATSCOMINTER(
    idCom varchar(5),
    idInter integer,
    idStat varchar(15),
    valeur float,
    PRIMARY KEY(idCom, idInter, idStat),
    constraint fk_com
        FOREIGN KEY(idCom)
            REFERENCES COMMUNE(CCom),
    constraint fk_annee
        FOREIGN KEY(idInter)
            REFERENCES INTERVALLE(idInter),
    constraint fk_stat
        FOREIGN KEY(idStat)
            REFERENCES STATS(idStat)
);