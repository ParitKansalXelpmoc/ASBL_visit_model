## Objective

- pos = ["Pre Site Visit", "Post Site Visit", "Sales Closure", "Flat Blocked"]
- neg = ["NA", "Not Interested", "Lead Initiated", "New Lead"]
- Do subtract Lead Creation button process.


## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/Top_15_Feature_Importances_from_Model.png' width='600'/>

- PRICE: 0.108750
- MEDIA_btn: 0.084106
- sourceCampaign: 0.055016
- no_of_visits_last_7_days: 0.050156
- total_sections_visited: 0.049129
- systime_since_first_event_this_week: 0.043031
- if_max_web_activity_is_recent: 0.037174
- avg_web_activity_duration: 0.035635
- PLAN: 0.028360
- MEDIA: 0.028023
- Mode_operatingSystem: 0.024876
- URL_HIT_btn: 0.024230
- operatingSystem: 0.020362
- time_spent_this_session: 0.019297
- Mode_sourceCampaign: 0.019009
- max_loan_entry_this_session: 0.016700
- HOME_btn: 0.016116
- total_different_pages_visited: 0.015010
- time_spent_24h: 0.014705
- M_PRICE: 0.013882
- SPECIFICATIONS: 0.013772
- M_PLAN: 0.013458
- projectId: 0.013218
- LOCATION: 0.013187
- SPECIFICATIONS_btn: 0.013110
- PRICE_btn: 0.012804
- PLAN_btn: 0.012744
- M_SPECIFICATIONS: 0.012580
- M_MEDIA: 0.012236
- M_LOCATION: 0.012073
- AMENITIES: 0.012069
- max_web_activity_duration: 0.012037
- LOCATION_btn: 0.011821
- M_HOME: 0.011791
- M_AMENITIES: 0.011727
- cummulative_time_spent: 0.011711
- AMENITIES_btn: 0.011652
- HOME: 0.011290
- loan_entries_last_7_days: 0.010291
- time_since_last_web_session: 0.009976
- max_loan_last_7_days: 0.009436
- time_spent_48h: 0.009420
- recent_web_session_duration: 0.008811
- Mode_projectId: 0.008577
- mapQueries_in_last_7_days: 0.007956
- loan_entries_this_session: 0.006396
- mapQueries_in_current_session: 0.002291

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 666318
- Number of unique globalIds with ground_truth in test set is 1: 984
- Percentage of positive globalIds compared to negative ones in test set : 0.15%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/6_2/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
