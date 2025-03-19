from pyspark.sql.functions import bucket

key = "first_etl_project"
iv = "first_etl_prj"
salt ="first_AESEcryption"

#AWS ACCESS AND SECREET KEY
aws_access_key = "  "  #Encrypted Key
aws_secret_key = "   " #Encrypted key
bucket_name = "first-etl-prj"
s3_transaction_data_mart_directory = "transaction_data_mart/"
s3_transaction_data_error_directory = "transaction_data_error/"
s3_transaction_data_processing_directory = "transaction_data_processing/"
s3_transaction_directory = "transaction_data/"


#Databse Credential
#mysql Database Connection properties
database_name = "first_etl_prj"
url = f"jdbc:mysql://localhost:3306/{database_name}"
properties ={
    "user":"root",
    "password":"password",
    "driver":"com.mysql.cj.jdbc.Driver"
}

#Table name
customer_table = "customer"
transaction_staging_table = "transaction_staging_table"
date_table = "date"
account_table = "account"

# data mart detail
transaction_data_mart_table = "transaction_data_mart"

#mandatory columns
mandatory_column = ["transaction_id","date_id","customer_id","account_id","amount","transaction_type"]

#file download location
local_directory = "H:\\first_etl_prj_local_file\\file_from_s3\\"
transaction_data_mart_local_file = "H:\\first_etl_prj_local_file\\transaction_data_mart\\"
transaction_data_mart_partition_local_file = "H:\\first_etl_prj_local_file\\transaction_data_partition\\"
error_folder_local_path = "H:\\first_etl_prj_local_file\\error_files\\"