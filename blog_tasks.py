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
    Do some research on the top 3 and then decide on 1 to be the blog based. 
    Create an outline and overall narration for the banking blog.
    """,
    expected_output="""
    A detailed outline and overall narration for the blog that 
    will resonate with a banker or bank technology enthusiast.
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
    An expert blog based on the outlines produced by the content strategist of no more than 1000 words. 
    Engaging and informative content that resonates with the bank's target audience.
    """,
    agent=writer,
    async_execution=False,
    context=[marketing_analyst_task, content_outline_task],
)

market_fact_check = Task(
    description="""
    Check the information within the first draft of the blog sent by the writer.
    Look online for any additional information that may be relevant.
    If the information is accurate or generally good, indicate that no changes need to be made.
    """,
    expected_output="""
    If changes required, return bulleted notes with additional changes that need to be made based on searches and analysis.
    """,
    agent=marketing_analyst,
    async_execution=False,
    context=[blog_output_task],
)

blog_revision_task = Task(
    description="""
    Rewrite the blog based on the notes and revisions of the market analyst.
    """,
    expected_output="""
    A revised blog including the notes and revisions made by the market analyst. 
    They should be checked again for any errors before being sent to the editor.
    """,
    agent=writer,
    async_execution=False,
    context=[blog_output_task, market_fact_check],
    output_file='blog-posts/new_post.txt'
)

final_editing_task = Task(
    description="""
    Review the content created by the writer and send it back for revision if necessary.
    The content should adhere to writing style given to the editor.
    """,
    expected_output="""
    A final revision of the content based on the style guide and relevant examples. 
    A file containing the finished blog post ready for publication.
    """,
    agent=editor,
    async_execution=False,
    context=[blog_output_task, market_fact_check, blog_revision_task]
)


