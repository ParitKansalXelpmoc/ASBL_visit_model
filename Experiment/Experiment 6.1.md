## Objective

- pos = ["Pre Site Visit", "Post Site Visit", "Sales Closure", "Flat Blocked"]
- neg = ["NA", "Not Interested", "Lead Initiated", "New Lead"]
- Do not subtract Lead Creation button process.

## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- PRICE: 0.113005
- MEDIA_btn: 0.082953
- sourceCampaign: 0.054677
- no_of_visits_last_7_days: 0.050593
- total_sections_visited: 0.048378
- systime_since_first_event_this_week: 0.043417
- if_max_web_activity_is_recent: 0.037651
- avg_web_activity_duration: 0.032988
- MEDIA: 0.030788
- Mode_operatingSystem: 0.023354
- URL_HIT_btn: 0.022602
- HOME_btn: 0.021081
- Mode_sourceCampaign: 0.020732
- operatingSystem: 0.020562
- PLAN: 0.020120
- time_spent_this_session: 0.019697
- max_loan_entry_this_session: 0.016049
- M_MEDIA: 0.015142
- M_PRICE: 0.014439
- projectId: 0.013847
- time_spent_24h: 0.013800
- total_different_pages_visited: 0.013683
- SPECIFICATIONS_btn: 0.013619
- PRICE_btn: 0.013378
- SPECIFICATIONS: 0.013269
- M_PLAN: 0.013263
- LOCATION: 0.013225
- AMENITIES: 0.012377
- PLAN_btn: 0.012372
- max_web_activity_duration: 0.012190
- M_SPECIFICATIONS: 0.012019
- M_LOCATION: 0.011868
- cummulative_time_spent: 0.011862
- M_HOME: 0.011818
- AMENITIES_btn: 0.011617
- LOCATION_btn: 0.011521
- HOME: 0.011313
- M_AMENITIES: 0.010683
- time_since_last_web_session: 0.009777
- time_spent_48h: 0.009666
- max_loan_last_7_days: 0.009443
- Mode_projectId: 0.008868
- recent_web_session_duration: 0.008693
- mapQueries_in_last_7_days: 0.008327
- loan_entries_this_session: 0.008065
- loan_entries_last_7_days: 0.007843
- mapQueries_in_current_session: 0.003364

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666318
- Number of unique globalIds with ground_truth in test set is 1: 984
- Percentage of positive globalIds compared to negative ones in test set : 0.15%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
