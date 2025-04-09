## Objective

- "is_lead_created"
- Do not subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- cummulative_time_spent: 0.628350
- PRICE_btn: 0.096172
- Mode_projectId: 0.049573
- HOME_btn: 0.029732
- MEDIA_btn: 0.021759
- time_spent_this_session: 0.016090
- M_PRICE: 0.014924
- total_different_pages_visited: 0.012807
- Mode_sourceCampaign: 0.011300
- loan_entries_last_7_days: 0.008897
- sourceCampaign: 0.007008
- M_HOME: 0.006946
- LOCATION_btn: 0.005442
- total_sections_visited: 0.005282
- URL_HIT_btn: 0.004363
- if_max_web_activity_is_recent: 0.004319
- projectId: 0.004227
- PRICE: 0.004046
- AMENITIES_btn: 0.003656
- Mode_operatingSystem: 0.003372
- operatingSystem: 0.003146
- systime_since_first_event_this_week: 0.003115
- no_of_visits_last_7_days: 0.002783
- PLAN_btn: 0.002695
- HOME: 0.002614
- max_web_activity_duration: 0.002521
- SPECIFICATIONS: 0.002499
- SPECIFICATIONS_btn: 0.002468
- max_loan_entry_this_session: 0.002401
- avg_web_activity_duration: 0.002298
- PLAN: 0.002282
- AMENITIES: 0.002262
- time_since_last_web_session: 0.002260
- MEDIA: 0.002249
- M_LOCATION: 0.002214
- recent_web_session_duration: 0.002152
- M_PLAN: 0.002152
- loan_entries_this_session: 0.002123
- time_spent_24h: 0.002113
- LOCATION: 0.002109
- mapQueries_in_last_7_days: 0.002089
- M_AMENITIES: 0.002003
- time_spent_48h: 0.001951
- max_loan_last_7_days: 0.001890
- mapQueries_in_current_session: 0.001804
- M_SPECIFICATIONS: 0.001801
- M_MEDIA: 0.001739

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 654779
- Number of unique globalIds with ground_truth in test set is 1: 20701
- Percentage of positive globalIds compared to negative ones in test set : 3.16%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
