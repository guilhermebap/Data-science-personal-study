import streamlit as st

def main():
    #st.title('Hello World')
    #st.header('This is the header')
    #st.subheader('This is the subheader')
    #st.text('This is a text')
    #st.image('Logo.png')
    #x = 0
    #x = st.number_input('Número: ', None, None, x)
    #x = st.slider("Escolha: ", 0, 100, x)
    #st.write('O valor escolhido é ', x)
    st.markdown('Botão')
    bt = st.button('Botão')
    if bt:
    	st.markdown('Clicado')
    
    check = st.checkbox('Checkbox')
    if check:
    	st.markdown('Checado')

    st.markdown('Radio')
    radio = st.radio('Escolha as opções:', ['Opt 1', 'Opt 2'])
    if radio == 'Opt 1':
    	st.markdown('Opção 1 escolhida')
    	st.write('Opção 1 escolhida')
    	st.text('Opção 1 escolhida')
    elif radio == 'Opt 2':
    	st.markdown('Opção 2 escolhida')
    	st.write('Opção 2 escolhida')
    	st.text('Opção 2 escolhida')

    st.markdown('Select box')
    select = st.selectbox('Escolha a opção:', ['Opt 1', 'Opt 2'])
    if select == 'Opt 1':
    	st.markdown('Opção 1')
    elif select == 'Opt 2':
    	st.markdown('Opção 2')


    st.markdown('Multiselect')
    multi = st.multiselect('Escolha a opção:', ['Opt 1', 'Opt 2'])
    if multi == 'Opt 1':
    	st.markdown('Opção 1')
    elif multi == 'Opt 2':
    	st.markdown('Opção 2')

    st.markdown('File Uploader')
    file_uploaded = st.file_uploader('Choose your file:', type = 'csv')
    st.markdown(file_uploaded)

    if file_uploaded is not None:
    	st.markdown('Salvo')
    elif file_uploaded is None:
    	st.markdown('Vazio')


if __name__ == '__main__':
    main()