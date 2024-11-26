import streamlit as st

# 初始化购买人数
if "purchase_count" not in st.session_state:
    st.session_state["purchase_count"] = 0

# Markdown 按钮的样式
markdown_button = """
<style>
.button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    outline: none;
    color: #fff;
    background-color: #4CAF50;
    border: none;
    border-radius: 15px;
    box-shadow: 0 9px #999;
}
.button:hover {background-color: #3e8e41}
.button:active {
    background-color: #3e8e41;
    box-shadow: 0 5px #666;
    transform: translateY(4px);
}
</style>
"""

st.markdown(markdown_button, unsafe_allow_html=True)

# 点击按钮功能
if st.button("跳转并购买"):
    # 购买人数增加
    st.session_state["purchase_count"] += 1
    # 跳转链接 (可替换为你的跳转目标)
    st.write("购买成功！跳转到 [商品页面](https://mp.weixin.qq.com/s?__biz=MzkzNDU0MjQ2NA==&mid=2247483698&idx=1&sn=6cbff36d7a90f0e1167e124ef878ed64&chksm=c2baecddf5cd65cbee95cff57e8cde7ece4a3e2b5ae9ee8753dc734bb21c034df78ea7474d61&payreadticket=HFvebtT2QhZ1v1DjXr_YI3np4FLZlHEdPcu95bc4N7cU1v-N966gfjrCAHdlWEfr1DnJLho#rd)")
    st.experimental_rerun()

# 显示购买人数
st.write(f"当前购买人数：{st.session_state['purchase_count']}")
