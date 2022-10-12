import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = 'data/'
output_dir = 'output/img/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for root , dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.csv'):
            output_dir_path = output_dir + '/' + file[:-4] + '/'

            print('reading file: ' + file)
            df_raw = pd.read_csv(root + '/' + file,usecols = ['GyroX', 'GyroY',
       'GyroZ', 'AccX', 'AccY', 'AccZ', 'MagX', 'MagY', 'MagZ','WatchGyroX',
       'WatchGyroY', 'WatchGyroZ', 'WatchAccX', 'WatchAccY', 'WatchAccZ'],index_col=False)
            
            print('Processing file: ' + file)
            # print(df_raw.keys())
            if os.path.exists(output_dir_path):
                continue
            len_phone = len(df_raw['GyroX'])
            len_watch = len(df_raw['WatchGyroX'])
            # Acc
            plt.subplot(3,1,1)
            plt.plot(df_raw['AccX'].values,label='AccX')
            plt.plot(df_raw['AccY'].values,label='AccY')
            plt.plot(df_raw['AccZ'].values,label='AccZ')
            plt.legend(loc='upper right')
            plt.title('Acc')
            # Gyro
            plt.subplot(3,1,2)
            plt.plot(df_raw['GyroX'].values,label='GyroX')
            plt.plot(df_raw['GyroY'].values,label='GyroY')
            plt.plot(df_raw['GyroZ'].values,label='GyroZ')
            plt.legend(loc='upper right')
            plt.title('Gyro')
            # Mag
            plt.subplot(3,1,3)
            plt.plot(df_raw['MagX'].values,label='MagX')
            plt.plot(df_raw['MagZ'].values,label='MagZ')
            plt.plot(df_raw['MagY'].values,label='MagY')
            # print(len_phone)
            # print(len(df_raw['MagZ']))
            plt.legend(loc='upper right')
            plt.title('Mag')
            plt.tight_layout()
            os.makedirs(output_dir_path)
            output_path_acc = output_dir_path +'sensors.png'
            plt.savefig(output_path_acc,dpi=400, bbox_inches='tight')
            plt.close()

            # Watch sensor
            # Acc
            plt.subplot(2,1,1)
            plt.plot(df_raw['WatchAccX'].values,label='AccX')
            plt.plot(df_raw['WatchAccY'].values,label='AccY')
            plt.plot(df_raw['WatchAccZ'].values,label='AccZ')
            plt.legend(loc='upper right')
            plt.title('Acc')
            # Gyro
            plt.subplot(2,1,2)
            plt.plot(df_raw['WatchGyroX'].values,label='GyroX')
            plt.plot(df_raw['WatchGyroY'].values,label='GyroY')
            plt.plot(df_raw['WatchGyroZ'].values,label='GyroZ')
            plt.legend(loc='upper right')
            plt.title('Gyro')
            plt.tight_layout()
            output_path_acc = output_dir_path +'watchSensors.png'
            plt.savefig(output_path_acc,dpi=400, bbox_inches='tight')
            print('Saved: ' + output_path_acc)
            plt.close()
            


