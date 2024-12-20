from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, List
import praw
import os
from datetime import datetime
from .helper_tools import remove_emojis

class RedditTrendsSchema(BaseModel):
    """Schema for Reddit Trends parameters"""
    subreddits: Optional[List[str]] = Field(
        default=None,
        description="List of subreddit names to scrape. Maximum of 3 subreddits."
    )

class RedditTrends(BaseTool):
    name: str = "Reddit Trends"
    description: str = "Fetches the latest trends from our favorite subreddits."
    args_schema: Optional[BaseModel] = None

    def __init__(self):
        super().__init__()
        self.args_schema = RedditTrendsSchema

    def _run(self, subreddits: Optional[List[str]] = None) -> dict:
        """
        Executes the Reddit API to scrape the top posts and their best two comments from specified subreddits.

        Parameters:
            subreddits (list of str): Optional; a list of subreddit names to scrape. If not provided, the function defaults to
                                      scraping posts from 'selfhosted', 'homelab', 'HomeNetworking', and 'HomeServer'.
                                      A maximum of three subreddits can be specified at a time.

        Returns:
            dict: A dictionary where each key is a subreddit and the value is a list of the top posts from that subreddit,
                  each post accompanied by its top two comments.

        Notes:
            Ensure that the subreddit names are correctly spelled and are existing subreddits on Reddit. The function is
            limited to scraping no more than three subreddits at once to maintain performance and adhere to API usage guidelines.
        """
        return self.scrape_reddit(subreddits)

    def scrape_reddit(self, subreddits=None):
        """
        Executes the Reddit API to scrape the top posts and their best two comments from specified subreddits.

        Parameters:
            subreddits (list of str): Optional; a list of subreddit names to scrape. If not provided, the function defaults to
                                      scraping posts from 'selfhosted', 'homelab', 'HomeNetworking', and 'HomeServer'.
                                      A maximum of three subreddits can be specified at a time.

        Returns:
            dict: A dictionary where each key is a subreddit and the value is a list of the top posts from that subreddit,
                  each post accompanied by its top two comments.

        Notes:
            Ensure that the subreddit names are correctly spelled and are existing subreddits on Reddit. The function is
            limited to scraping no more than three subreddits at once to maintain performance and adhere to API usage guidelines.
        """
        # Setup Credentials
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )

        if subreddits is None:
            subreddits = ["selfhosted", "homelab", "HomeServer"]

        if len(subreddits) > 3:
            raise Exception("Maximum of 3 subreddits at the time.")

        max_amount_of_posts = 3
        scrapped_reddit_data = {}
        
        for subreddit in subreddits:
            sub = reddit.subreddit(subreddit)
            
            for post in sub.hot(limit=max_amount_of_posts):
                posts = {
                    "title": remove_emojis(post.title),
                    "url": post.url,
                    "score": post.score,
                    "comments": [],
                    "created": datetime.utcfromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
                }

                try:
                    post.comments.replace_more(limit=0)
                    comments = post.comments.list()[:2]
                    
                    for comment in comments:
                        posts["comments"].append(remove_emojis(comment.body))
                        
                    scrapped_reddit_data.setdefault(sub.display_name, []).append(posts)
                    
                except praw.exceptions.APIException as e:
                    print(f"API exception occurred {e}")

        return scrapped_reddit_data