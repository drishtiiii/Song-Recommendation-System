import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("..."*120)
print("\t","\t","\t","\t","\t","\t","\t","Greetings")

def top10dance():
    #Top 10 songs danceability with artist names 
    df=pd.read_csv("audio1.csv")
    df
    df=pd.read_csv("audio1.csv",usecols=["danceability","artist_names"])
    df10=df.sort_values("danceability").head(10)
    print(df10)
    df10.plot(kind='bar', x="artist_names",title="Danceability Report",color="blue")
    plt.ylabel('dancebility')
    plt.show()

def  peak_rank():
    #songs peak rank
    df=pd.read_csv("audio1.csv", usecols=["artist_names","spotify_track_popularity","track_name"])
    df=df[df["artist_names"]=="Taylor Swift"]
    print(df)
    plt.xlabel("track_name")
    plt.ylabel("spotify_track_popularity")
    plt.title("peak_rank of your best artist")
    plt.plot(df.track_name,df.spotify_track_popularity , marker="*",markersize=10,color="red",linewidth=2,linestyle="dashdot")
    plt.show()
     
def songs_played():
     #duration_ms of artist
    df=pd.read_csv("audio1.csv", index_col=["artist_names"],usecols=["duration_ms","artist_names"])
    df2=df.groupby("artist_names").first()
    
    df2=df.sort_values("duration_ms", ascending=False).head(10)
    print(df2)
    exp=[0.1,0,0,0,0.2,0.1,0.1,0.1,0,0.1]
    plot = df2.plot.pie(y='duration_ms', figsize=(7, 7),explode=exp,autopct="%2.f",legend=False)
    plt.show()
      
while True:
    print("..."*120)
    print("\t","\t","\t","\t","\t","\t","\t","MENU")
    print("1. Top 10 songs you can groove on ")
    print("2. Get to know artist peak rank")
    print("3. Top 10 favourite long songs played")
    print("..."*120)
    a=input("Enter your Name ")
    ch=int(input("Enter your choice "))
    if ch==1:
        print("THANK YOU" , a)
        top10dance()
    elif ch==2:
        print("THANK YOU" , a)
        peak_rank()
    elif ch==3:
        print("THANK YOU" , a)
        songs_played()
        
