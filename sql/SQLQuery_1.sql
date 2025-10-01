select * from [Credit_Risk_Analysis].[dbo].[loan_cleaned] 

-- counting no. of loans
Select count(*) as total_loans FROM [Credit_Risk_Analysis].[dbo].[loan_cleaned]

-- counting  loans by status
select count(loan_status), count(*) as count from [Credit_Risk_Analysis].[dbo].[loan_cleaned] group by loan_status order by count DESC

-- calculat ethe average loan amount for each grade
select avg(loan_amnt) , grade from [Credit_Risk_Analysis].[dbo].[loan_cleaned] group by grade order by grade asc 

-- analyzing the distribution of loans by employement length
select count(loan_amnt) as count,emp_length as Employment_length from [Credit_Risk_Analysis].[dbo].[loan_cleaned] group by emp_length order by emp_length

-- finding default rate by loan purpose
SELECT purpose,
       COUNT(*) AS total_loans,
       SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS defaulted_loans,
       CAST(SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS default_rate
FROM [Credit_Risk_Analysis].[dbo].[loan_cleaned]
GROUP BY purpose
ORDER BY default_rate DESC;

--Top 10 states by average loan amount
SELECT addr_state, AVG(loan_amnt) AS avg_loan_amount
FROM [Credit_Risk_Analysis].[dbo].[loan_cleaned]
GROUP BY addr_state
ORDER BY avg_loan_amount DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;


SELECT TOP 10 *
FROM [Credit_Risk_Analysis].[dbo].[loan_cleaned];

-- SELECT COLUMN_NAME
-- FROM INFORMATION_SCHEMA.COLUMNS
-- WHERE TABLE_NAME = [Credit_Risk_Analysis].[dbo].[loan_cleaned];

-- default rate over time(month/year)
SELECT DATEPART(YEAR,issue_d) as years, 
datepart(MONTH,issue_d) as months, count(*) as total_loans,
sum(Case when loan_status='Charged Off' Then 1 else 0 end) 
from [Credit_Risk_Analysis].[dbo].[loan_cleaned] 
group by DATEPART(year, issue_d), DATEPART(month, issue_d)
ORDER BY years, months

-- subgrade wise default rate
SELECT 
    sub_grade,                             -- Group results by each sub-grade
    COUNT(*) AS total_loans,              -- Count total number of loans issued with this sub-grade
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS defaulted_loans,  -- Count loans defaulted ('Charged Off')
    CAST(SUM(CASE WHEN loan_status = 'Charged Off' 
    THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS default_rate  -- Calculate default rate as ratio
FROM 
    [Credit_Risk_Analysis].[dbo].[loan_cleaned]
GROUP BY 
    sub_grade                            -- Group by sub_grade to aggregate counts per category
ORDER BY 
    default_rate DESC;                   -- Sort results to show riskiest sub-grades first


SELECT 
    CASE 
        WHEN loan_amnt < 5000 THEN '<5k'
        WHEN loan_amnt BETWEEN 5000 AND 10000 THEN '5k-10k'
        WHEN loan_amnt BETWEEN 10001 AND 20000 THEN '10k-20k'
        ELSE '>20k'
    END AS loan_amnt_bin,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS defaulted_loans,
    CAST(SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS default_rate
FROM 
    [Credit_Risk_Analysis].[dbo].[loan_cleaned]
GROUP BY 
    CASE 
        WHEN loan_amnt < 5000 THEN '<5k'
        WHEN loan_amnt BETWEEN 5000 AND 10000 THEN '5k-10k'
        WHEN loan_amnt BETWEEN 10001 AND 20000 THEN '10k-20k'
        ELSE '>20k'
    END
ORDER BY 
    default_rate DESC;


SELECT 
    addr_state,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS defaulted_loans,
    CAST(SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS default_rate
FROM 
    [Credit_Risk_Analysis].[dbo].[loan_cleaned]
GROUP BY 
    addr_state
ORDER BY 
    default_rate DESC;
