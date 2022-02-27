# Cluster and Survival Analysis of Breast Cancer Patients using Gene Expressions 

## Project Demo Youtube video : https://www.youtube.com/watch?v=Z_i_nRDbrGg

## Problem Statement:

Cancers are mainly attributed to mutations in the genetic sequence of a person.Abnormal genes induce abnormal cellular and tissue growth, which in turn forms cancer tumors at the mutated part of the body.Diagnosis of breast cancer is a straight-forward procedure but estimating an accurate prognosis or survival period is difficult.This project aims at providing insights into the survival estimation of patients by grouping them into different groups/clusters by performing clustering and survival analysis with the help of their gene expression data.

## Project Description:

In this project,by using the Gene Expression data of patients suffering from breast cancer in Machine Learning models, we are able to estimate the survival probability and survival duration of that patient, which further provides insights into the treatment procedures (for example, the need for surgery and other treatments). This helps hospitals and medical staff to understand the condition of the patient with breast cancer and decide what treatment is best for them. It also helps to decide whether they should avoid  unnecessary and futile procedures like surgeries for patients who belong to 'less likely to survive' cluster group. We are also able to analyze the relationship between the combination of genes expressed and how it contributes to their overall survival.The project takes in the patient information and processes it using clustering algorithm and survival curves analysis and outputs a number between 0-3, each number associated with a survival rate group (Example: Group 1 means high survival and Group 3 means low survival etc)


## Azure Technology Used :

An Azure VM (compute) is created in the Azure ML workspace and Azure Machine Learning (Jupyter Notebook) is used for the analysis,training and deployment of the model.The model is deployed using local ACI (Azure Container Instance) Web Servive and the output is obtained (A rest API link is generated which sends back the clustering result) by giving (test values or custom )input and running the approriate cells in the jupyter notebook.

## Summary
The steps followed in this project are:
* In Azure Machine Leaning studio, a compute instance is created and a jupyter notebook is created to run the project. 
* The necessary python libraries  and the gene expression datasets are loaded into the notebook.
* Preprocessing, EDA, visualization, normalization of the dataset is performed.
* K-Means Clustering model divides the dataset entries (ie, patients) into 4 groups. The survival analysis of the clusters and genes are made and the clusters are named as group 0,1,2,3 
* (Cluster 0 - The patient has BELOW AVERAGE RATE OF SURVIVAL.

   Cluster 1 - The patient has VERY LOW CHANCES OF SURVIVAL.

   Cluster 2 - The patient has a comparitively HIGH RATE OF SURVIVAL

   Cluster 3 - The patient has a ABOVE AVERAGE CHANCES OF SURVIVAL)
* Inferences of the genes expressed and their contribution to survival of a patient are made.
* For deployment, the model is trained (available in model.pkl file) and the model is registered with the name 'clusmod'

* ![image](https://user-images.githubusercontent.com/89789765/155899257-e1e0a428-b162-4ef1-8523-0d1f87e7c1ec.png)
* A deployment environment is created by giving the packages and dependencies used and iference configuration is also written.
* A scoring script is also written for loading and getting result (in the form of json) from the ACI Web servive (score.py file)

* The model is deployed to Azure Container Instance Web Service (with the selected memory and CPU configurations) where a rest API id generated for the deployment. We can enter the details of patients and the output is returned as the cluster number to which the patient belongs to.
* For input, we can use the details in the dataset or also we can give custom input values (to df_new).
* Run the jupyter notebook to see the deployment Demo: https://www.youtube.com/watch?v=Z_i_nRDbrGg
