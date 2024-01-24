# NBA Rankings

Building a NBA Standings Data Pipeline in Google Cloud using Airflow 

From retrieving data via the API_NBA to crafting a dynamic Looker Studio dashboard, each phase contributes to the seamless flow of data for analysis and visualization.

Architecture
![Architecture](https://github.com/lakshyarawal/NBA_Rankings/assets/20071320/1b7fae6f-a165-4780-9f46-e53db6e5070d)

**Data Retrieval with Python and API_NBA API**
Python **requests** library is used to fetch the JSON.

**Storing Data in Google Cloud Storage (GCS)**
Once the data is obtained, our next step involves preserving it securely in the cloud. We’ll explore how to store this data in a **CSV format within Google Cloud Storage (GCS)**, ensuring accessibility and scalability for future processing.

**Creating a Cloud Function Trigger**
With our data safely stored, we proceed to set up a **Cloud Function that acts as the catalyst for our pipeline.** This function triggers upon file upload to the GCS bucket, serving as the initiator for our subsequent data processing steps.

**Execution of the Cloud Function**
Within the Cloud Function, code triggers a Dataflow job. We’ll handle triggers and pass the requisite parameters to initiate the Dataflow job, ensuring a smooth flow of data processing.

**Dataflow Job for BigQuery**
The core of this pipeline lies in the Dataflow job. Triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery.

**Looker Dashboard Creation**
Configuring Looker to connect with BigQuery, we’ll create a visual dashboard. This dashboard will serve as the visualization hub, enabling analysis based on the data loaded from our NBA statistics pipeline.


