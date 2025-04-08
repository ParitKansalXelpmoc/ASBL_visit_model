## Feature Importance

<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/Top_15_Feature_Importances_from_Model.png' width='600'/>

- if_max_web_activity_is_recent: 0.084162
- MEDIA: 0.069937
- Mode_operatingSystem: 0.042202
- no_of_visits_last_7_days: 0.034266
- LOCATION: 0.031931
- time_spent_this_session: 0.028083
- Mode_sourceCampaign: 0.027020
- AMENITIES: 0.026089
- systime_since_first_event_this_week: 0.025720
- max_loan_entry_this_session: 0.025465
- operatingSystem: 0.024859
- M_MEDIA: 0.024302
- M_SPECIFICATIONS: 0.024270
- AMENITIES_btn: 0.023972
- SPECIFICATIONS: 0.022522
- PRICE_btn: 0.021867
- M_AMENITIES: 0.019867
- URL_HIT_btn: 0.019736
- M_PLAN: 0.019323
- total_different_pages_visited: 0.018931
- projectId: 0.018783
- HOME_btn: 0.018774
- sourceCampaign: 0.018726
- PRICE: 0.018610
- MEDIA_btn: 0.018226
- HOME: 0.017537
- M_PRICE: 0.017392
- PLAN: 0.017222
- total_sections_visited: 0.017160
- PLAN_btn: 0.016678
- M_HOME: 0.016559
- SPECIFICATIONS_btn: 0.016347
- max_web_activity_duration: 0.016244
- M_LOCATION: 0.015395
- LOCATION_btn: 0.015126
- time_since_last_web_session: 0.014146
- max_loan_last_7_days: 0.013526
- time_spent_48h: 0.013286
- cummulative_time_spent: 0.012775
- avg_web_activity_duration: 0.012585
- recent_web_session_duration: 0.012046
- time_spent_24h: 0.011398
- Mode_projectId: 0.010926
- loan_entries_last_7_days: 0.009720
- mapQueries_in_last_7_days: 0.009326
- loan_entries_this_session: 0.006962
- mapQueries_in_current_session: 0.000000

## Results Distribution

- Number of unique globalIds with ground_truth in test set is 0: 22261
- Number of unique globalIds with ground_truth in test set is 1: 212
- Percentage of positive globalIds compared to negative ones in test set : 0.95%
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/Percentage_of_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/Percentage_of_Unique_globalId_where_Ground_Truth_=_1_in_Top_N_Predictions.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/Unique_globalId_with_Ground_Truth_=_1_Percentage_in_NER_Intervals.png' width='600'/>

## Shap Values
### With ground_truth == 0 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/With_ground_truth_==_0_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 1 with rank > 500
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/With_ground_truth_==_1_with_rank_more_than_500.png' width='700'/>
### With ground_truth == 0 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/With_ground_truth_==_0_with_rank_more_than_10000.png' width='700'/>
### With ground_truth == 1 with rank > 10000
<img src='https://raw.githubusercontent.com/ParitKansalXelpmoc/ASBL_visit_model/main/Experiment/4_1/With_ground_truth_==_1_with_rank_more_than_10000.png' width='700'/>
