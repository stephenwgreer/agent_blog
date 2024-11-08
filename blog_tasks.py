from crewai import Task
from blog_agents import marketing_analyst, content_strategist, writer, editor

marketing_analyst_task = Task(
    description="""
    Analyze the market trends in the banking sector and provide insights to the content strategist.
    """,
    expected_output="""
    A detailed analysis of the recent market trends in the banking sector with insights and recommendations for the content strategist. 
    Content will be distilled down into the top 3 themes with a description of each.
    """,
    agent=marketing_analyst,
    async_execution=False
)

content_outline_task = Task(
    description="""
    Create an outline and overall narration for each of the top three trends identified by the market analyst.
    """,
    expected_output="""
    3 different themes with a detailed outline and overall narration for each theme that will resonate with a banker or bank technology enthusiast.
    """,
    agent=content_strategist,
    async_execution=False,
    context=[marketing_analyst_task], # This task cannot begin until the CONTEXT, ie previous task, is completed
)

blog_output_task = Task(
    description="""
    Write up the content from the content strategist in accordance with the style guidelines.
    """,
    expected_output="""
    3 different blogs based on the outlines produced by the content strategist of no more than 1000 words each. Engaging and informative content that resonates with the bank's target audience.
    """,
    agent=writer,
    async_execution=False,
    context=[marketing_analyst_task, content_outline_task],
)

market_fact_check = Task(
    description="""
    Check the information within the first draft of the blogs sent by the writer.
    """,
    expected_output="""
    Rearch each blog and teturn each of the 3 first drafts with bulleted notes below on additional changes that need to be made based on searches and analysis. Changes no not necessarily need to be made.
    """,
    agent=marketing_analyst,
    async_execution=False,
    context=[blog_output_task],
)

blog_revision_task = Task(
    description="""
    Rewrite the 3 blogs based on the notes and revisions of the market analyst.
    """,
    expected_output="""
    The 3 blogs revised to include the notes and revisions made by the market analyst. They should be checked again for any errors before being sent to the editor.
    """,
    agent=writer,
    async_execution=False,
    context=[blog_output_task, market_fact_check],
    output_file='blog-posts/new_post.txt'
)

final_editing_task = Task(
    description="""
    Review the content created by the writer and send it back for revision if necessary.
    """,
    expected_output="""
    The 3 blogs reviewed and sent back for revision if necessary. The content should adhere to writing style given to the editor.
    """,
    agent=editor,
    async_execution=False,
    context=[blog_output_task, market_fact_check, blog_revision_task]
)


