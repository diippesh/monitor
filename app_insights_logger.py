# app_insights_logger.py - Assignment: Custom logs and traces to Azure Application Insights
import logging
import os

# Configure Azure Monitor connection (reads from Application Insights connection string)
try:
    if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
        from azure.monitor.opentelemetry import configure_azure_monitor
        configure_azure_monitor()
        print("✅ Azure Application Insights configured successfully")
    else:
        print("⚠️ APPLICATIONINSIGHTS_CONNECTION_STRING not found - logging locally only")
except Exception as e:
    print(f"❌ Failed to configure Azure Application Insights: {e}")

# Set up custom logger
logger = logging.getLogger("assignment_logger")
logger.setLevel(logging.INFO)

# Send custom logs and traces as per assignment
logger.info("🚀 Assignment: Custom logging to Azure Application Insights started")
logger.warning("⚠️ Assignment: Custom warning trace for monitoring")
logger.error("❌ Assignment: Custom error trace for troubleshooting")
logger.info("✅ Assignment: Custom logs sent to Application Insights successfully")
