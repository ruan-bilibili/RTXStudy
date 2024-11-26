import streamlit as st
from streamlit_option_menu import option_menu
import base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found at: {image_path}")


# 配置网页
st.set_page_config(page_title="RTXStudy", layout="wide")

# 顶部导航栏
selected = option_menu(
    menu_title=None,  # 不显示标题
    options=["首页", "题库/模板", "课程", "会员"],  # 页面选项
    icons=["house", "book", "book-half", "person"],  # 图标选项
    menu_icon="cast",  # 导航栏图标
    default_index=0,  # 默认选中第一个
    orientation="horizontal",  # 横向布局
    styles={
        "container": {
            "padding": "10px!important",  # 增加内边距
            "background-color": "#999999",  # 背景颜色
        },
        "icon": {
            "color": "black", 
            "font-size": "24px",  # 增大图标字体
        },
        "nav-link": {
            "font-size": "20px",  # 增大文字字体
            "text-align": "center",
            "margin": "5px",  # 增加外边距
            "padding": "10px 15px",  # 增加链接按钮的内边距
            "--hover-color": "#eee",
        },
        "nav-link-selected": {
            "background-color": "#edeaea",
            "color": "black",
        },
    },
)







# 定义一个居中显示内容的函数
def centered_content(content_func):
    """将内容居中显示"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        content_func()

# 图片跳转链接生成函数
def clickable_image(image_path, target_url, caption=None):
    with open(image_path, "rb") as file:
        image_data = file.read()
        base64_image = base64.b64encode(image_data).decode()
    html_code = f"""
    <a href="{target_url}" target="_blank">
        <img src="data:image/png;base64,{base64_image}" alt="{caption}" style="width:100%; max-width:300px;"/>
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    if caption:
        st.caption(caption)

# 定义侧边栏介绍
def sidebar_info(page_name, description):
    """侧边栏内容"""
    with st.sidebar:
        st.title(f"{page_name} 介绍")
        st.write(description)

# 首页
if selected == "首页":
    #sidebar_info("首页", "这是首页，用于展示网站的基本信息，包括文字描述和图片内容。")
    with st.sidebar:
        st.title("首页介绍")
        st.write("这是首页，用于展示网站的基本信息，包括文字描述和图片内容。") 
        st.image("Image/gzh.jpg", caption="扫码关注阮同学的公众号")  
        st.markdown(
            """
            <div style="text-align: center;">
                <a href="https://space.bilibili.com/76702965?spm_id_from=333.1007.0.0" target="_blank">
                    <img src="data:image/png;base64,{}" alt="第一张图片" style="width:50%; max-width:300px;"/>
                </a>
                <p style="margin-top: 10px; font-size: 14px; color: #555;">点击跳转到阮同学的B站主页</p>
            </div>
            """.format(
                get_base64_image("Image/bili_icon.png")  # 获取图片的Base64数据
            ),
            unsafe_allow_html=True,
        )

    
    

    
    
    def homepage_content():
        #st.write("这里是首页，展示文字和图片。")
        #st.subheader("文字段落1")
        #st.write("这里是一段文字介绍，内容根据具体需求填充。")

       

        # 居中显示第一张图片
        col1, col2 = st.columns([1, 2])  # 左右两列布局，右侧宽度为左侧的两倍

        with col1:
            # 左侧图片部分
            st.markdown(
                """
                <div style="text-align: center;">
                    <a href="https://mp.weixin.qq.com/s/HZ0yeNR9tt2cmiQwMY4ryw?payreadticket=HPIMr8zEnyx32qYUkImwhVFcuMI0kIXiTxATxY2syY5WkL-bAdd84i_MEvrC_gkRT1KHMdw" target="_blank">
                        <img src="data:image/png;base64,{}" alt="第一张图片" style="width:100%; max-width:300px;"/>
                    </a>
                    <p style="margin-top: 10px; font-size: 28px; color: #000000;">25考研英语1大作文模板</p>
                </div>
                """.format(
                    get_base64_image("Image/fm1.png")  # 获取图片的Base64数据
                ),
                unsafe_allow_html=True,
            )
            

        with col2:
            # 右侧文字介绍部分
            st.markdown(
                """
                <div style="text-align: left;">
                    <h2 style="color: #000000;">模板介绍</h2>
                    <p style="font-size: 16px; color: #333333;">
                        本模板专为25考研英语1大作文设计，帮助考生快速掌握高分写作技巧。
                        点击左侧图片购买，获取更多详细内容。
                    </p>
                    <p style="font-size: 16px; color: #333333;">
                        模板内容包括：主题句、连接词、实用例句以及范文讲解，适合英语水平不同的考生。
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
           



        #st.subheader("文字段落2")
        #st.write("这里是另一段文字，介绍其他内容。")

        # 居中显示第二张图片
        col1, col2 = st.columns([1, 2])  # 左右两列布局，右侧宽度为左侧的两倍

        with col1:
            # 左侧图片部分
            st.markdown(
                """
                <div style="text-align: center;">
                    <a href="https://mp.weixin.qq.com/s/3cDPZh4fo03jumTke10trQ?payreadticket=HGrjpfu1eo-DL4tAlY5j8BarutizwojU9f3J0bBIDr-sY7fmUD0Nj9F8AM6rgRtv4ay3amQ" target="_blank">
                        <img src="data:image/png;base64,{}" alt="第一张图片" style="width:100%; max-width:300px;"/>
                    </a>
                    <p style="margin-top: 10px; font-size: 28px; color: #000000;">25考研英语2大作文模板</p>
                </div>
                """.format(
                    get_base64_image("Image/fm2.png")  # 获取图片的Base64数据
                ),
                unsafe_allow_html=True,
            )

        with col2:
            # 右侧文字介绍部分
            st.markdown(
                """
                <div style="text-align: left;">
                    <h2 style="color: #000000;">模板介绍</h2>
                    <p style="font-size: 16px; color: #333333;">
                        本模板专为25考研英语2大作文设计，帮助考生快速掌握高分写作技巧。
                        点击左侧图片购买，获取更多详细内容。
                    </p>
                    <p style="font-size: 16px; color: #333333;">
                        模板内容包括：主题句、连接词、实用例句以及范文讲解，适合英语水平不同的考生。
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )





    # 调用 homepage_content
    centered_content(homepage_content)


