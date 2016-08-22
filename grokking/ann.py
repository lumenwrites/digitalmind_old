# neural network that takes in the input and uses weight to calculate prediction. 
def model(input, weight):
    prediction = input * weight
    return prediction

# Compare model's prediction to the goal prediction, return the error
def compute_error(input, weight, goal_prediction):
    prediction = model(input, weight)

    raw_error = prediction - goal_prediction
    # All errors are positive so that they don't cancel each other out
    # Squared to prioritize big errors over small ones
    normalized_error = raw_error ** 2

    return normalized_error

# Adjust weight up or down, return the one that reduces the error.
def fit(input, weight, goal_prediction, learning_rate):
    # Try using model to predict stuff
    prediction = model(input, weight)
    error = compute_error(input, weight, goal_prediction)

    print("Prediction: " + str(round(prediction, 8)))
    print("Error: " + str(round(error, 8)))

    # Gradient descent
    derivative = input * (prediction - goal_prediction)
    weight = weight - derivative    

    return weight


def train():        
    input = 0.5
    goal_prediction = 0.8

    # Initialize default random weight
    weight = 0.5
    # How much we're moving our weights each iteration
    learning_rate = 0.01

    # How many times to repeat learning
    epochs = 1101

    for iteration in range(epochs):
        # Improve the weight over a bunch of iterations.
        weight = fit(input, weight, goal_prediction, learning_rate)


train()        


    # # Hot cold
    # # Try increasing weight a bit, compute the error
    # up_weight = weight + learning_rate
    # up_error = compute_error(input, up_weight, goal_prediction)    

    # # Try decreasing weight a bit, compute the error    
    # down_weight = weight - learning_rate    
    # down_error = compute_error(input, down_weight, goal_prediction)    

    # # If decreasing weight minimizes the error decrease the weight
    # if down_error < up_error:
    #     weight = down_weight

    # # If increasing weight minimizes the error then increase it
    # if up_error < down_error:
    #     weight = up_weight
