# Azure-Final-ML-Project

Cluster and Survival Analysis of Breast Cancer Patients using Gene Expressions 


## Problem Statement:

Cancers are mainly attributed to mutations in the genetic sequence of a person.Abnormal genes induce abnormal cellular and tissue growth, which in turn forms cancer tumors at the mutated part of the body.Diagnosis of breast cancer is a straight-forward procedure but estimating an accurate prognosis or survival period is difficult.This project aims at providing insights into the survival estimation of patients by grouping them into different groups/clusters by performing clustering and survival analysis with the help of their gene expression data.

## Project Description:

In this project,by using the Gene Expression data of patients suffering from breast cancer in Machine Learning models, we are able to estimate the survival probability and survival duration of that patient, which further provides insights into the treatment procedures (for example, the need for surgery and other treatments).We are also able to analyze the relationship between the combination of genes expressed and their overall survival.


## Azure Technology Used :

An Azure VM (compute) is created in the Azure ML workspace and Azure Machine Learning (Notebook) is used for the analysis,training and deployment of the model.Azure Blob Storage is also used for storing necessary files.The model is deployed using local docker container and the output is obtained by giving (test values or custom )input and running the approriate cells in the jupyter notebook  