# 题库/模板
elif selected == "题库/模板":
    #sidebar_info("题库/模板", "这是题库/模板页面，用于展示题库或模板的内容，以图片的形式排列展示。")
    
    def templates_content():
        #st.write("这里展示题库/模板内容，图片分三列展示。")
        col1, col2, col3 = st.columns(3)
        with col1:
            clickable_image("Image/fm1.png", "https://mp.weixin.qq.com/s/HZ0yeNR9tt2cmiQwMY4ryw?payreadticket=HPIMr8zEnyx32qYUkImwhVFcuMI0kIXiTxATxY2syY5WkL-bAdd84i_MEvrC_gkRT1KHMdw", "25英语1大作文模板点击购买")
            clickable_image("Image/fm4.png", "https://mp.weixin.qq.com/s/cKP0qESla_5lA1qu4IT_Hw?payreadticket=HLTBG6hqy7iTDbiDIjoPDGBQJqfV_JIN0ZbLKjwPe6O6fDdgdtchel3cGrsNiqiZdOZj3Lo", "往年模板")
        with col2:
            clickable_image("Image/fm2.png", "https://mp.weixin.qq.com/s/3cDPZh4fo03jumTke10trQ?payreadticket=HGrjpfu1eo-DL4tAlY5j8BarutizwojU9f3J0bBIDr-sY7fmUD0Nj9F8AM6rgRtv4ay3amQ", "25英语2大作文模板点击购买")
        with col3:
            clickable_image("Image/fm3.png", "https://mp.weixin.qq.com/s/FnQukbaUVoQ57uzGNZ_xgQ?payreadticket=HIBTkh6BLsdFGdAGhpDpHpQHbkbhYKoPB8oAw-FkUsTmXvW1q0VHYAbrqVqVmrRByAdGwnw", "往年模板")
    
    centered_content(templates_content)

# 课程
elif selected == "课程":
    #sidebar_info("课程", "这是课程页面，包含课程描述和介绍内容。")
    
    def courses_content():
        #st.write("这里是课程页面，暂时仅有一段文字描述。")
        st.write("课程内容即将上线，敬请期待！")
    
    centered_content(courses_content)

# 会员
elif selected == "会员":
    #sidebar_info("会员", "这是会员页面，展示会员功能介绍。")
    
    def members_content():
        #st.write("这里是会员页面，暂时仅有一段文字描述。")
        st.write("会员功能即将上线，敬请期待！")
    
    centered_content(members_content)

