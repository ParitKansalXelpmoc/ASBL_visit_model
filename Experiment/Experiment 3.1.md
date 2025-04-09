## Objective

- pos = ["Pre Site Visit", "Post Site Visit", "Sales Closure", "Flat Blocked"]
- neg = ["Not Interested"]
- Do not subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- if_max_web_activity_is_recent: 0.105689
- PLAN: 0.039037
- MEDIA_btn: 0.031923
- operatingSystem: 0.030252
- MEDIA: 0.029787
- systime_since_first_event_this_week: 0.029324
- URL_HIT_btn: 0.026378
- Mode_operatingSystem: 0.025985
- Mode_sourceCampaign: 0.024698
- time_spent_this_session: 0.024460
- max_loan_entry_this_session: 0.023949
- SPECIFICATIONS: 0.023627
- no_of_visits_last_7_days: 0.022747
- AMENITIES_btn: 0.021452
- LOCATION: 0.021188
- AMENITIES: 0.020697
- PRICE_btn: 0.020696
- M_LOCATION: 0.019873
- M_PLAN: 0.019510
- M_PRICE: 0.019180
- PLAN_btn: 0.018904
- HOME_btn: 0.018745
- PRICE: 0.018563
- LOCATION_btn: 0.018389
- SPECIFICATIONS_btn: 0.017977
- M_HOME: 0.017861
- max_web_activity_duration: 0.017791
- M_AMENITIES: 0.017744
- M_SPECIFICATIONS: 0.017614
- total_different_pages_visited: 0.017583
- total_sections_visited: 0.017569
- sourceCampaign: 0.017086
- HOME: 0.016567
- projectId: 0.016072
- M_MEDIA: 0.015084
- time_spent_24h: 0.014890
- max_loan_last_7_days: 0.014869
- avg_web_activity_duration: 0.014781
- time_since_last_web_session: 0.014772
- time_spent_48h: 0.014469
- cummulative_time_spent: 0.014346
- recent_web_session_duration: 0.013634
- Mode_projectId: 0.012852
- loan_entries_last_7_days: 0.012375
- loan_entries_this_session: 0.011700
- mapQueries_in_last_7_days: 0.011390
- mapQueries_in_current_session: 0.005922

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 21490
- Number of unique globalIds with ground_truth in test set is 1: 983
- Percentage of positive globalIds compared to negative ones in test set : 4.57%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
