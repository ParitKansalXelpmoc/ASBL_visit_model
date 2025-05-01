import pandas as pd
from re import I
import numpy as np

def calculate_time_spent_per_page_and_unique_pages_visited(df):
    """
    Calculates the time spent on each page for each session in the last 7 days.

    Args:
    df (pd.DataFrame): Input DataFrame with columns:
        - 'globalId': Unique identifier for each user.
        - 'visitor_createdAt': Timestamp of the session.
        - 'instanceNumber': The instance number of the session.
        - 'time_spent_per_page': Dictionary containing page visit durations.

    Returns:
    pd.DataFrame: DataFrame with additional columns for each page in `main_pages`,
                  storing total time spent and total unique pages visited.
    """

    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    main_pages = ['HOME', 'PLAN', 'LOCATION', 'MEDIA', 'PRICE', 'AMENITIES', 'SPECIFICATIONS']

    # Initialize new columns for pages and total unique pages visited
    for page in main_pages:
        df[page] = 0.0
    df['total_different_pages_visited'] = 0

    def process_user_sessions(group):
        group = group.sort_values(['visitor_createdAt', 'instanceNumber']).copy().reset_index(drop=True)

        # Preallocate lists for storing results
        pages_time = {page: [0.0] * len(group) for page in main_pages}
        unique_pages = [0] * len(group)

        for i in range(len(group)):
            current_time = group.iloc[i]['visitor_createdAt']
            temp = group.iloc[:i+1]  # Ensuring inclusion of all past sessions

            # Filter for sessions in the last 7 days
            time_diffs = (current_time - temp['visitor_createdAt']).dt.total_seconds()
            recent_sessions = temp[time_diffs <= 604800].copy().reset_index(drop=True)  # 7 days in seconds

            # Compute total time spent per page
            page_time = {page: 0 for page in main_pages}
            for session_dict in recent_sessions['time_spent_per_page']:
                for page, time in session_dict.items():
                    if page in page_time:
                        page_time[page] += time

            # Store computed values
            for page in main_pages:
                pages_time[page][i] = page_time[page]
            unique_pages[i] = sum(1 for page in main_pages if page_time[page] > 0)

        # Assign computed values back to DataFrame
        for page in main_pages:
            group[page] = pages_time[page]
        group["total_different_pages_visited"] = unique_pages

        return group

    df = df.groupby('globalId', group_keys=False).apply(process_user_sessions)
    return df

def mode_metrics(df):
    """
    Calculates the mode of 'projectId', 'operatingSystem', and 'sourceCampaign' in the last 7 days.
    In case of a tie, the oldest value is selected.

    Args:
    df (pd.DataFrame): Input DataFrame with columns:
        - 'globalId': Unique identifier for each user.
        - 'visitor_createdAt': Timestamp of the session.
        - 'projectId': Project ID for the session.
        - 'operatingSystem': Operating system used in the session.
        - 'sourceCampaign': Source campaign for the session.
        - 'instanceNumber'

    Returns:
    pd.DataFrame: DataFrame with additional columns:
        - 'Mode_projectId': Mode of projectId in the last 7 days.
        - 'Mode_operatingSystem': Mode of operatingSystem in the last 7 days.
        - 'Mode_sourceCampaign': Mode of sourceCampaign in the last 7 days.
    """
    # Sort df chronologically within each user (globalId) based on session time and instance number

    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    df["Mode_projectId"] = None
    df["Mode_operatingSystem"] = None
    df["Mode_sourceCampaign"] = None

    def process_user_sessions(group):
        group = group.copy().reset_index(drop = True)
        for i in range(len(group)):
            current_time = group.iloc[i]['visitor_createdAt']
            temp = group.iloc[:i+1]
            recent_sessions = temp[(current_time - temp['visitor_createdAt']).dt.days <= 7].copy().reset_index(drop = True)

            if not recent_sessions.empty:
                for col in ["projectId", "operatingSystem", "sourceCampaign"]:
                    mode_values = recent_sessions[col].mode()
                    if not mode_values.empty:
                        # Get the first occurrence of the mode value in recent sessions
                        oldest_mode_value = recent_sessions[recent_sessions[col].isin(mode_values)].iloc[0][col]
                        group.at[group.index[i], f"Mode_{col}"] = oldest_mode_value
        return group

    df = df.groupby('globalId', group_keys=False).apply(process_user_sessions)

    allowed_sources = ("google", "organic", "whatsapp", "fim", "yoptima", "inshorts", "direct", "aurum", "criteo", "crit_ads", "dv_ads")
    df['sourceCampaign'] = df['sourceCampaign'].apply(lambda x: x if x in allowed_sources else "other")
    df['Mode_sourceCampaign'] = df['Mode_sourceCampaign'].apply(lambda x: x if x in allowed_sources else "other")

    allowed_os = ("android", "ios", "window", "mac", "linux", "chrome")
    df['operatingSystem'] = df['operatingSystem'].apply(lambda x: x.lower() if x.lower() in allowed_os else "unknown")
    df['Mode_operatingSystem'] = df['Mode_operatingSystem'].apply(lambda x: x.lower() if x.lower() in allowed_os else "unknown")


    return df


