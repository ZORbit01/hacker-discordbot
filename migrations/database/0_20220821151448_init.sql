-- upgrade --
CREATE TABLE IF NOT EXISTS "member" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "discord_id" BIGINT NOT NULL UNIQUE,
    "username" VARCHAR(255) NOT NULL,
    "is_bot" BOOL NOT NULL  DEFAULT False,
    "created_at" TIMESTAMPTZ,
    "avatar_url" VARCHAR(255),
    "joined_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "discord_id" BIGINT NOT NULL UNIQUE,
    "username" VARCHAR(255) NOT NULL,
    "is_bot" BOOL NOT NULL  DEFAULT False,
    "created_at" TIMESTAMPTZ,
    "avatar_url" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "verificationroom" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "verification_flag" VARCHAR(255) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_verificatio_user_id_49a5ba" UNIQUE ("user_id", "verification_flag")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
