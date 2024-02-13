from azure.data.tables import TableServiceClient
import os
import json
from datetime import datetime

def main(results: dict) -> str:
    connection_string = os.environ['AZURE_TABLE_STORAGE_CONNECTION_STRING']
    table_name = 'SentimentAnalysisResults'

    table_service = TableServiceClient.from_connection_string(connection_string)
    table_client = table_service.get_table_client(table_name)

    # Prepare the entity with a unique RowKey using timestamp
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    row_key = f"{results.get('document')}-{timestamp}"

    entity = {
        "PartitionKey": "SentimentAnalysis",
        "RowKey": row_key,
        "Document": results.get('document'),
        "Sentiment": results.get('overall_sentiment'),
        "Confidence": results.get('confidence')
    }

    # Insert the entity
    table_client.create_entity(entity=entity)

    return "Result stored in Azure Table Storage"
