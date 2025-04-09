## Objective

- pos = ["Sales Closure", "Flat Blocked"]
- neg = ["Not Interested", "Pre Site Visit", "Post Site Visit"]
- Do subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- if_max_web_activity_is_recent: 0.081312
- MEDIA: 0.072322
- Mode_operatingSystem: 0.044023
- no_of_visits_last_7_days: 0.032269
- LOCATION: 0.031460
- time_spent_this_session: 0.028567
- AMENITIES: 0.026745
- systime_since_first_event_this_week: 0.026350
- max_loan_entry_this_session: 0.025728
- AMENITIES_btn: 0.025458
- operatingSystem: 0.025132
- Mode_sourceCampaign: 0.025123
- M_MEDIA: 0.023734
- M_SPECIFICATIONS: 0.023234
- SPECIFICATIONS: 0.022363
- HOME_btn: 0.020404
- PRICE_btn: 0.020182
- URL_HIT_btn: 0.019794
- M_AMENITIES: 0.019655
- MEDIA_btn: 0.019114
- total_different_pages_visited: 0.018878
- sourceCampaign: 0.018828
- PRICE: 0.018787
- HOME: 0.018492
- M_PLAN: 0.018372
- projectId: 0.018168
- SPECIFICATIONS_btn: 0.017977
- PLAN: 0.017826
- M_PRICE: 0.017349
- PLAN_btn: 0.017276
- total_sections_visited: 0.017231
- M_HOME: 0.017112
- max_web_activity_duration: 0.015941
- cummulative_time_spent: 0.014942
- LOCATION_btn: 0.013949
- time_since_last_web_session: 0.013795
- M_LOCATION: 0.013385
- max_loan_last_7_days: 0.013086
- avg_web_activity_duration: 0.012609
- time_spent_48h: 0.012604
- time_spent_24h: 0.012093
- recent_web_session_duration: 0.011360
- mapQueries_in_last_7_days: 0.010831
- Mode_projectId: 0.010816
- loan_entries_last_7_days: 0.009329
- loan_entries_this_session: 0.005996
- mapQueries_in_current_session: 0.000000

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 22261
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.95%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
