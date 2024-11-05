from crewai import Crew, Process
from dotenv import load_dotenv
from Agent import marketing_analyst, content_strategist, writer, editor
from Task import marketing_analyst_task, content_outline_task, blog_output_task, market_fact_check, blog_revision_task

# Main
def main():
    # Load .env variables
    load_dotenv()

    crew = Crew(
        agents=[marketing_analyst, content_strategist, writer, editor],
        tasks=[
            marketing_analyst_task,
            content_outline_task,
            blog_output_task,
            market_fact_check,
            blog_revision_task,
        ],
        verbose=2,
        process=Process.sequential,
    )

    result = crew.kickoff()

    print("************ Results *************")
    print(result)


if __name__ == "__main__":
    main()