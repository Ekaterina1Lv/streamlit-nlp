import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Aplikacja NLP – Hugging Face')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.info('Aplikacja służy do analizy tekstu angielskiego: sprawdza jego wydźwięk emocjonalny '
        'albo tłumaczy go na język niemiecki. Wybierz opcję, wpisz tekst po angielsku i czekaj na wynik.')

st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

with st.echo():
    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

df = pd.read_csv("DSP_4.csv", sep = ';')
st.dataframe(df)
# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Przetwarzanie języka naturalnego')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu (eng -> de)",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        try:
            with st.spinner('Analizuję tekst...'):
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
            st.success('Gotowe!')
            st.write(answer)
        except Exception as e:
            st.error(f'Błąd: {e}')

if option == "Tłumaczenie tekstu (eng -> de)":
    text = st.text_area(label="Wpisz tekst po angielsku")
    if text:
        try:
            with st.spinner('Tłumaczę tekst...'):
                translator = pipeline("translation_en_to_de")
                answer = translator(text)
            st.success('Tłumaczenie gotowe!')
            st.write(answer[0]['translation_text'])
        except Exception as e:
            st.error(f'Błąd: {e}')

st.write('Numer indeksu: s29858')