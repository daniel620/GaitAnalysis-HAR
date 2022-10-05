import scipy.stats as stats
import numpy as np
import pandas as pd
import os

# read scaled data
scaled_X = pd.read_csv('data/ScaledData.csv')

def get_frames(df, frame_size, hop_size):

    N_FEATURES = 10
    feature_list = [['heartrate', 'handAcc16_1', 'handAcc16_2',
       'handAcc16_3', 'handGyro1',
       'handGyro2', 'handGyro3', 'handMagne1', 'handMagne2', 'handMagne3']]

    frames = []
    labels = []
    for i in range(0, len(df) - frame_size, hop_size):
        # process bar
        print('\r', 'processing: ', i, '/', len(df) - frame_size, end='')
 
        temp_list = []
        for feature in feature_list:
            x = df[feature].values[i: i + frame_size]
            temp_list.append(x)

        
        # Retrieve the most often used label in this segment
        label = stats.mode(df['label'][i: i + frame_size])[0][0]
        # frames.append([x, y, z])
        frames.append(temp_list)
        labels.append(label)
        
        # Due memory limit
        FRAME_SIZE = 20000
        if i % FRAME_SIZE == 0 and i != 0:
            # Bring the segments into a better shape
            frames = np.asarray(frames).reshape(-1, frame_size, N_FEATURES)
            labels = np.asarray(labels)

            # print(x.shape, y.shape)
            # save data
            np.save('data/npy/x/x_{:d}.npy'.format(int(i/FRAME_SIZE)), frames)
            np.save('data/npy/y/y_{:d}.npy'.format(int(i/FRAME_SIZE)), labels)
            frames=[]
            labels=[]
    # return frames, labels

# samling frequency is 100Hz
Fs = 100
frame_size = Fs*4 # 80
hop_size = Fs*2 # 40
get_frames(scaled_X, frame_size, hop_size)
# x, y = get_frames(scaled_X, frame_size, hop_size)

# print(x.shape, y.shape)
# # save data
# np.save('data/x.npy', x)
# np.save('data/y.npy', y)