def calculate_time_spent_last_24_and_48_hours(df):
    """
    Calculates the total time spent in the last 24 hours and 48 hours for each session.

    Args:
    df (pd.DataFrame): Input DataFrame with columns:
        - 'globalId': Unique identifier for each user.
        - 'visitor_createdAt': Timestamp of the session.
        - 'time_spent_this_session': Time spent on the current session.

    Returns:
    pd.DataFrame: DataFrame with additional columns:
        - 'time_spent_24h': Total time spent in the last 24 hours.
        - 'time_spent_48h': Total time spent in the last 48 hours.
    """

    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    def process_user_sessions(group):
        # Pre-allocate lists
        group = group.sort_values(['visitor_createdAt', 'instanceNumber']).reset_index(drop=True).copy()
        time_spent_24h = [0.0] * len(group)
        time_spent_48h = [0.0] * len(group)

        for i in range(len(group)):
            current_time = group.iloc[i]['visitor_createdAt']
            temp = group.iloc[:i+1]  # Sessions up to the current session

            # Filter for sessions within the last 24 and 48 hours
            time_diffs = (current_time - temp['visitor_createdAt']).dt.total_seconds()
            recent_sessions_24h = temp[time_diffs <= 86400].reset_index(drop=True).copy()  # Last 24 hours
            recent_sessions_48h = temp[time_diffs <= 172800].reset_index(drop=True).copy()  # Last 48 hours

            # Calculate total time spent in the last 24 and 48 hours
            time_spent_24h[i] = recent_sessions_24h['time_spent_this_session'].sum()
            time_spent_48h[i] = recent_sessions_48h['time_spent_this_session'].sum()

        # Assign computed values back to DataFrame
        group["time_spent_24h"] = time_spent_24h
        group["time_spent_48h"] = time_spent_48h

        return group

    df = df.groupby('globalId', group_keys=False).apply(process_user_sessions)

    return df



def max_page_metrics(df):
    """
    Calculates the max time spent on each page in the most time-consuming session within the last 7 days.

    Args:
    df (pd.DataFrame): Input DataFrame with columns:
        - 'globalId': Unique identifier for each user.
        - 'visitor_createdAt': Timestamp of the session.
        - 'instanceNumber': The instance number of the session.
        - 'time_spent_per_page': Dictionary containing page visit durations.
        - 'time_spent_this_session': Total time spent in this session.

    Returns:
    pd.DataFrame: DataFrame with additional columns for each page in `main_pages`,
                  storing the max time spent in any session within the last 7 days.
    """

    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    main_pages = ['HOME', 'PLAN', 'LOCATION', 'MEDIA', 'PRICE', 'AMENITIES', 'SPECIFICATIONS']

    # Initialize new columns
    for page in main_pages:
        df["M_" + page] = 0.0

    def process_user_sessions(group):
        group = group.sort_values(['visitor_createdAt', 'instanceNumber']).reset_index(drop=True).copy()
        max_time_per_page = {page: [0.0] * len(group) for page in main_pages}  # Pre-allocate storage

        for i in range(len(group)):
            current_time = group.iloc[i]['visitor_createdAt']

            # Get sessions within the last 7 days
            recent_sessions = group.iloc[:i+1]
            recent_sessions = recent_sessions[(current_time - recent_sessions['visitor_createdAt']).dt.days <= 7].reset_index(drop=True).copy()

            if recent_sessions.empty:
                continue

            # Find session with the maximum `time_spent_this_session`
            max_session_idx = recent_sessions['time_spent_this_session'].idxmax()
            max_session = recent_sessions.loc[max_session_idx]

            # Extract max time per page
            session_page_time = max_session['time_spent_per_page'] if isinstance(max_session['time_spent_per_page'], dict) else {}

            for page in main_pages:
                max_time_per_page[page][i] = session_page_time.get(page, 0.0)

        # Assign computed values back to DataFrame
        for page in main_pages:
            group["M_" + page] = max_time_per_page[page]

        return group

    df = df.groupby('globalId', group_keys=False).apply(process_user_sessions)

    return df



