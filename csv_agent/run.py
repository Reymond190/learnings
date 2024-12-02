

from langchain_community.chat_models import AzureChatOpenAI
from langchain_experimental.agents import create_csv_agent


llm = AzureChatOpenAI(
    openai_api_base="<yourapiurl>",
    openai_api_version="<api_version>",
    deployment_name="<yourmodel>",  
    openai_api_key="<yourapikey>",  
    openai_api_type="azure",
    temperature=0, # to ensure no hallucination
)


agent = create_csv_agent(llm,r"C:\Users\Downloads\test.csv\test.csv",verbose=True,allow_dangerous_code=True)

agent.run("how many rows are there?")

agent.run("What is the distribution of grades across all students?")

agent.run("What are the summary statistics (mean, median, mode, standard deviation) for the [specific column]")
