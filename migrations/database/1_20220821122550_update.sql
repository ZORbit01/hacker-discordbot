-- upgrade --
ALTER TABLE "member" ALTER COLUMN "avatar_url" DROP NOT NULL;
ALTER TABLE "member" ALTER COLUMN "created_at" DROP NOT NULL;
ALTER TABLE "user" ALTER COLUMN "avatar_url" DROP NOT NULL;
ALTER TABLE "user" ALTER COLUMN "created_at" DROP NOT NULL;
-- downgrade --
ALTER TABLE "user" ALTER COLUMN "avatar_url" SET NOT NULL;
ALTER TABLE "user" ALTER COLUMN "created_at" SET NOT NULL;
ALTER TABLE "member" ALTER COLUMN "avatar_url" SET NOT NULL;
ALTER TABLE "member" ALTER COLUMN "created_at" SET NOT NULL;
