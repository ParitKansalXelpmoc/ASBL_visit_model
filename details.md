# Model (without URL influence)

### **Feature Importance List**  
1. **if_maxweb_in_recent**: 0.247776  
2. **PRICE_btn**: 0.211531  
3. **total_btn_clicked**: 0.112964  
4. **time_spent_this_session**: 0.076386  
5. **HOME_btn**: 0.040848  
6. **total_pages_visited**: 0.027655  
7. **M_PRICE**: 0.026321  
8. **MEDIA_btn**: 0.024939  
9. **max_loan_entry_this_visit**: 0.021113  
10. **instanceNumber**: 0.013950  
11. **is_loan**: 0.011513  
12. **operatingSystem**: 0.010141  
13. **NoOfVisits**: 0.009448  
14. **loan_entry_count**: 0.008664  
15. **is_old_lead**: 0.008272  
16. **sourceCampaign**: 0.007881  
17. **total_sections_visited**: 0.006990  
18. **projectId**: 0.006301  
19. **LOCATION_btn**: 0.005986  
20. **HOME**: 0.005701  
21. **PRICE**: 0.005598  
22. **M_HOME**: 0.005563  
23. **max_loan_entry_this_week**: 0.005389  
24. **PLAN_btn**: 0.005033  
25. **systime_since_first_event_this_week**: 0.004930  
26. **cummulativeTimeSpent**: 0.004909  
27. **map_entry_count**: 0.004674  
28. **time_since_last_web_session**: 0.004646  
29. **M_LOCATION**: 0.004562  
30. **M_MEDIA**: 0.004409  
31. **recent_web_session_duration**: 0.004351  
32. **AMENITIES_btn**: 0.004344  
33. **LOCATION**: 0.004343  
34. **MEDIA**: 0.004313  
35. **SPECIFICATIONS**: 0.004267  
36. **recent_48_web_count**: 0.004263  
37. **avg_web_activity_duration**: 0.004025  
38. **recent_24_web_count**: 0.004005  
39. **max_web_duration**: 0.004002  
40. **AMENITIES**: 0.003973  
41. **SPECIFICATIONS_btn**: 0.003849  
42. **recent_24_cummulativeTimeSpent**: 0.003833  
43. **recent_48_cummulativeTimeSpent**: 0.003702  
44. **M_SPECIFICATIONS**: 0.003419  
45. **M_AMENITIES**: 0.003392  
46. **PLAN**: 0.003357  
47. **M_PLAN**: 0.002471  
48. **is_map**: 0.000000  
49. **OUR_PROJECTS**: 0.000000  
50. **NEARBY**: 0.000000  
51. **PARTNER_WITH_US**: 0.000000  
52. **LANDING**: 0.000000  
53. **M_OUR_PROJECTS**: 0.000000  
54. **M_NEARBY**: 0.000000  
55. **M_PARTNER_WITH_US**: 0.000000  
56. **M_LANDING**: 0.000000  
57. **LANDING_btn**: 0.000000  
58. **OUR_PROJECTS_btn**: 0.000000  
59. **ENQUIRE_btn**: 0.000000  
60. **EXPLORE_btn**: 0.000000  
61. **QR_btn**: 0.000000  
62. **BLOGS_btn**: 0.000000  
63. **PARTNER_WITH_US_btn**: 0.000000  
64. **EVENTS_btn**: 0.000000  
65. **POLLS/CCLEX011_btn**: 0.000000  
66. **LOCATION#:~:TEXT=..._btn**: 0.000000


---
---


