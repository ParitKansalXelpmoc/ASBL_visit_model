## Objective

- pos = ["Pre Site Visit", "Post Site Visit", "Sales Closure", "Flat Blocked"]
- neg = ["Not Interested"]
- Do subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- if_max_web_activity_is_recent: 0.097109
- PLAN: 0.039917
- MEDIA_btn: 0.034094
- MEDIA: 0.031725
- operatingSystem: 0.031383
- systime_since_first_event_this_week: 0.028703
- time_spent_this_session: 0.026609
- Mode_operatingSystem: 0.026135
- URL_HIT_btn: 0.025656
- max_loan_entry_this_session: 0.025145
- Mode_sourceCampaign: 0.024639
- no_of_visits_last_7_days: 0.024151
- SPECIFICATIONS: 0.023044
- LOCATION: 0.021595
- AMENITIES: 0.020785
- SPECIFICATIONS_btn: 0.020600
- M_PLAN: 0.020008
- AMENITIES_btn: 0.019686
- M_LOCATION: 0.019604
- PLAN_btn: 0.019502
- M_PRICE: 0.019343
- HOME_btn: 0.018861
- LOCATION_btn: 0.018782
- PRICE: 0.018767
- max_web_activity_duration: 0.018356
- M_AMENITIES: 0.018300
- PRICE_btn: 0.018206
- total_different_pages_visited: 0.017792
- M_HOME: 0.017732
- M_SPECIFICATIONS: 0.017451
- total_sections_visited: 0.017348
- projectId: 0.017198
- HOME: 0.016446
- M_MEDIA: 0.015866
- sourceCampaign: 0.015702
- time_since_last_web_session: 0.014998
- avg_web_activity_duration: 0.014980
- time_spent_24h: 0.014954
- max_loan_last_7_days: 0.014674
- time_spent_48h: 0.014495
- recent_web_session_duration: 0.013733
- cummulative_time_spent: 0.013521
- Mode_projectId: 0.012931
- mapQueries_in_last_7_days: 0.012011
- loan_entries_last_7_days: 0.011367
- loan_entries_this_session: 0.010849
- mapQueries_in_current_session: 0.005247

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 21490
- Number of unique globalIds with ground_truth in test set is 1: 983
- Percentage of positive globalIds compared to negative ones in test set : 4.57%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/3_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
