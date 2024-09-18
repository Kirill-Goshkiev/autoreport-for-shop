CREATE TABLE public.reports (
	shop_n varchar NOT NULL,
	cash_n varchar NOT NULL,
	doc_id varchar NOT NULL,
	item varchar NOT NULL,
	category varchar NOT NULL,
	amount int4 NULL,
	price numeric NULL,
	discount int4 NULL,
	CONSTRAINT reports_pk PRIMARY KEY (shop_n, cash_n, doc_id, item, category)
);
