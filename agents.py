from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

##create a senior blog content research
blog_researcher=Agent(
    role='Blog Researcher from YouTube Videos',
    goal='get the relevant video content for the topic {topic} from YT channel',
    verboe=True,
    memory=True,
    beckstory=(
        "expert in understanding video in AI Data Science , Machine Learning adn Gen AI and providing suggestion"
    ),
    tools=[],
    allow_delegation=True
)

##creating a senior blog writing agent with yt tool
blog_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video {topic}',
    verboe=True,
    memory=True,
    beckstory=(
        "with a flair for simplifying complex topics,you craft"
        "enaging narratives that captivate and educate , bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)
