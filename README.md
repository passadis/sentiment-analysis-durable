<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=azure,py,flask,terraform,vscode" />
  </a>
</p>

<h1 align="center">Azure AI Language: Sentiment Analysis with Durable Functions</h1>


## Introduction

This repository explores the integration of Azure Durable Functions with Azure AI Language services for Sentiment Analysis. Our focus is on utilizing Durable Functions, a powerful orchestration mechanism within the Azure Functions framework, to enhance the coding experience and build efficient, serverless solutions.

## Deployment

There are currently four durable function types in Azure Functions: activity, orchestrator, entity, and client. In our deployment we are using:

    Function 1 – HTTP Trigger (Client-Starter Function): Receives text input from the frontend and starts the orchestrator.
    Function 2 – Orchestrator Function: Orchestrates the sentiment analysis workflow.
    Function 3 – Activity Function: Calls Azure Cognitive Services Text Analytics API to analyze sentiment.
    Function 4 – Activity Function: Stores results into Azure Table Storage.


### Prerequisites

- **Code Editor**: We are using VSCode for our development.
- **Standard Files**: The necessary files for deployment, focusing on Infrastructure as Code (IaC) principles.

