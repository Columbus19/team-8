CREATE TABLE IF NOT EXISTS users(
  fullname VARCHAR(40) NOT NULL,
  email VARCHAR(40) NOT NULL,
  profile_pic VARCHAR(64) NOT NULL,
  value_of_assets VARCHAR(40) NOT NULL,
  monthly_net_income VARCHAR(40) NOT NULL,
  dob VARCHAR(40) NOT NULL,
  ssn VARCHAR(40) NOT NULL,
  phone_number VARCHAR(40) NOT NULL,
  PRIMARY KEY(fullname)
);