| **Threshold** | **Confusion Matrix** | **Precision (0/1)** | **Recall (0/1)** | **F1-Score (0/1)** | **Accuracy** | **Macro Avg** | **Weighted Avg** |
|:---------------|:--------------------|:---------------------|:------------------|:--------------------|:--------------|:---------------|:-----------------|
| **0.1** | `[[1198256, 3745] [20594, 25491]]` | 0.98 / 0.87 | 1.00 / 0.55 | 0.99 / 0.68 | 0.98 | 0.93 / 0.78 / 0.83 | 0.98 / 0.98 / 0.98 |
| **0.2** | `[[1203898, 6243] [14952, 22993]]` | 0.99 / 0.79 | 0.99 / 0.61 | 0.99 / 0.68 | 0.98 | 0.89 / 0.80 / 0.84 | 0.98 / 0.98 / 0.98 |
| **0.3** | `[[1207166, 8444] [11684, 20792]]` | 0.99 / 0.71 | 0.99 / 0.64 | 0.99 / 0.67 | 0.98 | 0.85 / 0.82 / 0.83 | 0.98 / 0.98 / 0.98 |
| **0.4** | `[[1209668, 10499] [9182, 18737]]` | 0.99 / 0.64 | 0.99 / 0.67 | 0.99 / 0.66 | 0.98 | 0.82 / 0.83 / 0.82 | 0.98 / 0.98 / 0.98 |
| **0.5** | `[[1211670, 12350] [7180, 16886]]` | 0.99 / 0.58 | 0.99 / 0.70 | 0.99 / 0.63 | 0.98 | 0.79 / 0.85 / 0.81 | 0.99 / 0.98 / 0.99 |
| **0.6** | `[[1213326, 14572] [5524, 14664]]` | 1.00 / 0.50 | 0.99 / 0.73 | 0.99 / 0.59 | 0.98 | 0.75 / 0.86 / 0.79 | 0.99 / 0.98 / 0.99 |
| **0.7** | `[[1214792, 17159] [4058, 12077]]` | 1.00 / 0.41 | 0.99 / 0.75 | 0.99 / 0.53 | 0.98 | 0.70 / 0.87 / 0.76 | 0.99 / 0.98 / 0.99 |


---
---

