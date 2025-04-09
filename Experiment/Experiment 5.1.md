## Objective

- pos = ["Sales Closure", "Flat Blocked"]
- neg = ["Not Interested", "Pre Site Visit", "Post Site Visit", "NA"]
- Do not subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- MEDIA_btn: 0.272141
- if_max_web_activity_is_recent: 0.082460
- Mode_operatingSystem: 0.068970
- sourceCampaign: 0.043234
- PRICE: 0.042743
- systime_since_first_event_this_week: 0.030574
- MEDIA: 0.019495
- PLAN: 0.018578
- total_sections_visited: 0.018562
- total_different_pages_visited: 0.018073
- Mode_sourceCampaign: 0.017155
- time_spent_this_session: 0.015632
- no_of_visits_last_7_days: 0.015390
- HOME_btn: 0.015108
- operatingSystem: 0.014400
- LOCATION: 0.014264
- max_loan_entry_this_session: 0.014109
- M_HOME: 0.013768
- AMENITIES_btn: 0.013334
- AMENITIES: 0.013283
- URL_HIT_btn: 0.012897
- SPECIFICATIONS: 0.012680
- cummulative_time_spent: 0.011654
- PRICE_btn: 0.011654
- M_PRICE: 0.011200
- M_SPECIFICATIONS: 0.011148
- projectId: 0.010562
- SPECIFICATIONS_btn: 0.010548
- M_PLAN: 0.010368
- HOME: 0.009498
- avg_web_activity_duration: 0.009387
- PLAN_btn: 0.009174
- time_since_last_web_session: 0.009013
- LOCATION_btn: 0.008917
- M_AMENITIES: 0.008796
- M_MEDIA: 0.008787
- max_web_activity_duration: 0.008664
- M_LOCATION: 0.008181
- time_spent_48h: 0.007974
- max_loan_last_7_days: 0.007868
- time_spent_24h: 0.007712
- recent_web_session_duration: 0.007098
- Mode_projectId: 0.007093
- loan_entries_last_7_days: 0.005897
- mapQueries_in_last_7_days: 0.005231
- loan_entries_this_session: 0.004724
- mapQueries_in_current_session: 0.002001

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666987
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.03%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
