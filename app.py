from dotenv import load_dotenv

load_dotenv()
#画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示される
#条件①：ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変える。
#条件②：用意する専門家の種類は近代美術家、書家、歴史家、陶芸家、古物鑑定士の5種類とする。
#条件③:「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用する
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from typing import Literal
def get_expert_response(input_text: str, expert_type: Literal['近代美術家', '書家', '歴史家', '陶芸家', '古物鑑定士']) -> str:
    system_messages = {
        '近代美術家': "あなたは優れた近代美術家です。芸術の歴史や技法に精通しており、創造的な視点で質問に答えます。",
        '書家': "あなたは熟練した書家です。書道の技術や歴史に詳しく、美しい文字を書く方法について助言します。",
        '歴史家': "あなたは知識豊富な歴史家です。過去の出来事や文化について深い理解を持ち、正確な情報を提供します。",
        '陶芸家': "あなたは経験豊かな陶芸家です。陶器の制作技術やデザインに精通しており、創作に関する質問に答えます。",
        '古物鑑定士': "あなたは信頼できる古物鑑定士です。骨董品や歴史的なアイテムの価値や真贋について専門的な知識を持っています。"
    }
    
    chat = ChatOpenAI(temperature=0)
    messages = [
        SystemMessage(content=system_messages[expert_type]),
        HumanMessage(content=input_text)
    ]
    response = chat(messages)
    return response.content

st.title("専門家に質問しよう！")
expert_type = st.radio(
    "専門家の種類を選んでください:",
    ('近代美術家', '書家', '歴史家', '陶芸家', '古物鑑定士')
)
input_text = st.text_input("質問を入力してください:")
if st.button("送信"):
    if input_text:
        answer = get_expert_response(input_text, expert_type)
        st.write("回答:")
        st.write(answer)
    else:
        st.write("質問を入力してください。")
from dotenv import load_dotenv
