import pandas as pd
import ast

def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['visitorSource'] == "TRACKING"].copy().reset_index(drop=True)
    df['_id'] = df['_id'].astype(str)
    df['botLog'] = df['botLog'].astype(str)
    df['visitorId'] = df['visitorId'].astype(str)
    df['projectId'] = df['projectId'].astype(str)
    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')
    df['instanceNumber'] = df['instanceNumber'].astype(int)
    df['visitorSource'] = df['visitorSource'].astype(str)
    df['channel'] = df['channel'].astype(int)
    df['sourceCampaign'] = df['sourceCampaign'].astype(str)
    df['cummulativeTimeSpent'] = df['cummulativeTimeSpent'].astype(float)
    df['operatingSystem'] = df['operatingSystem'].astype(str)
    # df['userDeviceInfo'] = df['userDeviceInfo'].fillna("").astype(str)
    df['globalId'] = df['globalId'].astype(int)
    
    list_columns = [
        'loanEntriesinterest', 'loanEntriessalary', 'loanEntriesfoir',
        'mapQueries_distance', 'mapQueries_duration',
        'trackEvents_eventName', 'trackEvents_timeSpent', 'trackEvents_type',
        'trackEvents_pageName', 'trackEvents_pageName_eventName_direct'
    ]
    
    for col in list_columns:
        df[col] = df[col].apply(lambda x: ast.literal_eval(x.strip()) if isinstance(x, str) else x)

    df['trackEvents_startTime'] = df['trackEvents_startTime'].astype(str)
    df['isLead'] = df['isLead'].astype(bool)
    df['maxLeadStage'] = df['maxLeadStage'].astype(str)
    # df['microMarket'] = df['microMarket'].fillna("").astype(str)
    # df['isActualMicroMarket'] = df['isActualMicroMarket'].fillna("").astype(str)
    df['trackEvents_pageName'] = df['trackEvents_pageName'].apply(
            lambda x: [str(item).replace(
                'LOCATION#:~:TEXT=BE%20IT%20VIA%20THE%20BALANAGAR,THIS%20SPOT%20ENSURES%20GREAT%20CONNECTIVITY.',
                'LOCATION') for item in x]
        )

    df['sourceCampaign'] = df['sourceCampaign'].str.lower()
    df['sourceCampaign'] = df['sourceCampaign'].str.strip()
    df['sourceCampaign'] = df['sourceCampaign'].str.strip("'\"")
    df['sourceCampaign'] = df['sourceCampaign'].str.replace(' ', '_')
    df['sourceCampaign'] = df['sourceCampaign'].apply(
        lambda x: 'google' if 'google' in x else x
    )
    df['sourceCampaign'] = df['sourceCampaign'].apply(
        lambda x: 'fb' if x.startswith('fb') else x
    )
    df['sourceCampaign'] = df['sourceCampaign'].apply(
        lambda x: 'inncircles' if x.startswith('inncircle') else x
    )
    df['sourceCampaign'] = df['sourceCampaign'].apply(
        lambda x: 'news_paper' if "news" in x and ("print" in x or "paper" in x) else x
    )
    df['sourceCampaign'] = df['sourceCampaign'].apply(
        lambda x: 'affiliatesms' if x.startswith('affiliatesms') else x
    )
    df['sourceCampaign'] = df['sourceCampaign'].apply(
        lambda x: 'test' if x.startswith('test') else x
    )
    
    return df
