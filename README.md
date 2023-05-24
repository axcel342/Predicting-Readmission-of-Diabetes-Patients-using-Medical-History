# Machine Learning Project: Predicting Patient Readmission

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Summary
This project focuses on developing and training a Decision Tree classification model using the Sklearn library to accurately predict patient readmission within 30 days, after several days, or no readmission, based on their medical history. By leveraging machine learning techniques, we aim to assist healthcare providers in identifying patients who are at a higher risk of readmission and enable proactive interventions.

## Technologies Used
- Python
- Flask
- Sklearn
- Pandas
- NumPy

## Dataset
The dataset used for this project is the "Diabetes 130-US hospitals for years 1999-2008" dataset, which can be accessed from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008).

This dataset contains information about patients who were admitted to 130 US hospitals between the years 1999 and 2008. It consists of various features related to patient demographics, medical history, medications, and lab test results. The goal is to predict whether a patient will be readmitted to the hospital within 30 days, after several days, or not readmitted.

Please follow the instructions on the UCI Machine Learning Repository website to download the dataset. Once downloaded, you can load the dataset into your project using Python libraries like Pandas or NumPy.

## Model Building
For this project, a **Decision Tree** classification model was built using Sklearn with the **entropy** criterion and a random state of 0. The model was trained on the prepared training data and predictions were made on the test data. Evaluation metrics such as **precision**, **recall**, and **F1-score** were used to assess the model's performance, along with a generated confusion matrix to visualize the predicted and actual values.

## Application Deployment
The application was deployed using Flask as the framework and Bootstrap on the frontend. Users can upload a csv file containing relevant information about the patient's medical history and a prediction.csv file is downloaded containing the prediction column.

## Evaluation Metrics
The model was evaluated using the following metrics:
- precision
- recall
- F1-score

## Conclusion
The model demonstrated promising performance in accurately classifying patients into categories of readmission within 30 days, after several days, or no readmission. The findings from this project have the potential to assist healthcare providers in identifying high-risk patients for proactive interventions, thereby improving patient care and reducing healthcare costs. Further enhancements could involve exploring ensemble methods or incorporating additional features to improve the model's predictive capabilities.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
