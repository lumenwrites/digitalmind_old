Title: Learning rate schedule
Date: 2016-08-22
Status: Draft

So you can gradually decrease your learning rate. Learning rate schedule.
 
 Can decrease gradually based ln epoch, or in big drops at specific epochs.
 
 decay
 
 calculated with this formula
 
 drop based
 
 Dropping by half every specific number of epochs.
 
 you write a step_decay function and then just pass it to the thing.
 
 tips
 
 increase initial learning rate(coz it decays start with a large number)
 use large momentum(helps to make updates in the right direction when learning rate is small)
 experiment with different schedules. You dont know which one is the best one. Try ones that change exponentially or respond to accuracy of the model. Experiment to pick the best one.
 
