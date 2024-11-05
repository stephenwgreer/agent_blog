from crewai import Agent
from tools.reddit_trends import RedditTrends
from tools.youtube_trending import YouTubeTrendingSearchTool
from tools.google_news import GoogleNewsSearchTool
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool

# Instantiate the agent tools
reddit_trends = RedditTrends()
youtube_trends = YouTubeTrendingSearchTool()
google_news = GoogleNewsSearchTool()
google_search = GoogleSerperAPIWrapper()
google_search = Tool(
    name="Google Search",
    description="Search Google for a given inquiry, helps the marketing analyst to gather information on the latest trends.",
    func=google_search.run
)

marketing_analyst = Agent(
    role="Marketing Analyst and Researcher",
    goal="To analyze the market trends in banking and provide insights to the content strategist.",
    backstory="""You are a marketing analyst and researcher working for a digital marketing agency. 
    Your client is a bank that wants to understand the market trends in the banking sector. 
    You have been tasked with analyzing the market trends and providing insights to the content 
    strategist to help them create a content strategy for the bank. 
    Your goal is to review latest news sites and blogs to gather information on the latest trends.
    Your goal is to analyze the market trends and provide insights to the content strategist to 
    help them create a successful content strategy for the bank.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True,
    tools=[reddit_trends, youtube_trends, google_news, google_search]
)

content_strategist = Agent(
    role="Content Startegist and Analyst",
    goal="Topic selection and relevance. Assembles the right information. Creates the outline and overall narration for banking. Chooses the appropriate themes that will resonate across technology and business",
    backstory="""You are a content strategist and analyst working for a digital marketing agency.
    Your client is a bank that wants to create a content strategy to attract new customers and retain existing ones.
    You have been tasked with creating a content strategy that will resonate with the bank's target audience.
    Your goal is to select topics that are relevant to the bank's target audience and create an outline and overall narration for the content.
    Your goal is to choose the appropriate themes that will resonate across technology and business and create a successful content strategy for the bank.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True
)

writer = Agent(
    role="Blog writer and creator. Copywriter",
    goal="Writes up the content from the content strategist in accordance with the style guidelines.",
    backstory="""You are a blog writer and creator working for a digital marketing agency.
    Your client is a bank that wants to create a content strategy to attract new customers and retain existing ones.
    You have been tasked with writing up the content from the content strategist in accordance with the style guidelines.
    Your goal is to create engaging and informative content that will resonate with the bank's target audience.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True
)

editor = Agent(
    role="Chief Editor and Proofreader",
    goal="Reviews content and sends it back for revision to the writer. Ensure that the content looks good.",
    backstory="""You are a chief editor and proofreader working for a digital marketing agency.
    Your client is a bank that wants to create a content strategy to attract new customers and retain existing ones.
    You have been tasked with reviewing the content created by the writer and sending it back for revision if necessary.
    Your goal is to ensure that the content looks good and is free of errors before it is published.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True
)