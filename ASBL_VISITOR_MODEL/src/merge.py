import pandas as pd

def compute_time_spent_per_page(df: pd.DataFrame)-> pd.DataFrame:
    """
    Computes cumulative time spent per page for each globalId separately.
    """
    known_pages = ['PRICE', 'HOME', 'PLAN', 'AMENITIES', 'LOCATION', 'SPECIFICATIONS', 'MEDIA']
    for page in known_pages:
        trackEvents_timeSpent_ = list(df['trackEvents_timeSpent'])
        trackEvents_pageName_ = list(df['trackEvents_pageName'])
        trackEvents_type_ = list(df['trackEvents_type'])
        result = [0.0 for _ in range(len(df))]
        for i in range(len(df)):
            for timespent, pagename, pagetype in zip(
                trackEvents_timeSpent_[i], trackEvents_pageName_[i], trackEvents_type_[i]
            ):
                if str(pagetype).lower() != 'click' and pagename == page:
                    result[i] += timespent

        df[page] = result
    return df




def compute_button_clicks_per_page(df: pd.DataFrame)-> pd.DataFrame:
    """
    Computes cumulative time spent per page for each globalId separately.
    """
    known_pages = ['PRICE', 'HOME', 'PLAN', 'AMENITIES', 'LOCATION', 'SPECIFICATIONS', 'MEDIA']
    for page in known_pages:
        trackEvents_timeSpent_ = list(df['trackEvents_timeSpent'])
        trackEvents_pageName_ = list(df['trackEvents_pageName'])
        trackEvents_type_ = list(df['trackEvents_type'])
        result = [0 for _ in range(len(df))]
        for i in range(len(df)):
            for timespent, pagename, pagetype in zip(
                trackEvents_timeSpent_[i], trackEvents_pageName_[i], trackEvents_type_[i]
            ):
                if str(pagetype).lower() == 'click' and pagename == page:
                    result[i] += 1

        df[page+"_btn"] = result
    return df



def compute_time_spent_this_session(df: pd.DataFrame)-> pd.DataFrame:
    """
    Computes total time spent in each session per globalId.
    """
    df["time_spent_this_session"] = [sum(a) for a in df['trackEvents_timeSpent']]
    return df



def compute_is_lead_created(df: pd.DataFrame)-> pd.DataFrame:
    """
    Computes 'is_lead_created' flag for each session based on events.
    """

    events = [str(x) for x in df["trackEvents_eventName"]]
    times = [sum(a) for a in df['trackEvents_timeSpent']]

    result = []
    for event, time in zip(events, times):
        if ("$LEAD_CREATED" in event or "$SUBMIT_LEAD_BTN" in event) and time > 1:
            result.append(True)
        else:
            result.append(False)
    df["is_lead_created"] = result

    return df




def compute_enquiry_and_lead_clicks(df: pd.DataFrame)-> pd.DataFrame:
    """
    Computes number of ENQUIRY_DIALOG or LEAD button clicks per known page
    for each globalId separately. 
    """
    known_pages = ['PRICE', 'HOME', 'PLAN', 'AMENITIES', 'LOCATION', 'SPECIFICATIONS', 'MEDIA']
    for page in known_pages:
        trackEvents_timeSpent_ = list(df['trackEvents_timeSpent'])
        trackEvents_pageName_ = list(df['trackEvents_pageName'])
        trackEvents_type_ = list(df['trackEvents_type'])
        trackEvents_eventName_ = list(df['trackEvents_eventName'])

        result = [0 for _ in range(len(df))]
        for i in range(len(df)):
            for timespent, pagename, pagetype, eventName in zip(
                trackEvents_timeSpent_[i], trackEvents_pageName_[i],
                trackEvents_type_[i], trackEvents_eventName_[i]
            ):
                event_str = " ".join(eventName).upper()
                if str(pagetype).lower() == 'click' and pagename == page and ('ENQUIRY_DIALOG' in event_str or 'LEAD' in event_str):
                    result[i] += 1

        df[page + "_btn_sub"] = result
    return df




def process_web_session_sections(df: pd.DataFrame) -> pd.DataFrame:
    trackEvents_eventName_ = list(df['trackEvents_eventName'])
    trackEvents_timeSpent_ = list(df['trackEvents_timeSpent'])
    trackEvents_pageName_ = list(df['trackEvents_pageName'])
    result = []

    for i in range(len(df)):
        section_dict = {}
        event_lists = trackEvents_eventName_[i]
        timespents = trackEvents_timeSpent_[i]
        pagenames = trackEvents_pageName_[i]

        for event_list, timespent, pagename in zip(event_lists, timespents, pagenames):
            if not event_list or len(event_list) == 0 or timespent <= 0.01:
                continue

            page_count = len(event_list)
            if page_count == 0:
                continue

            timesplit = timespent / page_count

            for event in event_list:
                event = event.strip('$')

                if pagename and pagename not in event:
                    event = f"{pagename}${event}"

                # Normalize known event names
                event = (event.replace('LANDING', 'HOME')
                                .replace('ENQUIRE', 'HOME')
                                .replace('PLANS', 'PLAN'))

                section_event = "$".join(event.split('$')[:2])
                section_dict[section_event] = section_dict.get(section_event, 0) + timesplit

        result.append(section_dict)

    df['sections_info'] = result
    return df


def compute_loan_entries(df: pd.DataFrame) -> pd.DataFrame:
    a = list(df['loanEntriessalary'])

    # Count number of entries in each list
    df['loan_entries_this_session'] = [len(x) for x in a]

    # Get the max value in the list, or None if empty or not a list
    df['max_loan_entry_this_session'] = [
        max(x) if len(x) > 0 else None for x in a
    ]

    return df


def calculate_map_entries(df: pd.DataFrame) -> pd.DataFrame:
    a = list(df['mapQueries_duration'])
    df['mapQueries_in_current_session'] =  [len(x) for x in a]
    return df

