import streamlit as st
import yfinance as yf

st.title("4 3 3 INVESTED")
if "calculated" not in st.session_state:
    st.session_state.calculated = False

@st.cache_data(ttl=300)
def get_stock_price(ticker):
    if not ticker:
        return 0.0
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d") # 抓取最近一天的歷史資料
        if not hist.empty:
            return float(hist['Close'].iloc[-1]) # 取得最新收盤價
        else:
            return 0.0
    except:
        return 0.0

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Original")
    numbero = st.text_input("Stock ticker(Enter stock number .TW or .TWO)", value="00662.TW", key="numbero")
    numbero1 = st.number_input("Insert a number of shares", key="numbero1")
    numbero2=get_stock_price(numbero)
    if numbero2 > 0:
        st.success(f"Price: ${numbero2:,.2f}")
    else:
        st.error("Invalid Ticker")
    invested_o=numbero2*numbero1
    st.write(f"Original invested amount: ${invested_o:,.2f}")

with col2:
    st.header("Double")
    numberd = st.text_input("Stock ticker(Enter stock number .TW or .TWO)", value="00670L.TW", key="numberd")
    numberd1 = st.number_input("Insert a number of shares", key="numberd1")
    numberd2=get_stock_price(numberd)
    if numberd2 > 0:
        st.success(f"Price: ${numberd2:,.2f}")
    else:
        st.error("Invalid Ticker")
    invested_d=numberd2*numberd1
    st.write(f"Double invested amount: ${invested_d:,.2f}")
    

with col3:
    st.header("Cash")
    numberc = st.text_input("Stock ticker(Enter stock number .TW or .TWO)", value="00864B.TWO", key="numberc")
    numberc1 = st.number_input("Insert a number of shares", key="numberc1")
    numberc2=get_stock_price(numberc)
    if numberc2 > 0:
        st.success(f"Price: ${numberc2:,.2f}")
    else:
        st.error("Invalid Ticker")
    invested_c=numberc2*numberc1
    st.write(f"Cash invested amount: ${invested_c:,.2f}")

st.divider()
if st.button("Calculation ratio", type="primary"):
    st.session_state.calculated = True

# 只要狀態是 True (代表按過按鈕了)，就顯示下方的所有內容
if st.session_state.calculated:
 st.header("Investment Proportions")

 total_invested = invested_o + invested_d + invested_c
 st.write(f"**Total Invested Amount:** ${total_invested:,.2f}")

 if total_invested > 0:
    ratio_o = (invested_o / total_invested) * 100
    ratio_d = (invested_d / total_invested) * 100
    ratio_c = (invested_c / total_invested) * 100
    
    col_r1, col_r2, col_r3 = st.columns(3)
    col_r1.metric("Original Ratio", f"{ratio_o:.1f}%")
    col_r2.metric("Double Ratio", f"{ratio_d:.1f}%")
    col_r3.metric("Cash Ratio", f"{ratio_c:.1f}%")
 else:
    st.info("Please enter share prices and amounts to calculate proportions.")


 st.divider()
 st.header("Rebalance Plan to 4:3:3")
 option = st.selectbox(
    "How would you like to balance?",
    ("Trade", "Investing money"),
    index=None,
    placeholder="Select balance method...",)    
        
 def get_action_text(diff, price):
            if abs(diff) < 0.01:
                return "✅ Perfectly balanced!"
            
            action = "🟢 **BUY**" if diff > 0 else "🔴 **SELL**"
            amount = abs(diff)
            shares_text = ""
            
            if price > 0:
                shares = amount / price
                return f"{action}\n\nAdjustment amount: **${amount:,.2f}**\n\nCurrent stock price: **${price:,.2f}**\n\nRecommended number of shares: **{shares:,.2f}** shares"
            else:
                return f"{action}\n\n調整金額: **${amount:,.2f}**\n\n⚠️ *(請輸入有效股價以計算股數)*"
        
 if option == "Trade":
        target_o = total_invested * 0.4
        target_d = total_invested * 0.3
        target_c = total_invested * 0.3
        
        diff_o = target_o - invested_o
        diff_d = target_d - invested_d
        diff_c = target_c - invested_c
        
        col_a1, col_a2, col_a3 = st.columns(3)
        
        with col_a1:
            st.subheader("Original (40%)")
            st.write(f"Target: ${target_o:,.2f}")
            st.info(get_action_text(diff_o, numbero2))
            
        with col_a2:
            st.subheader("Double (30%)")
            st.write(f"Target: ${target_d:,.2f}")
            st.info(get_action_text(diff_d, numberd2))

        with col_a3:
            st.subheader("Cash (30%)")
            st.write(f"Target: ${target_c:,.2f}")
            st.info(get_action_text(diff_c, numberc2))

    # --- 方案 B：只投入新資金再平衡 (Investing money) ---
 elif option == "Investing money":
        # 1. 計算如果「不賣出任何部位」所需要達到的全新總資產規模
        new_total = max(
            invested_o / 0.4, 
            invested_d / 0.3, 
            invested_c / 0.3
        )
        
        # 2. 計算總共需要額外投入多少新資金
        money_to_add = new_total - total_invested
        st.success(f"💡 To balance without selling, you need to invest an additional: **${money_to_add:,.2f}**")
        
        # 3. 重新計算新的目標金額
        new_target_o = new_total * 0.4
        new_target_d = new_total * 0.3
        new_target_c = new_total * 0.3
        
        # 4. 重新計算差額 (因為是只買不賣，這些差額一定都會大於等於 0)
        diff_o_new = new_target_o - invested_o
        diff_d_new = new_target_d - invested_d
        diff_c_new = new_target_c - invested_c
        
        col_b1, col_b2, col_b3 = st.columns(3)
        
        with col_b1:
            st.subheader("Original (40%)")
            st.write(f"New Target: ${new_target_o:,.2f}")
            st.info(get_action_text(diff_o_new, numbero2))
            
        with col_b2:
            st.subheader("Double (30%)")
            st.write(f"New Target: ${new_target_d:,.2f}")
            st.info(get_action_text(diff_d_new, numberd2))

        with col_b3:
            st.subheader("Cash (30%)")
            st.write(f"New Target: ${new_target_c:,.2f}")
            st.info(get_action_text(diff_c_new, numberc2))
else:
 st.info("Please enter share prices and amounts to calculate proportions.")














