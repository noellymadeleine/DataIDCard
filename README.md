# DataIDCard
When working with a CSV file, one of the initial steps is to get a sneak peek at the data, including column names, missing values, data types, etc. However, this information is often presented in a messy way. This Python script provides a simple solution to make the dataset sneak peek more readable.
This script collects and prints information about a dataset. It reads a dataset from a CSV file, collects various information such as shape, column names, missing values, and data types, and prints the information in a nice ASCII format.

## Requirements

- Python 3.x
- pandas

## Usage

1. Install the required dependencies:

   ```shell
   pip install pandas 
   ```
   
run:
   ```shell
   python collect_dataset_info.py [your csv file]
   ```

Here is an example of results:

```
+----------------------------------------+
|             Dataset Shape              |
+----------------------------------------+
|              Rows: 10,000              |
|              Columns: 12               |
+----------------------------------------+

+----------------------------------------+
|              Column Names              |
+----------------------------------------+
| customer_id                            |
| credit_score                           |
| country                                |
| gender                                 |
| age                                    |
| tenure                                 |
| balance                                |
| products_number                        |
| credit_card                            |
| active_member                          |
| estimated_salary                       |
| churn                                  |
+----------------------------------------+

+----------------------------------------+
|             Missing Values             |
+----------------------------------------+
| customer_id: 0                         |
| credit_score: 0                        |
| country: 0                             |
| gender: 0                              |
| age: 0                                 |
| tenure: 0                              |
| balance: 0                             |
| products_number: 0                     |
| credit_card: 0                         |
| active_member: 0                       |
| estimated_salary: 0                    |
| churn: 0                               |
+----------------------------------------+

+----------------------------------------+
|               Data Types               |
+----------------------------------------+
| customer_id: int64                     |
| credit_score: int64                    |
| country: object                        |
| gender: object                         |
| age: int64                             |
| tenure: int64                          |
| balance: float64                       |
| products_number: int64                 |
| credit_card: int64                     |
| active_member: int64                   |
| estimated_salary: float64              |
| churn: int64                           |
+----------------------------------------+
```

