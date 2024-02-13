import os
import requests
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main(document: str) -> dict:
    endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]
    key = os.environ["TEXT_ANALYTICS_KEY"]

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    response = text_analytics_client.analyze_sentiment([document], show_opinion_mining=False)
    doc = next(iter(response))

    if not doc.is_error:
        simplified_result = {
            "overall_sentiment": doc.sentiment,
            "confidence_positive": doc.confidence_scores.positive,
            "confidence_neutral": doc.confidence_scores.neutral,
            "confidence_negative": doc.confidence_scores.negative,
            "document": document
        }
        return simplified_result
    else:
        return {"error": "Sentiment analysis failed"}
