import streamlit as st
import datetime

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    # セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('こども(18才未満)', '大人(18才以上)')
    )

    # ラジオボタン
    sex_category = st.radio(
        '性別',
        ('男', '女', 'その他')
    )

    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理')
    )

    # チェックボックス
    mail_subscride = st.checkbox('メールマガジンを購読する。')
    # スライダー
    height = st.slider('身長', value=164, min_value=110, max_value=210)
    # 日付
    start_date = st.date_input('開始日', datetime.date(2022, 10, 21))

    # カラービッカー
    color = st.color_picker('テーマカラー', '#00f900')

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ!{name}さん!{address}に書籍送りました。')
        st.text(f'年齢層：{age_category}')
        st.text(f'性別：{sex_category}')
        st.text(f'趣味：{",".join(hobby)}')
        if mail_subscride:
            st.text('メールマガジンを購読します。')
        else:
            st.text('メールマガジンを購読しません。')

        st.text(f'身長：{height}cm')
        st.text(f'開始日付：{start_date}')
