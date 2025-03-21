# Features Documentation

## 1. Identifiers & Timestamps
- **globalId**: Unique identifier assigned to a visitor.
- **_id**: Unique identifier assigned to a session/visit.
- **createdAt_x**: Timestamp indicating when this session/visit occurred.

## 2. Lead Status Indicators
- **isLead**: Indicates whether this particular session resulted in a lead conversion (1 = Yes, 0 = No).
- **is_lead_created**: Indicates if the lead was created in this session due to specific actions (LEAD_CREATED or SUBMIT_LEAD_BTN).
- **is_old_lead**: Indicates whether the visitor has been marked as `is_lead_created = True` for any session before the current one.

## 3. Session & Visit Characteristics
- **NoOfVisits**: Number of sessions the visitor had this week (including this session).
- **operatingSystem**: Most frequently used operating system by this visitor in the current week.
- **sourceCampaign**: Most frequently used marketing source or campaign in the current week.
- **projectId**: The projectId associated with this specific session.
- **projectId_mode**: Most frequently occurring projectId for the visitor in this week.
- **microMarket**: Most frequently visited micro-market by the visitor this week.

## 4. Time-Based Metrics
- **systime_since_first_event_this_week**: Time elapsed from the first session this week to the start of this session.
- **avg_web_activity_duration**: Average session duration for this visitor this week.
- **max_web_duration**: Longest session duration for this visitor this week.
- **time_spent_this_session**: Time spent in the current session.
- **if_maxweb_in_recent**: Indicates whether the longest session was the current one (1 = Yes, 0 = No).
- **recent_web_session_duration**: Duration of the most recent non-zero duration session before this one (if available, otherwise None).
- **time_since_last_web_session**: Time elapsed since the end of the previous session to the start of the current session.
- **instanceNumber**: Sequential session number in the dataset.
- **cummulativeTimeSpent**: Total time spent across all sessions this week (including the current session).

## 5. Recent Activity Duration (Action-Specific)
- **recent_24**: A dictionary of time spent on different actions in this session.
  
  Example:
  ```json
  {
      "HOME$HERO_SECTION$VIEW": 970.068,
      "HOME$HERO_SECTION": 2.558,
      "HOME$BROCHURE_SECTION": 5.634
  }
  ```
- **recent_24_cummulativeTimeSpent**: Total time spent on different actions in the last 24 hours.
- **recent_48**: A dictionary of time spent on different actions in this session but tracked for 48 hours.
- **recent_48_cummulativeTimeSpent**: Total time spent on different actions in the last 48 hours.

## 6. Mapping & Loan Interactions
- **is_map**: Indicates if the visitor used the map feature at least once this week.
- **Is_loan**: Indicates if the visitor made a loan inquiry at least once this week.
- **loan_entry_count**: Total number of loan inquiries made this week.
- **max_loan_entry**: Maximum loan inquiries in a single session this week.
- **map_entry_count**: Total number of times the visitor used the map feature this week.

## 7. Recent Visit Counts
- **recent_24_web_count**: Number of sessions by this visitor in the last 24 hours.
- **recent_48_web_count**: Number of sessions by this visitor in the last 48 hours.

## 8. Page & Section Visits
- **total_sections_visited**: Number of unique website sections visited this week.
- **total_pages_visited**: Number of unique pages visited this week.
- **Different Pages**: Time spent on specific pages this week:
  - OUR_STORY
  - SPECIFICATIONS
  - AMENITIES
  - MEDIA
  - OUR_PROJECTS
  - PRICE
  - LOCATION
  - PLAN
  - HOME
  - PLANS
  - NEARBY
  - PARTNER_WITH_US
  - LANDING
- **Different Pages Maximum**: Time spent on different pages during the session with the highest duration this week:
  - M_OUR_STORY
  - M_SPECIFICATIONS
  - M_AMENITIES
  - M_MEDIA
  - M_OUR_PROJECTS
  - M_PRICE
  - M_LOCATION
  - M_PLAN
  - M_HOME
  - M_PLANS
  - M_NEARBY
  - M_PARTNER_WITH_US
  - M_LANDING

## 9. Button Clicks & Interactions
- **button_counts**: A dictionary tracking the number of times different buttons were clicked in this session.
  
  Example:
  ```json
  {
      "URL_HIT": 33,
      "HOME": 40,
      "PLAN": 27,
      "MEDIA": 29
  }
  ```
- **total_btn_clicked**: Total buttons clicked in the last 7 days.
- **Different Buttons**: Count of different types of buttons clicked in the last 7 days:
  - URL_HIT_btn
  - HOME_btn
  - PLAN_btn
  - MEDIA_btn
  - PRICE_btn
  - AMENITIES_btn
  - LOCATION_btn
  - SPECIFICATIONS_btn
  - LANDING_btn
  - OUR_PROJECTS_btn
  - ENQUIRE_btn
  - EXPLORE_btn
  - OUR_STORY_btn
  - QR_btn
  - BLOGS_btn
  - PARTNER_WITH_US_btn
  - EVENTS_btn
  - POLLS/CCLEX011_btn
  - LOCATION#:~:TEXT=BE%20IT%20VIA%20THE%20BALANAGAR,THIS%20SPOT%20ENSURES%20GREAT%20CONNECTIVITY._btn

