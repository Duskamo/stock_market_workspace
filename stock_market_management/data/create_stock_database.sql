
/* Create Database */
DROP DATABASE stock_market_workspace;
CREATE DATABASE stock_market_workspace;

/* Create Tables */
USE stock_market_workspace;

DROP TABLE trading_journal;
CREATE TABLE trading_journal(
	trade_id INT NOT NULL,
	trade_date VARCHAR(15),
	symbol VARCHAR(10),
	type VARCHAR(5),
	quantity FLOAT,
	bought FLOAT,
	sold FLOAT,
	initial_risk FLOAT,
	commission FLOAT,
	profit_and_loss FLOAT, 
	PRIMARY KEY (trade_id)
);
