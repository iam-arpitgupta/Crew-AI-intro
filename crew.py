from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from task import research_task,write_task

#for calling this in a sequential manner
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential, #sequential task execution is default
    mempry=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)
#start the task execution process and enhanced feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL VS DATA SCIENCE'})
print(result)
