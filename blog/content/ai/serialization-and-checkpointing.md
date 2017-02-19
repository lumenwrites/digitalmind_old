Title: Serialization and Checkpointing
Date: 2016-08-22
Status: Draft

Because deep learni models take a long time to train, we need to be able to be able to save our progress. This article is about serialization(saving the models on disk) and checkpointing(saving the best versions of our models.

we will learn it on the basis of the code from hello world tutorial.

# Saving the model

Saving models, and loading them to make predctions

Keras separates saving the model architecture and saving the weights.

Models can be saved as json, weights can be saved as hd5.

# Loading the model

# Checkpointing

Checkpointing is a fault tolerance technique for long running processes. You are regularly taking the model snapshots in case of failure, so that if there's a problem not everythig is lost.

Checkpoint can be used directly, lr as a starting point for a new run to pick up where it left off. Checkpointing captures the weights of the model.

Keras checkpointing api allows you to choose when to do the checkpoints. It is a good idea to save checkpoints every time the model improves. You can monitor various metrics. We will set it up so that it saves the weighhts every time there's an improvement in  classification accuracy.

'''

Saving the best weights

# Loadig a saved model


