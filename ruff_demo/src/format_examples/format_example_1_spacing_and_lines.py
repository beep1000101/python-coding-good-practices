def train(model, X, y, lr=0.01, epochs=10, batch_size=32):
    preds = model(X)
    loss = ((preds-y)**2).mean()
    if lr > 0.001:
        print('Training with lr', lr)
    return loss


def evaluate(model, X, y):  result = model(X); acc = (
    result == y).sum()/len(y); print("acc:", acc); return acc


def predict(model, X): return model(X)
def ugly_math(a, b, c): return a+b*c - 2*a+b*c
