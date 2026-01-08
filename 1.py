import streamlit as st
import time
import numpy as np
import pandas as pd

st.title("大家好, 我叫廖益楷")
st.write("以下是我的自我介紹:")
st.session_state=False
自我介紹 = """
大家好，我叫 Ken Liao，目前就讀於暨南大學。課餘時間我喜歡打籃球，
透過運動來紓壓，希望可以中樂透然後直接休學。

下面是亂掰的,字多一點比較好看:)

(大家好，我叫小隨意，其實我每天最大的目標就是決定早餐吃什麼，
然後晚餐再決定要不要加點甜點。我喜歡看星星，也喜歡跟貓咪聊天，雖然牠們通常不回我。
我對程式有一點興趣，但大部分時間都在想「這個函數能不能幫我做一杯奶茶？」。
我會畫塗鴉，但畫出來常常被朋友說「這是抽象藝術嗎？」。
我愛亂買東西，尤其是奇怪的小玩意兒，像是可以跳舞的橡皮鴨或者會唱歌的鬧鐘。
我有時候會嘗試新的食譜，結果經常炸鍋或焦掉，但我還是樂此不疲。我也喜歡挑戰自己，
像是一次吃三種口味的冰淇淋，或者用左手刷牙。
總之，我就是一個喜歡嘗試、喜歡搞笑、有點隨性、有點奇怪，但又很努力活得開心的人。
希望以後能遇到更多和我一樣喜歡亂搞的人，一起分享生活的小確幸和奇怪的靈感！)
"""


def stream_data():
    for char in 自我介紹:
        yield char
        time.sleep(0.04)

if st.button("About me"):
    st.write_stream(stream_data)
if st.button("My photo"):
    st.session_state=True
if st.session_state:
    p = st.empty()
    p.progress(0, "Wait for it...")
    time.sleep(1)
    p.progress(50, "Wait for it...")
    time.sleep(1)
    p.progress(100, "Wait for it...")
    time.sleep(1)
    with p.container():
     st.image("image1.jfif", caption="海的對面是敵人")
if st.button("BACK"):
    st.write(" ")