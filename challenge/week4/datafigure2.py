# need to import json file 
import json 
import pandas as pd

# exception handler 
# test if target file exist 
# @return param : times  and minutes



def analysis(file, user_id):

#    times = 0
#    minutes = 0

    try:
        df = pd.read_json(file)
    except ValueError:
        return 0, 0

    df = df[df['user_id'] == user_id].minutes

    return df.count(), df.sum()
    

    return times, minutes

def PlotData(user_id, total_minutes):
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x = user_id
    y = total_minutes

    ax.set_title("StudyData")
    ax.set_ylabel("Study Time")
    ax.set_xlabel("User ID")