def calculate_loan_map_metrics(df):
    """
    Function to calculate:
    1. max_loan_entry_this_session and loan_entries_this_session.
    2. max_loan_last_7_days and loan_entries_last_7_days.
    3. map_queries_last_7_days (based on mapQueries_in_current_session)

    Args:
    df (pd.DataFrame): Must contain:
                       - 'globalId'
                       - 'visitor_createdAt'
                       - 'instanceNumber'
                       - 'loan_entries_this_session'
                       - 'max_loan_entry_this_session'
                       - 'mapQueries_in_current_session'

    Returns:
    pd.DataFrame: Original DataFrame with additional columns:
                  - 'max_loan_last_7_days'
                  - 'loan_entries_last_7_days'
                  - 'mapQueries_in_last_7_days'
    """
    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    def compute_metrics_for_user(user_df):
        user_df = user_df.sort_values(['visitor_createdAt', 'instanceNumber']).copy().reset_index(drop=True)
        n = len(user_df)
        max_loan_7_days = [0] * n
        loan_entries_7_days = [0] * n
        map_queries_7_days = [0] * n

        for i in range(n):
            current_time = user_df.iloc[i]['visitor_createdAt']
            time_diffs = (current_time - user_df.iloc[:i+1]['visitor_createdAt']).dt.total_seconds()
            last_7_days_df = user_df.iloc[:i+1][time_diffs <= 604800].copy()

            max_loan_7_days[i] = last_7_days_df['max_loan_entry_this_session'].max(skipna=True)
            loan_entries_7_days[i] = last_7_days_df['loan_entries_this_session'].sum(skipna=True)
            map_queries_7_days[i] = last_7_days_df['mapQueries_in_current_session'].sum(skipna=True)

        user_df['max_loan_last_7_days'] = max_loan_7_days
        user_df['loan_entries_last_7_days'] = loan_entries_7_days
        user_df['mapQueries_in_last_7_days'] = map_queries_7_days

        return user_df
    df = df.groupby('globalId', group_keys=False).apply(compute_metrics_for_user)

    return df


