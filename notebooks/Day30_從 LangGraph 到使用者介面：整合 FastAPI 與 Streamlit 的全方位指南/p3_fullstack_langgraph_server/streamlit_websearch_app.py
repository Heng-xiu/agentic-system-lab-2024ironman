import streamlit as st
from langchain.schema import HumanMessage, AIMessage
from langserve import RemoteRunnable
from typing import Optional

# 設置 LangServe 服務的 URL
API_URL = "http://localhost:8000/websearch/"
app = RemoteRunnable(API_URL)

def stream_app_catch_tool_calls(inputs, thread) -> Optional[AIMessage]:
    """
    流式處理應用程序並捕獲工具調用。

    Args:
        inputs (dict): 包含消息的輸入字典。
        thread (dict): 包含線程信息的字典。

    Returns:
        Optional[AIMessage]: 如果捕獲到工具調用,則返回包含工具調用的 AIMessage,否則返回 None。
    """
    tool_call_message = None
    assistant_response = ""
    for output in app.stream(inputs, thread, stream_mode="values"):
        for key, value in output.items():
            message = value["messages"][-1]
            if isinstance(message, AIMessage) and message.tool_calls:
                tool_call_message = message
            else:
                if isinstance(message, AIMessage):
                    assistant_response += message.content
                    st.write(message.content)
    return tool_call_message, assistant_response

# 設置頁面標題
st.title('網路查詢助手')
# 添加使用提示
st.markdown("---")
st.markdown("提示: 您可以詢問各種問題，例如 '2024 鐵人賽關於 LangGraph 文章' 或 '高雄推薦餐廳有哪些？'")

# 創建一個對話歷史列表來存儲對話
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# 顯示對話歷史
for message in st.session_state.conversation_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 創建聊天輸入
user_input = st.chat_input("請輸入您的查詢:")

if user_input:
    # 添加用戶輸入到對話歷史
    st.session_state.conversation_history.append({"role": "user", "content": user_input})
    
    # 在聊天界面顯示用戶輸入
    with st.chat_message("user"):
        st.write(user_input)

    # 處理用戶輸入
    with st.chat_message("assistant"):
        with st.spinner("正在處理您的查詢..."):
            try:
                thread = {"configurable": {"thread_id": "5"}}
                inputs = [HumanMessage(content=user_input)]
                
                tool_call_message, assistant_response = stream_app_catch_tool_calls(
                    {"messages": inputs},
                    thread
                )
                
                # 將助手的回應添加到對話歷史
                if assistant_response:
                    st.session_state.conversation_history.append({"role": "assistant", "content": assistant_response})
                else:
                    st.error("抱歉,我無法處理您的查詢。請稍後再試。")
                    st.session_state.conversation_history.append({"role": "assistant", "content": "抱歉,我無法處理您的查詢。請稍後再試。"})
                
            except Exception as e:
                st.error(f"發生錯誤: {e}")
                st.session_state.conversation_history.append({"role": "assistant", "content": f"發生錯誤: {e}"})
    # 強制重新運行應用以更新顯示
    st.rerun()

st.markdown("---")