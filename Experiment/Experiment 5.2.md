## Objective

- pos = ["Sales Closure", "Flat Blocked"]
- neg = ["Not Interested", "Pre Site Visit", "Post Site Visit", "NA"]
- Do subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- MEDIA: 0.247514
- if_max_web_activity_is_recent: 0.086803
- Mode_operatingSystem: 0.061135
- sourceCampaign: 0.056279
- PRICE: 0.041330
- systime_since_first_event_this_week: 0.029072
- no_of_visits_last_7_days: 0.025085
- total_sections_visited: 0.019459
- time_spent_this_session: 0.018848
- total_different_pages_visited: 0.018668
- PLAN: 0.017928
- Mode_sourceCampaign: 0.016604
- max_loan_entry_this_session: 0.016016
- operatingSystem: 0.014895
- LOCATION: 0.014712
- URL_HIT_btn: 0.014678
- HOME_btn: 0.014671
- MEDIA_btn: 0.014417
- M_HOME: 0.014407
- AMENITIES_btn: 0.013802
- AMENITIES: 0.013137
- SPECIFICATIONS: 0.012815
- M_SPECIFICATIONS: 0.012297
- M_PRICE: 0.011608
- PRICE_btn: 0.011595
- projectId: 0.011250
- M_PLAN: 0.010684
- avg_web_activity_duration: 0.010625
- M_AMENITIES: 0.010458
- M_MEDIA: 0.010413
- PLAN_btn: 0.010240
- SPECIFICATIONS_btn: 0.010098
- cummulative_time_spent: 0.009685
- LOCATION_btn: 0.009464
- HOME: 0.009295
- max_web_activity_duration: 0.009001
- M_LOCATION: 0.008696
- time_since_last_web_session: 0.008570
- time_spent_24h: 0.008403
- time_spent_48h: 0.007902
- max_loan_last_7_days: 0.007851
- Mode_projectId: 0.007764
- recent_web_session_duration: 0.007543
- mapQueries_in_last_7_days: 0.005520
- loan_entries_last_7_days: 0.005412
- loan_entries_this_session: 0.003353
- mapQueries_in_current_session: 0.000000

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666987
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.03%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/5_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
