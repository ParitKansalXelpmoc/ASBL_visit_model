import pandas as pd

def filter_and_process_dataframe(df)-> pd.DataFrame:
    # Filter rows where time_spent_this_session > 5
    df = df[df['time_spent_this_session'] > 5]
    
    # Sort dataframe
    df = df.sort_values(by=['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)
    
    # Define the column groups and the new column names
    columns_to_process = [
        (['PRICE', 'HOME', 'PLAN', 'AMENITIES', 'LOCATION', 'SPECIFICATIONS', 'MEDIA'], 'time_spent_per_page'),
        (['PRICE_btn', 'HOME_btn', 'PLAN_btn', 'AMENITIES_btn', 'LOCATION_btn', 'SPECIFICATIONS_btn', 'MEDIA_btn'], 'button_count'),
        (['PRICE_btn_sub', 'HOME_btn_sub', 'PLAN_btn_sub', 'AMENITIES_btn_sub', 'LOCATION_btn_sub', 'SPECIFICATIONS_btn_sub', 'MEDIA_btn_sub'], 'enquiry_and_lead_clicks')
    ]
    
    # Loop through each column set and create new columns
    for cols, new_col in columns_to_process:
        result = []
        for i in range(len(df)):
            result.append({col: df[col][i] for col in cols})
        df[new_col] = result

    # Return the processed dataframe
    return df
