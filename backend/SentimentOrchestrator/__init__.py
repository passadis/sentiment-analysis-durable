import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    document = context.get_input()  # Treat input as a single document
    result = yield context.call_activity("AnalyzeSentiment", document)
    # Call the function to store the result in Azure Table Storage
    yield context.call_activity("StoreInTableStorage", result)
    return result

main = df.Orchestrator.create(orchestrator_function)
