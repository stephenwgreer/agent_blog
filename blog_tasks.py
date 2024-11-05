from crewai import Task
from blog_agents import marketing_analyst, content_strategist, writer, editor

marketing_analyst_task = Task(
    description="""
    Analyze the market trends in the banking sector and provide insights to the content strategist.
    """,
    expected_output="""
    A detailed analysis of the market trends in the banking sector with insights and recommendations for the content strategist.
    """,
    agent=marketing_analyst,
    async_execution=False
    
)

content_outline_task = Task(
    description="""
    Create an outline and overall narration for the content strategy for the bank.
    """,
    expected_output="""
    A detailed outline and overall narration for the content strategy for the bank.
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
    Engaging and informative content that resonates with the bank's target audience.
    """,
    agent=writer,
    async_execution=False,
    context=[marketing_analyst_task, content_outline_task],
)

market_fact_check = Task(
    description="""
    Write up the content from the content strategist in accordance with the style guidelines.
    """,
    expected_output="""
    Engaging and informative content that resonates with the bank's target audience.
    """,
    agent=writer,
    async_execution=False,
    context=[marketing_analyst_task, content_outline_task, blog_output_task],
)

blog_revision_task = Task(
    description="""
    Write up the content from the content strategist in accordance with the style guidelines.
    """,
    expected_output="""
    Engaging and informative content that resonates with the bank's target audience.
    """,
    agent=writer,
    async_execution=False,
    context=[blog_output_task, market_fact_check]
)

final_editing_task = Task(
    description="""
    Review the content created by the writer and send it back for revision if necessary.
    """,
    expected_output="""
    Content that looks good and is free of errors before it is published.
    """,
    agent=editor,
    async_execution=False,
    context=[blog_output_task, market_fact_check, blog_revision_task]
)