def compute_visits_and_activity_in_last_7_days(df):
    """
    Optimized function to calculate:
    1. Number of visits in the last 7 days for each session.
    2. Average web activity duration for each session considering only rows where 'time_spent_this_session' is not 0 or NaN.
    3. Maximum web activity duration for each session.
    4. Whether the current session has the maximum web activity in the last 7 days for that globalId.

    Args:
    df (pd.DataFrame): Input DataFrame with columns:
                       - 'globalId'
                       - 'visitor_createdAt'
                       - 'instanceNumber'
                       - 'time_spent_this_session'

    Returns:
    pd.DataFrame: Original DataFrame with additional columns:
                  - 'no_of_visits_last_7_days'
                  - 'avg_web_activity_duration'
                  - 'max_web_activity_duration'
                  - 'if_max_web_activity_is_recent'
                  - 'recent_web_session_duration'
                  - 'time_since_last_web_session'
                  - 'systime_since_first_event'
                  - 'systime_since_first_event_this_week'
    """
    df = df.copy()
    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], utc=True)

    # Sort the DataFrame by 'globalId', 'visitor_createdAt', and 'instanceNumber'
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    # Group by 'globalId' to process each group separately
    def process_group(group):
        group = group.copy().reset_index(drop = True)
        # Initialize lists to store results
        no_of_visits_last_7_days = []
        avg_web_activity_duration = []
        max_web_activity_duration = []
        if_max_web_activity_is_recent = []
        recent_web_session_duration = []
        time_since_last_web_session = []
        systime_since_first_event_this_week = []
        cummulative_time_spent = []
        no_of_session_haing_time_spent_greater_than_avg_time_spent = []

        # Iterate over each row in the group
        for i, row in group.iterrows():
            # Filter rows up to the current row
            current_df = group.iloc[:i + 1]

            # Calculate visits in the last 7 days
            seven_days_ago = row['visitor_createdAt'] - pd.Timedelta(days=7)
            last_7_days_visits = current_df[current_df['visitor_createdAt'] > seven_days_ago].copy()
            no_of_visits_last_7_days.append(len(last_7_days_visits))
            cummulative_time_spent.append(last_7_days_visits['time_spent_this_session'].sum())

            # Filter valid rows for average web activity duration (excluding 0 and NaN)
            valid_rows = last_7_days_visits[['visitor_createdAt', 'time_spent_this_session']].copy().replace(0, pd.NA).dropna().reset_index(drop = True)
            avg_duration = valid_rows['time_spent_this_session'].mean() if len(valid_rows) > 0 else 0
            avg_web_activity_duration.append(avg_duration)
            no_of_session_haing_time_spent_greater_than_avg_time_spent.append(
                len(valid_rows[valid_rows['time_spent_this_session'] > avg_duration])
                )


            # Get the second-to-last session duration if it exists
            recent_session_duration = valid_rows['time_spent_this_session'].iloc[-2] if len(valid_rows) > 1 else 0
            recent_web_session_duration.append(recent_session_duration)

            # Calculate time since last web session
            if len(valid_rows) > 1:
                time_diff = row['visitor_createdAt'] - list(valid_rows['visitor_createdAt'])[-2]
                time_since_last_web_session.append(time_diff.total_seconds())
                if(time_diff.total_seconds() < 0):
                    print(time_diff.total_seconds())
                    print(row['globalId'])
            else:
                time_since_last_web_session.append(np.nan)

            # Calculate the maximum web activity duration for valid rows
            max_duration = valid_rows['time_spent_this_session'].max() if len(valid_rows) > 0 else np.nan
            max_web_activity_duration.append(max_duration)

            # Calculate the maximum activity duration in the last 7 days
            recent_max_duration = last_7_days_visits['time_spent_this_session'].max()
            if row['time_spent_this_session'] == recent_max_duration:
                if_max_web_activity_is_recent.append(True)
            else:
                if_max_web_activity_is_recent.append(False)


            # Calculate the time since the first event in the last 7 days
            systime_since_first_event_this_week.append(
                (row['visitor_createdAt'] - last_7_days_visits['visitor_createdAt'].min()).total_seconds() / 86400
            )

        # Assign calculated values to group columns
        group['no_of_visits_last_7_days'] = no_of_visits_last_7_days
        group['avg_web_activity_duration'] = avg_web_activity_duration

        group['max_web_activity_duration'] = max_web_activity_duration
        group['if_max_web_activity_is_recent'] = if_max_web_activity_is_recent
        ### change this
        group['recent_web_session_duration'] = recent_web_session_duration
        group['time_since_last_web_session'] = time_since_last_web_session
        group['systime_since_first_event_this_week'] = systime_since_first_event_this_week
        group['cummulative_time_spent'] = cummulative_time_spent
        group['no_of_session_haing_time_spent_greater_than_avg_time_spent'] = no_of_session_haing_time_spent_greater_than_avg_time_spent
        return group

    # Apply processing to each group and reset index
    df = df.groupby('globalId', group_keys=False).apply(process_group)

    return df




