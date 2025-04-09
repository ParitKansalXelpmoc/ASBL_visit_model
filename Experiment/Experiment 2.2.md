## Objective

- pos = ["Pre Site Visit", "Post Site Visit", "Sales Closure", "Flat Blocked"]
- neg = ["NA", "Not Interested"]
- Do subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- PRICE: 0.110862
- MEDIA_btn: 0.082035
- sourceCampaign: 0.057444
- no_of_visits_last_7_days: 0.050451
- total_sections_visited: 0.049451
- systime_since_first_event_this_week: 0.043064
- if_max_web_activity_is_recent: 0.038394
- avg_web_activity_duration: 0.036569
- MEDIA: 0.029019
- PLAN: 0.027367
- Mode_operatingSystem: 0.025361
- URL_HIT_btn: 0.024973
- operatingSystem: 0.020520
- Mode_sourceCampaign: 0.018068
- time_spent_this_session: 0.017646
- max_loan_entry_this_session: 0.016631
- HOME_btn: 0.016089
- total_different_pages_visited: 0.015141
- time_spent_24h: 0.014776
- SPECIFICATIONS: 0.013833
- M_PRICE: 0.013703
- M_PLAN: 0.013152
- projectId: 0.013028
- LOCATION: 0.012828
- cummulative_time_spent: 0.012823
- M_MEDIA: 0.012578
- PRICE_btn: 0.012519
- PLAN_btn: 0.012358
- M_SPECIFICATIONS: 0.012185
- AMENITIES_btn: 0.011933
- M_LOCATION: 0.011851
- AMENITIES: 0.011804
- M_HOME: 0.011634
- SPECIFICATIONS_btn: 0.011512
- LOCATION_btn: 0.011451
- max_web_activity_duration: 0.011394
- HOME: 0.011312
- M_AMENITIES: 0.010874
- time_since_last_web_session: 0.009869
- max_loan_last_7_days: 0.009700
- time_spent_48h: 0.009626
- recent_web_session_duration: 0.008850
- Mode_projectId: 0.008755
- mapQueries_in_last_7_days: 0.008683
- loan_entries_last_7_days: 0.006820
- loan_entries_this_session: 0.006664
- mapQueries_in_current_session: 0.004397

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666215
- Number of unique globalIds with ground_truth in test set is 1: 984
- Percentage of positive globalIds compared to negative ones in test set : 0.15%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/2_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
