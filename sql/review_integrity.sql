-- Purpose: Stores a fingerprint (SHA-256 hash) of each submitted review so later
-- changes or deletions can be detected (story: Detect changes to submitted reviews).
-- Author: Maaz Majeed. Run once in dev, then in UAT.
CREATE TABLE IF NOT EXISTS ReviewFingerprints (
  reviewType  VARCHAR(20) NOT NULL,   -- 'Open' or 'Confidential'
  reviewID    INT NOT NULL,
  contentHash CHAR(64) NOT NULL,
  recordedAt  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (reviewType, reviewID)
);
