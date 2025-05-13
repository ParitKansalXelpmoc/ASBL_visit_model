from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import pandas as pd
import tempfile
import shutil
import os
import json

# Required columns to verify in the input JSON
REQUIRED_COLUMNS = [
    '_id', 'botLog', 'visitorId', 'projectId', 'visitor_createdAt', 'instanceNumber',
    'visitorSource', 'channel', 'sourceCampaign', 'cummulativeTimeSpent',
    'operatingSystem', 'globalId', 'loanEntriesinterest',
    'loanEntriessalary', 'loanEntriesfoir', 'mapQueries_distance', 'mapQueries_duration',
    'trackEvents_eventName', 'trackEvents_startTime', 'trackEvents_timeSpent',
    'trackEvents_type', 'trackEvents_pageName', 'trackEvents_pageName_eventName_direct',
    'isLead', 'maxLeadStage', 'currLeadStage',
]

NOT_NULL_COLUMNS = REQUIRED_COLUMNS.copy()

# Import transformation functions
from src.merge import (
    compute_is_lead_created,
    compute_time_spent_this_session,
    compute_time_spent_per_page,
    compute_button_clicks_per_page,
    compute_enquiry_and_lead_clicks,
    compute_loan_entries,
    calculate_map_entries,
    process_web_session_sections,
)
from src.data_coversion import (
    preprocess_dataframe
)
from src.filter import filter_and_process_dataframe
from src.feature_creation import (
    calculate_time_spent_per_page_and_unique_pages_visited,
    mode_metrics,
    calculate_time_spent_last_24_and_48_hours,
    max_page_metrics,
    calculate_loan_map_metrics,
    compute_visits_and_activity_in_last_7_days,
    calculate_enquiry_and_lead_clicks_,
    calculate_button_count
)

app = FastAPI()

@app.post("/process-data/", response_model=List[dict])
async def process_data(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        # Load JSON data
        df = pd.read_json(tmp_path, lines=True)  # Change to lines=True if JSONL format

        # Drop any columns not in REQUIRED_COLUMNS
        df = df[[col for col in df.columns if col in REQUIRED_COLUMNS]]

        # Validate that all required columns are present
        missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required columns: {missing_columns}"
            )

        # Check for nulls in required columns
        nan_columns = df[NOT_NULL_COLUMNS].isnull().any()
        nan_columns_list = nan_columns[nan_columns].index.tolist()
        if nan_columns_list:
            raise HTTPException(
                status_code=400,
                detail=f"The following required columns contain null values: {nan_columns_list}"
            )

        # Step 1: Preprocess
        df = preprocess_dataframe(df)

        # Step 2: Apply feature engineering
        df = compute_is_lead_created(df)
        df = compute_time_spent_this_session(df)
        df = compute_time_spent_per_page(df)
        df = compute_button_clicks_per_page(df)
        df = compute_enquiry_and_lead_clicks(df)
        df = compute_loan_entries(df)
        df = calculate_map_entries(df)
        df = process_web_session_sections(df)

        # Step 3: Apply filtering and additional processing
        df = filter_and_process_dataframe(df)

        # Step 4:
        df = calculate_time_spent_per_page_and_unique_pages_visited(df)
        df = mode_metrics(df)
        df = calculate_time_spent_last_24_and_48_hours(df)
        df = max_page_metrics(df)
        df = calculate_loan_map_metrics(df)
        df = compute_visits_and_activity_in_last_7_days(df)
        df = calculate_enquiry_and_lead_clicks_(df)
        df = calculate_button_count(df)

        # Convert to JSON-compatible list of dicts
        records = json.loads(df.to_json(orient="records"))
        return records

    finally:
        os.remove(tmp_path)  # Clean up temporary file
