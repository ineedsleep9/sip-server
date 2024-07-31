import json

file = "./src/pipeline/baseline_31July2024_eval_withconf.json"

data = []

with open(file, 'r') as f:
    data = json.load(f)

fails = []


for curr_dict in data[10]['failure_cases']:
    if(curr_dict['ground_truth'] != curr_dict['model_prediction']):
        curr_dict['false_positive'] = (curr_dict['model_prediction'][:1] == 'Y')
        curr_dict['false_negative'] = (curr_dict['model_prediction'][:1] == 'N')
        fails.append(curr_dict)
    
data[10] = {
    'id': "Failure Cases",
    'failure_cases': fails
}

with open("./src/pipeline/all_eval_results.json", 'w') as f:
    json.dump(data, f, indent=4)