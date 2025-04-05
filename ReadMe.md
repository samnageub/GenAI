Steps: 
1- Install Ollama locally https://ollama.com/download/windows
2- Pip Install the following libraries
    streamlit
    langchain_core
    langchain_community
    langchain_ollama
    pdfplumber
3- Unpack deepseek: Pick desired model per your local machine performance: I picked 1.5b : Run this  command in your terminal where you installed Ollama
    ollama run deepseek-r1:1.5b
4- Copy code in app.py in github and customize it if needed
5- Deploy the app locally by running this command in terminal: 
    streamlit run app.py
6- Enjoy DeepSeek in your local machine: http://localhost:8501/
7- Deploy the rag_deep locally by running this command in terminal: 
    streamlit run rag_deep.py
8- Enjoy DeepSeek with RAG in your local machine to ask qustions about specfic private documents in your local machine : http://localhost:8501/
9-added new file for speed hackathon Smart Traffic Management


