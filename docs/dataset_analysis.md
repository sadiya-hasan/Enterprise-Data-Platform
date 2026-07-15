\# Olist Dataset Analysis



This document contains the analysis of the Brazilian E-Commerce Public Dataset by Olist.



\---



\# Orders Dataset



\*\*File Name\*\*



\- olist\_orders\_dataset.csv



\## Summary



\- Total Records: 99,441

\- Total Columns: 8

\- Primary Key: order\_id

\- Foreign Key: customer\_id



\## Columns



1\. order\_id

2\. customer\_id

3\. order\_status

4\. order\_purchase\_timestamp

5\. order\_approved\_at

6\. order\_delivered\_carrier\_date

7\. order\_delivered\_customer\_date

8\. order\_estimated\_delivery\_date



\## NULL Values



| Column | NULL Count |

|--------|-----------:|

| order\_approved\_at | 160 |

| order\_delivered\_carrier\_date | 1783 |

| order\_delivered\_customer\_date | 2965 |



\## Duplicate Records



\- Duplicate order\_id: 0



\## Distinct Order Statuses



\- approved

\- canceled

\- created

\- delivered

\- invoiced

\- processing

\- shipped

\- unavailable



\## Observation



The Orders table is the central table of the dataset.



Each order belongs to one customer and contains important timestamps that describe the order lifecycle.



Some delivery-related columns contain NULL values, which appear to be valid for cancelled or incomplete orders rather than data quality issues.