def calculate_enquiry_and_lead_clicks_(df):
    """
    Args:
    df (pd.DataFrame): Input DataFrame with columns:
        - 'globalId': Unique identifier for each user.
        - 'visitor_createdAt': Timestamp of the session.
        - 'instanceNumber': The instance number of the session.
        - 'enquiry_and_lead_clicks': Dictionary containing button visit counts.

    Returns:
    pd.DataFrame: Updated DataFrame with additional columns tracking button clicks in the last 7 days.
    """

    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')

    # Sort for chronological order
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    # List of buttons to track
    buttons = ['HOME', 'PLAN', 'LOCATION', 'MEDIA', 'PRICE', 'AMENITIES', 'SPECIFICATIONS']

    # Initialize button count columns
    for button in buttons:
        df[button + "_btn_sub_cum"] = 0

    def process_user_sessions(group):
        group = group.sort_values(['visitor_createdAt', 'instanceNumber']).reset_index(drop=True).copy()
        button_counts = {button+ "_btn_sub": [0] * len(group) for button in buttons}  # Pre-allocate storage
        #print(button_counts)

        for i in range(len(group)):
            current_time = group.iloc[i]['visitor_createdAt']

            # Get past sessions within the last 7 days
            recent_sessions = group.iloc[:i+1]
            recent_sessions = recent_sessions[(current_time - recent_sessions['visitor_createdAt']).dt.days <= 7].reset_index(drop=True).copy()

            # Initialize button visit counts
            enquiry_and_lead_clicks = {}

            # Accumulate button counts from recent sessions
            for session_dict in recent_sessions['enquiry_and_lead_clicks'].fillna({}):  # Handle NaN values
                #print(session_dict)
                for button, count in session_dict.items():
                    enquiry_and_lead_clicks[button] = count + enquiry_and_lead_clicks.get(button, 0)
            #print("*"*100)
            #print(buttons)
            #print(button_counts)
            #print(enquiry_and_lead_clicks)
            # Store results in pre-allocated lists
            for button in buttons:
                button_counts[button+"_btn_sub"][i] = enquiry_and_lead_clicks[button+ "_btn_sub"]
            #print("*"*100)


        # Assign computed values back to DataFrame
        for button in buttons:
            group[button + "_btn_sub_cum"] = button_counts[button + "_btn_sub"]

        return group

    df = df.groupby('globalId', group_keys=False).apply(process_user_sessions)

    return df


def calculate_button_count(df):
    """
    Args:
    df (pd.DataFrame): Input DataFrame with columns:
        - 'globalId': Unique identifier for each user.
        - 'visitor_createdAt': Timestamp of the session.
        - 'instanceNumber': The instance number of the session.
        - 'button_count': Dictionary containing button visit counts.

    Returns:
    pd.DataFrame: Updated DataFrame with additional columns tracking button clicks in the last 7 days.
    """

    df['visitor_createdAt'] = pd.to_datetime(df['visitor_createdAt'], errors='coerce')

    # Sort for chronological order
    df = df.sort_values(['globalId', 'visitor_createdAt', 'instanceNumber']).reset_index(drop=True)

    # List of buttons to track
    buttons = ['HOME', 'PLAN', 'LOCATION', 'MEDIA', 'PRICE', 'AMENITIES', 'SPECIFICATIONS']

    # Initialize button count columns
    for button in buttons:
        df[button + "_btn_cum"] = 0

    def process_user_sessions(group):
        gropu = group.sort_values(['visitor_createdAt', 'instanceNumber']).reset_index(drop=True).copy()
        button_counts = {button + "_btn_cum": [0] * len(group) for button in buttons}  # Pre-allocate storage
        #print(button_counts)
        #print("*"*100)
        for i in range(len(group)):
            current_time = group.iloc[i]['visitor_createdAt']

            # Get past sessions within the last 7 days
            recent_sessions = group.iloc[:i+1]
            recent_sessions = recent_sessions[(current_time - recent_sessions['visitor_createdAt']).dt.days <= 7].reset_index(drop=True).copy()

            # Initialize button visit counts
            button_count = {button + "_btn_cum": 0 for button in buttons}
            #print(button_count)
            #print("*"*100)

            # Accumulate button counts from recent sessions
            for session_dict in recent_sessions['button_count'].fillna({}):  # Handle NaN values
                for button, count in session_dict.items():
                    button_count[button] = count + button_count.get(button, 0)
            #print(button_count)
            #print("*"*100)

            # Store results in pre-allocated lists
            for button in buttons:
                button_counts[button + "_btn_cum"][i] = button_count[button + "_btn"]

            #print(button_counts)
            #print("*"*100)


        # Assign computed values back to DataFrame
        for button in buttons:
            group[button + "_btn_cum"] = button_counts[button+"_btn_cum"]

        return group

    df = df.groupby('globalId', group_keys=False).apply(process_user_sessions)

    return df