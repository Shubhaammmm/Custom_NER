# Custom NER

## Steps to run the system
1. Prepare training data
    + Open the URL - 
    annotate the data.
2. Download the config.cfg file using script
   Run the script config.sh using
   >./config.sh

2. Save the file to training_input.json
3. Run the script -> prepare_trainingdata.py using script
    > 
4. Run the script train.sh using
    > ./train.sh
5. Run the test using ```python3 test.py```

6. To Run the API Run the Script api.sh using 
   > ./api.sh
   or Run uvicorn Api:app --reload in the Terminal