from turtle import title
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
            if not os.path.exists(output_dir_path):
                os.makedirs(output_dir_path)
            print('csv path',root + file)
            df_raw = pd.read_csv(root + file)
            print('df_raw.shape',df_raw.shape)
            # Acc
            df_raw_Acc = df_raw[['Timestamp', 'AccX', 'AccY', 'AccZ']].iloc[-1000:]
            plt.subplot(3,1,1)
            plt.plot(df_raw_Acc.index, df_raw_Acc.AccX)
            plt.title('AccX')
            plt.subplot(3,1,2)
            plt.plot(df_raw_Acc.index, df_raw_Acc.AccY)
            plt.title('AccY')
            plt.subplot(3,1,3)
            plt.plot(df_raw_Acc.index, df_raw_Acc.AccZ)
            plt.title('AccZ')
            plt.tight_layout()
            output_path_acc = output_dir_path +'Acc.png'
            plt.savefig(output_path_acc,dpi=600, bbox_inches='tight')
            plt.close()
            # Gyro
            df_raw_Gyro = df_raw[['Timestamp', 'GyroX', 'GyroY', 'GyroZ']].iloc[-1000:]
            plt.subplot(3,1,1)
            plt.plot(df_raw_Gyro.index, df_raw_Gyro.GyroX)
            plt.title('GyroX')
            plt.subplot(3,1,2)
            plt.plot(df_raw_Gyro.index, df_raw_Gyro.GyroY)
            plt.title('GyroY')
            plt.subplot(3,1,3)
            plt.plot(df_raw_Gyro.index, df_raw_Gyro.GyroZ)
            plt.title('GyroZ')
            plt.tight_layout()
            output_path_acc = output_dir_path +'Gyro.png'
            plt.savefig(output_path_acc,dpi=600, bbox_inches='tight')
            plt.close()
            # Mag
            # df_raw_Mag = df_raw[['Timestamp', 'MagX', 'MagY', 'MagZ']]
            # plt.subplot(3,1,1)
            # plt.plot(df_raw_Mag.index, df_raw_Mag.MagX)
            # plt.title('MagX')
            # plt.subplot(3,1,2)
            # plt.plot(df_raw_Mag.index, df_raw_Mag.MagY)
            # plt.title('MagY')
            # plt.subplot(3,1,3)
            # plt.plot(df_raw_Mag.index, df_raw_Mag.MagZ)
            # plt.title('MagZ')
            # plt.tight_layout()
            # output_path_acc = output_dir_path +'Mag.png'
            # plt.savefig(output_path_acc,dpi=400, bbox_inches='tight')
            # plt.close()