### **Threshold: 0.1**  
**Confusion Matrix:**  
```
[[1198256    3745]
 [  20594   25491]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.98      1.00      0.99   1202001
           1       0.87      0.55      0.68     46085

    accuracy                           0.98   1248086
   macro avg       0.93      0.78      0.83   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.2**  
**Confusion Matrix:**  
```
[[1203898    6243]
 [  14952   22993]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1210141
           1       0.79      0.61      0.68     37945

    accuracy                           0.98   1248086
   macro avg       0.89      0.80      0.84   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.3**  
**Confusion Matrix:**  
```
[[1207166    8444]
 [  11684   20792]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1215610
           1       0.71      0.64      0.67     32476

    accuracy                           0.98   1248086
   macro avg       0.85      0.82      0.83   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.4**  
**Confusion Matrix:**  
```
[[1209668   10499]
 [   9182   18737]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1220167
           1       0.64      0.67      0.66     27919

    accuracy                           0.98   1248086
   macro avg       0.82      0.83      0.82   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.5**  
**Confusion Matrix:**  
```
[[1211670   12350]
 [   7180   16886]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1224020
           1       0.58      0.70      0.63     24066

    accuracy                           0.98   1248086
   macro avg       0.79      0.85      0.81   1248086
weighted avg       0.99      0.98      0.99   1248086
```

---

### **Threshold: 0.6**  
**Confusion Matrix:**  
```
[[1213326   14572]
 [   5524   14664]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       1.00      0.99      0.99   1227898
           1       0.50      0.73      0.59     20188

    accuracy                           0.98   1248086
   macro avg       0.75      0.86      0.79   1248086
weighted avg       0.99      0.98      0.99   1248086
```

---

### **Threshold: 0.7**  
**Confusion Matrix:**  
```
[[1214792   17159]
 [   4058   12077]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       1.00      0.99      0.99   1231951
           1       0.41      0.75      0.53     16135

    accuracy                           0.98   1248086
   macro avg       0.70      0.87      0.76   1248086
weighted avg       0.99      0.98      0.99   1248086
```

### Model (without URL influence)

| **Threshold** | **Train Accuracy** | **Train Precision** | **Train Recall** | **Train F1 Score** | **Val Accuracy** | **Val Precision** | **Val Recall** | **Val F1 Score** | **Test Accuracy** | **Test Precision** | **Test Recall** | **Test F1 Score** |
|:---------------|:------------------:|:-------------------:|:-----------------:|:------------------:|:-----------------:|:-------------------:|:----------------:|:-----------------:|:------------------:|:--------------------:|:----------------:|:-----------------:|
| **0.2**         | 0.9952             | 0.8015               | 0.9888             | 0.8853              | 0.9881             | 0.6248               | 0.8404             | 0.7167              | 0.9830             | 0.6060               | 0.7865             | 0.6845              |
| **0.3**         | 0.9968             | 0.8699               | 0.9776             | 0.9206              | 0.9891             | 0.6666               | 0.7796             | 0.7187              | 0.9839             | 0.6402               | 0.7112             | 0.6738              |
| **0.4**         | 0.9976             | 0.9162               | 0.9591             | 0.9372              | 0.9895             | 0.7013               | 0.7175             | 0.7093              | 0.9842             | 0.6711               | 0.6409             | 0.6557              |
| **0.45**        | 0.9977             | 0.9331               | 0.9465             | 0.9397              | 0.9896             | 0.7172               | 0.6854             | 0.7009              | 0.9844             | 0.6875               | 0.6096             | 0.6462              |
| **0.5**         | 0.9977             | 0.9474               | 0.9314             | 0.9393              | 0.9896             | 0.7327               | 0.6547             | 0.6915              | 0.9844             | 0.7017               | 0.5776             | 0.6336              |
| **0.6**         | 0.9974             | 0.9678               | 0.8909             | 0.9278              | 0.9893             | 0.7603               | 0.5849             | 0.6612              | 0.9839             | 0.7264               | 0.5016             | 0.5934              |
| **0.7**         | 0.9965             | 0.9828               | 0.8287             | 0.8992              | 0.9887             | 0.7900               | 0.5009             | 0.6131              | 0.9830             | 0.7485               | 0.4131             | 0.5324              |


# Model (with URL influence)

### **Feature Importance List**  
1. **if_maxweb_in_recent:** 0.255451  
2. **PRICE_btn:** 0.211654  
3. **total_btn_clicked:** 0.097836  
4. **time_spent_this_session:** 0.080458  
5. **HOME_btn:** 0.043188  
6. **M_PRICE:** 0.026505  
7. **MEDIA_btn:** 0.025767  
8. **max_loan_entry_this_visit:** 0.023338  
9. **total_pages_visited:** 0.019686  
10. **instanceNumber:** 0.015505  
11. **loan_entry_count:** 0.010185  
12. **operatingSystem:** 0.009920  
13. **URL_HIT_btn:** 0.008993  
14. **LOCATION_btn:** 0.008090  
15. **sourceCampaign:** 0.007971  
16. **is_loan:** 0.007802  
17. **cummulativeTimeSpent:** 0.007441  
18. **total_sections_visited:** 0.006536  
19. **projectId:** 0.006191  
20. **is_old_lead:** 0.006077  
21. **M_HOME:** 0.005623  
22. **PRICE:** 0.005542  
23. **M_MEDIA:** 0.005500  
24. **NoOfVisits:** 0.005497  
25. **recent_24_cummulativeTimeSpent:** 0.005111  
26. **AMENITIES_btn:** 0.005029  
27. **map_entry_count:** 0.004825  
28. **max_loan_entry_this_week:** 0.004685  
29. **PLAN_btn:** 0.004551  
30. **systime_since_first_event_this_week:** 0.004521  
31. **time_since_last_web_session:** 0.004520  
32. **M_LOCATION:** 0.004437  
33. **recent_web_session_duration:** 0.004418  
34. **SPECIFICATIONS_btn:** 0.004350  
35. **HOME:** 0.004293  
36. **recent_24_web_count:** 0.004280  
37. **SPECIFICATIONS:** 0.004235  
38. **AMENITIES:** 0.004192  
39. **LOCATION:** 0.004092  
40. **MEDIA:** 0.004001  
41. **max_web_duration:** 0.003781  
42. **avg_web_activity_duration:** 0.003758  
43. **M_SPECIFICATIONS:** 0.003694  
44. **recent_48_cummulativeTimeSpent:** 0.003663  
45. **recent_48_web_count:** 0.003614  
46. **PLAN:** 0.003469  
47. **M_AMENITIES:** 0.003416  
48. **M_PLAN:** 0.002309  
49. **is_map:** 0.000000  
50. **OUR_PROJECTS:** 0.000000  
51. **NEARBY:** 0.000000  
52. **PARTNER_WITH_US:** 0.000000  
53. **LANDING:** 0.000000  
54. **M_OUR_PROJECTS:** 0.000000  
55. **M_NEARBY:** 0.000000  
56. **M_PARTNER_WITH_US:** 0.000000  
57. **M_LANDING:** 0.000000  
58. **LANDING_btn:** 0.000000  
59. **OUR_PROJECTS_btn:** 0.000000  
60. **ENQUIRE_btn:** 0.000000  
61. **EXPLORE_btn:** 0.000000  
62. **QR_btn:** 0.000000  
63. **BLOGS_btn:** 0.000000  
64. **PARTNER_WITH_US_btn:** 0.000000  
65. **EVENTS_btn:** 0.000000  
66. **POLLS/CCLEX011_btn:** 0.000000  
67. **LOCATION#:~:TEXT=BE%20IT%20VIA%20THE%20BALANAGAR,THIS%20SPOT%20ENSURES%20GREAT%20CONNECTIVITY._btn:** 0.000000


---

| **Threshold** | **Confusion Matrix** | **Precision (0/1)** | **Recall (0/1)** | **F1-Score (0/1)** | **Accuracy** | **Macro Avg** | **Weighted Avg** |
|:---------------|:--------------------|:---------------------|:------------------|:--------------------|:--------------|:---------------|:-----------------|
| **0.1** | `[[1198390, 3728] [20460, 25508]]` | 0.98 / 0.87 | 1.00 / 0.55 | 0.99 / 0.68 | 0.98 | 0.93 / 0.78 / 0.83 | 0.98 / 0.98 / 0.98 |
| **0.2** | `[[1203920, 6225] [14930, 23011]]` | 0.99 / 0.79 | 0.99 / 0.61 | 0.99 / 0.69 | 0.98 | 0.89 / 0.80 / 0.84 | 0.98 / 0.98 / 0.98 |
| **0.3** | `[[1207150, 8289] [11700, 20947]]` | 0.99 / 0.72 | 0.99 / 0.64 | 0.99 / 0.68 | 0.98 | 0.85 / 0.82 / 0.83 | 0.98 / 0.98 / 0.98 |
| **0.4** | `[[1209484, 10215] [9366, 19021]]` | 0.99 / 0.65 | 0.99 / 0.67 | 0.99 / 0.66 | 0.98 | 0.82 / 0.83 / 0.83 | 0.98 / 0.98 / 0.98 |
| **0.5** | `[[1211297, 12080] [7553, 17156]]` | 0.99 / 0.59 | 0.99 / 0.69 | 0.99 / 0.64 | 0.98 | 0.79 / 0.84 / 0.81 | 0.99 / 0.98 / 0.98 |
| **0.6** | `[[1212952, 14064] [5898, 15172]]` | 1.00 / 0.52 | 0.99 / 0.72 | 0.99 / 0.60 | 0.98 | 0.76 / 0.85 / 0.80 | 0.99 / 0.98 / 0.99 |
| **0.7** | `[[1214408, 16452] [4442, 12784]]` | 1.00 / 0.44 | 0.99 / 0.74 | 0.99 / 0.55 | 0.98 | 0.72 / 0.86 / 0.77 | 0.99 / 0.98 / 0.99 |

---

### **Threshold: 0.1**  
**Confusion Matrix:**  
```
[[1198390    3728]
 [  20460   25508]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.98      1.00      0.99   1202118
           1       0.87      0.55      0.68     45968

    accuracy                           0.98   1248086
   macro avg       0.93      0.78      0.83   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.2**  
**Confusion Matrix:**  
```
[[1203920    6225]
 [  14930   23011]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1210145
           1       0.79      0.61      0.69     37941

    accuracy                           0.98   1248086
   macro avg       0.89      0.80      0.84   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.3**  
**Confusion Matrix:**  
```
[[1207150    8289]
 [  11700   20947]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1215439
           1       0.72      0.64      0.68     32647

    accuracy                           0.98   1248086
   macro avg       0.85      0.82      0.83   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.4**  
**Confusion Matrix:**  
```
[[1209484   10215]
 [   9366   19021]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1219699
           1       0.65      0.67      0.66     28387

    accuracy                           0.98   1248086
   macro avg       0.82      0.83      0.83   1248086
weighted avg       0.98      0.98      0.98   1248086
```

---

### **Threshold: 0.5**  
**Confusion Matrix:**  
```
[[1211297   12080]
 [   7553   17156]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       0.99      0.99      0.99   1223377
           1       0.59      0.69      0.64     24709

    accuracy                           0.98   1248086
   macro avg       0.79      0.84      0.81   1248086
weighted avg       0.99      0.98      0.98   1248086
```

---

### **Threshold: 0.6**  
**Confusion Matrix:**  
```
[[1212952   14064]
 [   5898   15172]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       1.00      0.99      0.99   1227016
           1       0.52      0.72      0.60     21070

    accuracy                           0.98   1248086
   macro avg       0.76      0.85      0.80   1248086
weighted avg       0.99      0.98      0.99   1248086
```

---

### **Threshold: 0.7**  
**Confusion Matrix:**  
```
[[1214408   16452]
 [   4442   12784]]
```

**Classification Report:**  
```
              precision    recall  f1-score   support

           0       1.00      0.99      0.99   1230860
           1       0.44      0.74      0.55     17226

    accuracy                           0.98   1248086
   macro avg       0.72      0.86      0.77   1248086
weighted avg       0.99      0.98      0.99   1248086
```

---

| **Threshold** | **Train Accuracy** | **Train Precision** | **Train Recall** | **Train F1 Score** | **Val Accuracy** | **Val Precision** | **Val Recall** | **Val F1 Score** | **Test Accuracy** | **Test Precision** | **Test Recall** | **Test F1 Score** |
|:---------------|:------------------:|:-------------------:|:-----------------:|:------------------:|:-----------------:|:-------------------:|:----------------:|:-----------------:|:------------------:|:--------------------:|:----------------:|:-----------------:|
| **0.2**         | 0.9952             | 0.8012               | 0.9887             | 0.8851              | 0.9882             | 0.6253               | 0.8439             | 0.7183              | 0.9831             | 0.6065               | 0.7871             | 0.6851              |
| **0.3**         | 0.9968             | 0.8685               | 0.9779             | 0.9200              | 0.9892             | 0.6667               | 0.7882             | 0.7224              | 0.9840             | 0.6416               | 0.7165             | 0.6770              |
| **0.4**         | 0.9975             | 0.9140               | 0.9590             | 0.9360              | 0.9895             | 0.6987               | 0.7257             | 0.7119              | 0.9843             | 0.6701               | 0.6506             | 0.6602              |
| **0.45**        | 0.9977             | 0.9324               | 0.9462             | 0.9393              | 0.9896             | 0.7135               | 0.6959             | 0.7046              | 0.9843             | 0.6818               | 0.6185             | 0.6486              |
| **0.5**         | 0.9977             | 0.9471               | 0.9311             | 0.9390              | 0.9896             | 0.7274               | 0.6655             | 0.6951              | 0.9843             | 0.6943               | 0.5868             | 0.6361              |
| **0.6**         | 0.9974             | 0.9679               | 0.8914             | 0.9281              | 0.9894             | 0.7556               | 0.6012             | 0.6696              | 0.9840             | 0.7201               | 0.5189             | 0.6032              |
| **0.7**         | 0.9965             | 0.9828               | 0.8273             | 0.8984              | 0.9889             | 0.7838               | 0.5244             | 0.6284              | 0.9833             | 0.7421               | 0.4373             | 0.5503              |



