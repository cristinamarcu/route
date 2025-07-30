# Route fetch data and analysis 


## Spec 1

* Entry point is  [main_spec1.py](main_spec1.py). 
* The template for making a request (on which the campaign data is filled progamatically) is [request_body_spec1.json](request_body_spec1.json)
* [outputs_spec1](outputs_spec1) folder contains raw data returned by REST API
* [results_spec1](results_spec1) folder has the outputs aggregated and the PowerBI analysis

## Spec 2

* Entry point is [main_spec2.py](main_spec2.py).
* The template for making a request (on which the campaign data is filled progamatically) is [request_body_spec2.json](request_body_spec2.json) 
* [outputs_spec2](outputs_spec2) folder contains raw data returned by REST API
* [results_spec2](results_spec2)  folder has the outputs aggregated and the PowerBI analysis


## Extra info

* credentials and configuration are to be set in [credentials.py](credentials.py)
* output of metadata calls like demographics or environment are saved in the [metadata](metadata) folder
