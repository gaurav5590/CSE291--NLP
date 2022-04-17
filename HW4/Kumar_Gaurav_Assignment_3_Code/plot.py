# Plotting the graph
import pickle
import numpy as np
import matplotlib.pyplot as plt
data = pickle.load(open('models/metrics_plot.pkl','rb'))


## Plotting loss epoch  wise


epochs_to_plot = 20
train_loss = []

for key in data[0].keys():
  train_loss.append(data[0][key])

train_loss_filtered = []
for tr in train_loss:
  train_loss_filtered+=[x for i, x in enumerate(tr) if (i+1)%50==0]

loss_input = list(range(1,len(train_loss_filtered)+1))
print(len(loss_input))
input_ticks = [i for i in loss_input if i%4==0]
batch_labels = list(range(1,len(loss_input)+1))

plt.title("Training and Validation Loss plot for 20 epochs.")
plt.xlabel("Training Progress (Epoch)")
plt.ylabel("Training loss")
plt.xticks(input_ticks, batch_labels)
plt.plot(loss_input, train_loss_filtered)

valid_loss = list(data[1].values())[:epochs_to_plot]
plt.plot(input_ticks, valid_loss)



## Plotting other metrics


# import pickle
# %matplotlib inline
# import numpy as np
# import matplotlib.pyplot as plt
# data = pickle.load(open('metrics_plot.pkl','rb'))
# ## Plotting loss epoch  wise
# epochs_to_plot = 20
# #train_loss_filtered = [x for i, x in enumerate(data[0])]
# train_loss = list(data[9].values())[:epochs_to_plot]
# valid_loss = list(data[8].values())[:epochs_to_plot]
# epoch_num = list(range(1,len(train_loss)+1))[:epochs_to_plot]
# input_ticks = [i for i in range(30) if i%2==0]
# plt.title("Unlabeled and Labeled Complete Match")
# plt.xlabel("Epoch Number")
# plt.ylabel("Score")
# plt.xticks(input_ticks, input_ticks)
# #plt.ylim(4,8)
# plt.plot(epoch_num, train_loss, label='Unlabeled CM.')
# plt.plot(epoch_num, valid_loss, label='Labeled CM.')
# plt.legend()