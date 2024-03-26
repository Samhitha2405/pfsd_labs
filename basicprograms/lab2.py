from itertools import product

probabilities = {
    "Burglary": {"T": 0.001, "F": 0.999},
    "Earthquake": {"T": 0.002, "F": 0.998},
    "Alarm": {
        ("T", "T"): 0.95,
        ("T", "F"): 0.94,
        ("F", "T"): 0.29,
        ("F", "F"): 0.01,
    },
    "JohnCalls": {"T": 0.9, "F": 0.1},
    "MaryCalls": {"T": 0.7, "F": 0.3},
}


def compute_probability(event, probabilities):
    total_prob = 1.0
    for node, value in event.items():
        try:
            if isinstance(probabilities[node], dict):
                parents = tuple([event[parent] for parent in probabilities[node]])
                total_prob *= probabilities[node][parents][value]
            else:
                total_prob *= probabilities[node][value]
        except KeyError:
            pass
    return total_prob


def inference(evidence, query, probabilities):
    evidence.update(query)
    evidence_values = {node: ["T", "F"] for node in evidence.keys()}
    total_probability = 0.0
    for event in product(*[[(node, value) for value in values] for node, values in evidence_values.items()]):
        event_dict = dict(event)
        if all(event_dict[node] == evidence[node] for node in evidence):
            total_probability += compute_probability(event_dict, probabilities)
    return total_probability



evidence = {"JohnCalls": "T"}
query = {"Burglary": "F"}
result = inference(evidence, query, probabilities)
print("Probability of Burglary absent given John calls:", result)