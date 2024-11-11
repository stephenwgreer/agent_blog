from crewai import Agent
# from tools.reddit_trends import RedditTrends
# from tools.youtube_trending import YouTubeTrendingSearchTool
from tools.google_news import GoogleNewsSearchTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import Tool
from typing import Optional
from pydantic import BaseModel, Field
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    WebsiteSearchTool,
    SerperDevTool
)

# Define schema for google search
class GoogleSearchSchema(BaseModel):
    """Schema for Google Search parameters"""
    query: str = Field(..., description="The search query to look up")

# Instantiate the agent tools
# reddit_trends = RedditTrends()
# youtube_trends = YouTubeTrendingSearchTool()
google_news = GoogleNewsSearchTool()
search = GoogleSerperAPIWrapper()
style_guide = DirectoryReadTool(directory='/style_guides')
file_tool = FileReadTool()
website_tool = WebsiteSearchTool()
serper_websearch_tool = SerperDevTool()

# Create the Google Search tool with schema
google_search = Tool(
    name="Google Search",
    description="Search Google for a given inquiry, helps the marketing analyst to gather information on the latest trends.",
    func=search.run,
    args_schema=GoogleSearchSchema
)

marketing_analyst = Agent(
    role="Market Analyst and Researcher",
    goal="To analyze the market trends in banking and provide insights to the content strategist.",
    backstory="""You are a market analyst and researcher working in the banking industry. 
    You are an expert in banking technology and the business of banking and have decades of experience.
    You work for a publication that helps clients understand the market trends in the banking sector. 
    You have been tasked with analyzing the market trends and providing insights to the content 
    strategist to help them create a content strategy for the bank. 
    Your goal is to review latest news sites and blogs to gather information on the latest trends then distill
    them into the top 3 themes. You also review and update blogs with additional notes sent from the editor.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True,
    #reddit_trends, youtube_trends, google_news, google_search
    tools=[serper_websearch_tool, website_tool]
)

content_strategist = Agent(
    role="Content Strategist and Analyst",
    goal="Topic selection and relevance. Assembles the right information. Chooses the appropriate themes that will resonate across technology and business. Creates the outline and overall narration for banking.",
    backstory="""You are a content strategist and analyst working for the publication specializing in bank technology and business trends.
    You are an expert in banking technology and the business of banking and have decades of experience.
    You have been tasked with creating a content strategy that will resonate with the bank's target audience.
    You take the topics from the market analyst and research the topics to create an outline and overall narration for the content strategy.
    You will always write up content with concrete examples to use in the text.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True,
    tools=[serper_websearch_tool, website_tool]
)

writer = Agent(
    role="Blog writer and creator. Copywriter",
    goal="Writes up the content from the content strategist in accordance with the style guidelines.",
    backstory="""You are a blog writer and creator working for a news organization that writes about banking technology.
    You have an excellent command of the English language and are skilled at creating engaging and informative content.
    You know how blogs generally look and are structured. All your content is SEO optimized and is written like a blog.
    Your goal is to create engaging and informative content that will resonate with bankers and banking technology enthusiasts.
    You know the right words to use and will use industry jargon where necessary.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True,
)

editor = Agent(
    role="Chief Editor and Proofreader",
    goal="Reviews content and sends it back for revision to the writer. Ensure that the content looks good.",
    backstory="""You are a chief editor and proofreader working for the news publication focused on banking.
    You review content created by the writer and ensure that it is free of errors before it is published.
    In the style_guide folder and using the style_guide tool, you will look at existing examples of style and tone and ensure that the content is consistent with the publication's style.
    Then you send it back for revision if necessary.
    """,
    verbose=True,
    memory=True,
    allow_delegation=True,
    tools=[style_guide, file_tool]
)