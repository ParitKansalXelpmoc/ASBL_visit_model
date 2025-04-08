## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- if_max_web_activity_is_recent: 0.101830
- MEDIA: 0.086780
- Mode_operatingSystem: 0.040290
- no_of_visits_last_7_days: 0.034509
- systime_since_first_event_this_week: 0.028879
- LOCATION: 0.028853
- time_spent_this_session: 0.027520
- operatingSystem: 0.027326
- max_loan_entry_this_session: 0.026952
- Mode_sourceCampaign: 0.026135
- SPECIFICATIONS: 0.025899
- AMENITIES_btn: 0.024818
- M_SPECIFICATIONS: 0.021505
- AMENITIES: 0.020495
- PRICE_btn: 0.019671
- URL_HIT_btn: 0.019634
- HOME_btn: 0.019323
- PLAN: 0.019015
- M_AMENITIES: 0.018740
- M_PLAN: 0.018700
- M_MEDIA: 0.018075
- sourceCampaign: 0.017993
- PRICE: 0.017762
- HOME: 0.017533
- total_different_pages_visited: 0.017194
- M_PRICE: 0.017009
- MEDIA_btn: 0.016688
- total_sections_visited: 0.016540
- projectId: 0.016476
- M_HOME: 0.016458
- M_LOCATION: 0.015884
- PLAN_btn: 0.015749
- max_web_activity_duration: 0.015038
- LOCATION_btn: 0.014219
- time_since_last_web_session: 0.013967
- SPECIFICATIONS_btn: 0.012780
- max_loan_last_7_days: 0.012473
- time_spent_48h: 0.012254
- time_spent_24h: 0.011914
- cummulative_time_spent: 0.011861
- avg_web_activity_duration: 0.011851
- recent_web_session_duration: 0.011097
- Mode_projectId: 0.010377
- loan_entries_last_7_days: 0.008514
- mapQueries_in_last_7_days: 0.007573
- loan_entries_this_session: 0.005847
- mapQueries_in_current_session: 0.000000

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 21490
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.99%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/1_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
