# Blogging Agents

This agent consists of **four** different component agents:

- **Market Analyst**
     - Role: Looks for relevant pieces of news or topics in blogs
- **Content Strategist**
    - Role: Topic selection and relevance. Assembles the right information. Creates the outline and overall narration. Chooses the appropriate themes
- **Writer**
    - Role: Writes up the content in accordance with the style guidelines
- **Editor**
    - Role: Reviews content and sends it back for revision to the writer


The workflow for the Agent model is as follows:
1. The **market analyst** looks for relevant news and articles from the last month and distills them down into the top 3 themes.
2. The **content strategist** researches each of themes and looks at which is the most popular. It then creates an outline with bullets of relevant content underneath each.
3. The **writer** then creates a first draft of the content and passes it to the **market analyst**.
4. The **market analyst** reviews against an additional web search to make sure the content is consistent. It passes any notes and changes to the **writer**.
5. The **writer** creates a revision of the content for the **editor**.
6. The **editor** ensures the content adheres to publisher style (existing example content which guides writing style), making any revisions necessary.

> Note that this agent service requires a subscription to Crew.AI 
>
> Go to [Crew.AI](https://app.crewai.com)

