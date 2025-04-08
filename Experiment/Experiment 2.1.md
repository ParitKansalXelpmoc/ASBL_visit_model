## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- PRICE: 0.111510
- MEDIA_btn: 0.085342
- sourceCampaign: 0.052990
- no_of_visits_last_7_days: 0.050590
- total_sections_visited: 0.049329
- systime_since_first_event_this_week: 0.042452
- if_max_web_activity_is_recent: 0.038446
- avg_web_activity_duration: 0.033088
- MEDIA: 0.031339
- Mode_operatingSystem: 0.023538
- URL_HIT_btn: 0.023364
- HOME_btn: 0.021589
- operatingSystem: 0.020897
- PLAN: 0.020270
- Mode_sourceCampaign: 0.020114
- time_spent_this_session: 0.018582
- max_loan_entry_this_session: 0.016053
- M_MEDIA: 0.015101
- M_PRICE: 0.014387
- total_different_pages_visited: 0.014147
- time_spent_24h: 0.014051
- projectId: 0.013911
- PRICE_btn: 0.013564
- LOCATION: 0.013303
- SPECIFICATIONS_btn: 0.013221
- M_PLAN: 0.013108
- SPECIFICATIONS: 0.012756
- M_LOCATION: 0.012597
- PLAN_btn: 0.012577
- max_web_activity_duration: 0.012090
- AMENITIES: 0.011991
- cummulative_time_spent: 0.011933
- M_HOME: 0.011763
- LOCATION_btn: 0.011737
- AMENITIES_btn: 0.011697
- M_SPECIFICATIONS: 0.011648
- M_AMENITIES: 0.011403
- HOME: 0.011336
- time_spent_48h: 0.009571
- time_since_last_web_session: 0.009568
- max_loan_last_7_days: 0.009420
- Mode_projectId: 0.008843
- recent_web_session_duration: 0.008629
- loan_entries_last_7_days: 0.008183
- mapQueries_in_last_7_days: 0.007951
- loan_entries_this_session: 0.007143
- mapQueries_in_current_session: 0.002878

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666215
- Number of unique globalIds with ground_truth in test set is 1: 984
- Percentage of positive globalIds compared to negative ones in test set : 0.15%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
