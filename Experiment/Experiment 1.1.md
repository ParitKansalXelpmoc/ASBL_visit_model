## Objective

- pos = ["Sales Closure", "Flat Blocked"]
- neg = ["Not Interested"]
- Do not subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- if_max_web_activity_is_recent: 0.103620
- MEDIA: 0.086976
- Mode_operatingSystem: 0.039778
- no_of_visits_last_7_days: 0.032702
- LOCATION: 0.028866
- operatingSystem: 0.028669
- systime_since_first_event_this_week: 0.028083
- AMENITIES_btn: 0.026750
- time_spent_this_session: 0.026482
- SPECIFICATIONS: 0.025817
- Mode_sourceCampaign: 0.025714
- max_loan_entry_this_session: 0.024028
- PRICE_btn: 0.022247
- AMENITIES: 0.020605
- M_SPECIFICATIONS: 0.020545
- URL_HIT_btn: 0.019880
- M_PLAN: 0.018664
- PLAN: 0.018663
- M_AMENITIES: 0.018628
- MEDIA_btn: 0.018127
- sourceCampaign: 0.018102
- HOME_btn: 0.017992
- projectId: 0.017959
- total_different_pages_visited: 0.017691
- PRICE: 0.017240
- M_HOME: 0.016860
- HOME: 0.016794
- total_sections_visited: 0.016654
- M_PRICE: 0.016653
- LOCATION_btn: 0.016407
- M_MEDIA: 0.015735
- PLAN_btn: 0.015652
- M_LOCATION: 0.015454
- max_web_activity_duration: 0.015360
- SPECIFICATIONS_btn: 0.014903
- time_since_last_web_session: 0.014026
- cummulative_time_spent: 0.013938
- time_spent_48h: 0.013094
- max_loan_last_7_days: 0.012495
- avg_web_activity_duration: 0.011872
- time_spent_24h: 0.011560
- recent_web_session_duration: 0.011307
- Mode_projectId: 0.010377
- mapQueries_in_last_7_days: 0.006590
- loan_entries_this_session: 0.005380
- loan_entries_last_7_days: 0.005059
- mapQueries_in_current_session: 0.000000

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 21490
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.99%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
