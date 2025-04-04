CREATE TABLE flipkart_products (
    uniq_id VARCHAR(255) PRIMARY KEY,
    crawl_timestamp DATETIME,
    product_url TEXT,
    product_name TEXT,
    product_category_tree TEXT,
    pid VARCHAR(255),
    retail_price INT,
    discounted_price INT,
    image TEXT,
    is_FK_Advantage_product BOOLEAN,
    description TEXT,
    product_rating FLOAT,
    overall_rating FLOAT,
    brand VARCHAR(255),
    product_specifications TEXT
);

-- Load Data (Run this in MySQL)
LOAD DATA LOCAL INFILE 'C:/Users/Siddhesh/Downloads/flipkart_com-ecommerce_sample.csv'
INTO TABLE flipkart_products
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Query: Count Top 10 Categories
SELECT  
    SUBSTRING_INDEX(product_category_tree, ',', 1) AS category,  
    COUNT(*) AS total_products  
FROM flipkart_products  
GROUP BY category  
ORDER BY total_products DESC  
LIMIT 10;
-- Finds the Average Price of Each Category
SELECT  
    SUBSTRING_INDEX(product_category_tree, '>', 1) AS category,  
    AVG(retail_price) AS avg_price  
FROM flipkart_products  
GROUP BY category  
ORDER BY avg_price DESC
-- Finds the Best Rated Products
SELECT  
    product_name,  
    overall_rating  
FROM flipkart_products  
WHERE overall_rating IS NOT NULL  
ORDER BY overall_rating DESC  
LIMIT 10;
--for avg price 
SELECT  
    TRIM(BOTH ' []\"' FROM SUBSTRING_INDEX(product_category_tree, ',', 1)) AS category,  
    AVG(retail_price) AS avg_price  
FROM flipkart_products  
WHERE retail_price > 0  
GROUP BY category  
ORDER BY avg_price DESC;
