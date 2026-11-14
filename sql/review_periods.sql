-- Purpose: Creates the ReviewPeriods table (Sprint 1). Run once in dev, then in UAT.
-- Author: Maaz Majeed. 
CREATE TABLE IF NOT EXISTS ReviewPeriods (
  periodID INT AUTO_INCREMENT PRIMARY KEY,
  periodName VARCHAR(100) NOT NULL UNIQUE,
  startDate DATE NOT NULL,
  deadlineDate DATE NOT NULL,
  isConfidential BOOLEAN NOT NULL DEFAULT FALSE,
  createdBy INT NOT NULL,
  FOREIGN KEY (createdBy) REFERENCES Employees(employeeID)
);
