DROP TABLE IF EXISTS Posts;
CREATE TABLE Posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT,
    dacanc TEXT
);
INSERT INTO Posts (titolo, info, dacanc) VALUES (
    'Primo post',
    'Dettaglio Post',
    'prova'

);
INSERT INTO Posts (titolo, info) VALUES (
    'Secondo post',
    'Dettaglio Post'

);
INSERT INTO Posts (titolo, info) VALUES (
    'Terzo post',
    'Dettaglio Post'
);