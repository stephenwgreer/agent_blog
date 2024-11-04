from crewai import Task

marketing_analyst_task = Task(
    description="""
    Analyze the market trends in the banking sector and provide insights to the content strategist.
    """,
    expected_output="""
    A detailed analysis of the market trends in the banking sector with insights and recommendations for the content strategist.
    """,
    dependencies=[],
    completion_criteria="""
    """
)

content_outline_task = Task(
    description="""
    Create an outline and overall narration for the content strategy for the bank.
    """,
    expected_output="""
    A detailed outline and overall narration for the content strategy for the bank.
    """,
    dependencies=[],
    completion_criteria="""
    """
)

blog_output_task = Task(
    description="""
    Write up the content from the content strategist in accordance with the style guidelines.
    """,
    expected_output="""
    Engaging and informative content that resonates with the bank's target audience.
    """,
    dependencies=[],
    completion_criteria="""
    """
)

blog_editing_task = Task(
    description="""
    Review the content created by the writer and send it back for revision if necessary.
    """,
    expected_output="""
    Content that looks good and is free of errors before it is published.
    """,
    dependencies=[],
    completion_criteria="""
    """
)


