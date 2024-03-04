from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load breast cancer dataset
data = load_breast_cancer()

# Extract data from the dataset
label_names = data['target_names']
labels = data['target']
features_names = data['feature_names']
features = data['data']

# Display information about the dataset
print("Label Names:", label_names)
print("First Label:", labels[0])
print("First Feature Name:", features_names[0])
print("First Feature Values:", features[0])

# Split the data into training and testing sets
train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.40, random_state=3)

# Create and train a Gaussian Naive Bayes classifier
gnb = GaussianNB()
model = gnb.fit(train, train_labels)

# Make predictions on the test set
pred = model.predict(test)

# Display predictions and accuracy
print("Predictions:", pred)
print("Accuracy:", accuracy_score(test_labels, pred) * 100, "%")
