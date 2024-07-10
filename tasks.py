from tools import yt_tool
from crewai import Task
from agents import blog_writer,blog_researcher

##research task
research_task = Task(
    description=(
        "identify the topic video {topic}."
        "get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraphs long report bosed on the {topic} of video content.',
    tools=[yt_tool],
    agent=blog_researcher,
)

#writing task with language model configuration
write_task = Task(
    description=(
        "get info from the youtube channel on the topic {topic} ."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.'
                    'and create the content for the blog',
    tools=[yt_tool],
    agent=blog_researcher,
    async_execution=False,
    output_file='new-blog-post.md' # example of output generation
)
