import math

# Sample dataset: [Outlook, Temperature, Humidity, Wind, PlayTennis]
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    label_counts = {}
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1
    ent = 0.0
    for count in label_counts.values():
        prob = count / total
        ent -= prob * math.log2(prob)
    return ent

def split(data, index, value):
    return [row for row in data if row[index] == value]

def choose_best_feature(data, features):
    base_entropy = entropy(data)
    best_gain = 0.0
    best_index = -1
    for i in range(len(features)):
        values = set(row[i] for row in data)
        new_entropy = 0.0
        for value in values:
            subset = split(data, i, value)
            prob = len(subset) / len(data)
            new_entropy += prob * entropy(subset)
        info_gain = base_entropy - new_entropy
        if info_gain > best_gain:
            best_gain = info_gain
            best_index = i
    return best_index

def majority_class(data):
    labels = [row[-1] for row in data]
    return max(set(labels), key=labels.count)

def build_tree(data, features):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if len(features) == 0:
        return majority_class(data)

    best_index = choose_best_feature(data, features)
    best_feature = features[best_index]
    tree = {best_feature: {}}
    values = set(row[best_index] for row in data)

    for value in values:
        subset = split(data, best_index, value)
        sub_features = features[:best_index] + features[best_index+1:]
        sub_data = [row[:best_index] + row[best_index+1:] for row in subset]
        tree[best_feature][value] = build_tree(sub_data, sub_features)

    return tree

decision_tree = build_tree(dataset, features)
print("Decision Tree:")
print(decision_tree)
