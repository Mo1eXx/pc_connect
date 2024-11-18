CREATE TABLE IF NOT EXISTS person (id uuid PRIMARY KEY, name TEXT);

CREATE TABLE IF NOT EXISTS pc (id uuid PRIMARY KEY, title TEXT);

CREATE TABLE IF NOT EXISTS person_pc (id uuid PRIMARY KEY, pc_id uuid NOT NULL, person_id uuid NOT NULL);

CREATE UNIQUE INDEX IF NOT EXISTS person_pc_idx ON person_pc (pc_id, person_id);

