## Objective

- pos = ["Sales Closure", "Flat Blocked"]
- neg = ["Not Interested", "NA"]
- Do subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- MEDIA_btn: 0.255084
- if_max_web_activity_is_recent: 0.103039
- sourceCampaign: 0.054394
- PRICE: 0.050605
- systime_since_first_event_this_week: 0.040575
- Mode_operatingSystem: 0.027114
- MEDIA: 0.022272
- PLAN: 0.019626
- no_of_visits_last_7_days: 0.017610
- max_loan_entry_this_session: 0.016376
- Mode_sourceCampaign: 0.016189
- total_sections_visited: 0.015411
- total_different_pages_visited: 0.015106
- operatingSystem: 0.014644
- AMENITIES_btn: 0.014476
- LOCATION: 0.014355
- time_spent_this_session: 0.014307
- M_HOME: 0.014084
- projectId: 0.013723
- HOME_btn: 0.013380
- URL_HIT_btn: 0.013274
- SPECIFICATIONS: 0.012392
- M_SPECIFICATIONS: 0.011591
- cummulative_time_spent: 0.011566
- AMENITIES: 0.010922
- M_PLAN: 0.010885
- M_AMENITIES: 0.010855
- M_PRICE: 0.010781
- PRICE_btn: 0.010571
- max_web_activity_duration: 0.010119
- PLAN_btn: 0.009616
- SPECIFICATIONS_btn: 0.009452
- M_MEDIA: 0.009276
- HOME: 0.009236
- avg_web_activity_duration: 0.009186
- time_spent_24h: 0.008972
- LOCATION_btn: 0.008971
- time_since_last_web_session: 0.008191
- mapQueries_in_current_session: 0.008017
- time_spent_48h: 0.007913
- max_loan_last_7_days: 0.007704
- Mode_projectId: 0.007436
- M_LOCATION: 0.007368
- recent_web_session_duration: 0.006946
- mapQueries_in_last_7_days: 0.006359
- loan_entries_last_7_days: 0.006149
- loan_entries_this_session: 0.003878

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666215
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.03%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
