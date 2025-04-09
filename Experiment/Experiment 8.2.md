## Objective

- "is_lead_created"
- Do subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- cummulative_time_spent: 0.599206
- M_PRICE: 0.095113
- Mode_projectId: 0.070523
- MEDIA_btn: 0.027974
- HOME_btn: 0.020445
- PRICE: 0.011159
- total_different_pages_visited: 0.011061
- Mode_sourceCampaign: 0.010414
- if_max_web_activity_is_recent: 0.010383
- PRICE_btn: 0.009917
- sourceCampaign: 0.008732
- M_HOME: 0.007025
- projectId: 0.006144
- total_sections_visited: 0.005973
- Mode_operatingSystem: 0.005163
- no_of_visits_last_7_days: 0.004865
- loan_entries_this_session: 0.004850
- URL_HIT_btn: 0.004678
- loan_entries_last_7_days: 0.004622
- LOCATION_btn: 0.004593
- operatingSystem: 0.004477
- time_spent_this_session: 0.003860
- systime_since_first_event_this_week: 0.003438
- avg_web_activity_duration: 0.003219
- HOME: 0.003202
- M_PLAN: 0.003076
- M_LOCATION: 0.003024
- PLAN: 0.002959
- time_since_last_web_session: 0.002945
- LOCATION: 0.002922
- AMENITIES: 0.002867
- max_loan_entry_this_session: 0.002856
- SPECIFICATIONS: 0.002846
- MEDIA: 0.002802
- recent_web_session_duration: 0.002770
- time_spent_48h: 0.002757
- AMENITIES_btn: 0.002735
- time_spent_24h: 0.002732
- max_loan_last_7_days: 0.002701
- PLAN_btn: 0.002624
- max_web_activity_duration: 0.002480
- SPECIFICATIONS_btn: 0.002394
- M_MEDIA: 0.002380
- M_SPECIFICATIONS: 0.002358
- M_AMENITIES: 0.002329
- mapQueries_in_current_session: 0.002225
- mapQueries_in_last_7_days: 0.002179

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 654779
- Number of unique globalIds with ground_truth in test set is 1: 20701
- Percentage of positive globalIds compared to negative ones in test set : 3.16%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/8_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
