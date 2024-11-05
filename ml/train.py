import pandas as pd

from sklearn.model_selection import train_test_split as tts
from catboost import CatBoostClassifier, Pool

data = pd.read_csv("database/reviews.csv", delimiter=',')

X = data["review"].values.reshape(-1, 1)
Y = data["rate"].values.reshape(-1, 1)

x_train, x_val, y_train, y_val = tts(X, Y, random_state=42, test_size=0.2)

print(x_train.shape, y_train.shape)

train_pool = Pool(
    data=x_train,
    label=y_train,
    text_features=[0]
)
val_pool = Pool(
    data=x_val,
    label=y_val,
    text_features=[0]
)


model = CatBoostClassifier(
    iterations=1000,
    depth=8,
    eval_metric="TotalF1",
    task_type="CPU",
    od_wait=500,
    od_type="Iter",
    learning_rate=0.001
)

model.fit(
    train_pool,
    eval_set=val_pool,
    verbose=10,
    use_best_model=True
)

model.save_model("model_clf.cbm")