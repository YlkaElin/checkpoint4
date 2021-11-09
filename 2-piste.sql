CREATE TABLE toimipaikka (
    id SERIAL PRIMARY KEY,
    nimi varchar(255) NOT NULL,
    sijainti varchar(255) NOT NULL,
    aloitusvuosi int NOT NULL);

INSERT INTO toimipaikka (nimi, sijainti, aloitusvuosi) VALUES ('Academy Finland', 'Espoo', 2017);
INSERT INTO toimipaikka (nimi, sijainti, aloitusvuosi) VALUES ('Academy Sweden', 'Kista', 2015);
INSERT INTO toimipaikka (nimi, sijainti, aloitusvuosi) VALUES ('Academy Germany', 'Munchen', 2018);

ALTER TABLE astia ADD COLUMN toimipaikka_id INTEGER;

ALTER TABLE astia
ADD CONSTRAINT toimipaikka_if_fk
FOREIGN KEY (toimipaikka_id)
REFERENCES toimipaikka(id);