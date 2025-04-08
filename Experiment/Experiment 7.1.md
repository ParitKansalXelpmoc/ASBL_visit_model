## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- MEDIA_btn: 0.284469
- if_max_web_activity_is_recent: 0.102665
- PRICE: 0.049815
- sourceCampaign: 0.047390
- systime_since_first_event_this_week: 0.037921
- Mode_operatingSystem: 0.026547
- PLAN: 0.020297
- MEDIA: 0.019217
- no_of_visits_last_7_days: 0.018457
- Mode_sourceCampaign: 0.016843
- total_sections_visited: 0.016255
- HOME_btn: 0.015022
- time_spent_this_session: 0.014400
- max_loan_entry_this_session: 0.014054
- AMENITIES_btn: 0.013780
- M_HOME: 0.013628
- operatingSystem: 0.013405
- total_different_pages_visited: 0.013173
- LOCATION: 0.013139
- SPECIFICATIONS: 0.012741
- URL_HIT_btn: 0.012672
- projectId: 0.012493
- PRICE_btn: 0.011017
- M_SPECIFICATIONS: 0.010937
- M_PLAN: 0.010894
- M_PRICE: 0.010875
- M_AMENITIES: 0.010698
- cummulative_time_spent: 0.010562
- max_web_activity_duration: 0.010466
- AMENITIES: 0.010191
- PLAN_btn: 0.010052
- LOCATION_btn: 0.009948
- SPECIFICATIONS_btn: 0.009832
- time_since_last_web_session: 0.009013
- HOME: 0.008702
- avg_web_activity_duration: 0.008546
- M_MEDIA: 0.008101
- time_spent_48h: 0.007743
- max_loan_last_7_days: 0.007648
- M_LOCATION: 0.007634
- time_spent_24h: 0.007612
- recent_web_session_duration: 0.007038
- Mode_projectId: 0.006771
- mapQueries_in_last_7_days: 0.005315
- loan_entries_last_7_days: 0.004961
- loan_entries_this_session: 0.004856
- mapQueries_in_current_session: 0.002204

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666215
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.03%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/7_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
