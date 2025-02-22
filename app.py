from crewai import Agent, Task, AgentPrompt, Crew
from crewai.tools import SearchTool

# --- Agent 1: Research Agent ---
agent_1 = Agent(
    name="research_agent",
    description="Expert researcher, synthesizing comprehensive information from credible sources.",
    goals=[
        "Well-organized research drafts with proper citations",
        "Provide relevant data from reliable sources",
        "Add references and citations (MLA style or as needed)",
        "Ensure clarity and coherence in the research content",
        "Synthesizing raw data into meaningful insights"
    ],
    allow_tools=["SearchTool"],
    tools=[SearchTool()]
)

# --- Agent 2: Content Writer ---
agent_2 = Agent(
    name="content_writer",
    description="Skilled at creating engaging blog posts while maintaining accuracy.",
    goals=[
        "Write concise content that flows logically",
        "Combine essential research findings into compelling copy",
        "Maintain correct structure, grammar, and style",
        "Provide well-edited content ready for publication"
    ],
    allow_tools=[],
    tools=[]
)

# --- Task Definition ---
research_tasks = Task(
    name="Research Tasks",
    instructions=[
        "Conduct comprehensive research on Google including:",
        "  1. Key industry trends and analysis",
        "  2. Relevant keywords and market insights",
        "  3. Statistical data related to relevant topics",
          "Evaluate source credibility and extract the best information",
          "Consolidate findings into a coherent research draft"
      ]
  )
  

agent_prompt = AgentPrompt(
      name="Output Format",
      instructions=[
          "Create a properly structured content/report",
          "Retain essential references from the original source text",
          "Ensure the content is ready to be handed off to the 'content_writer' agent for final publication"
      ]
  )
  

crew = Crew(
      agents=[agent_1, agent_2]
  )
  
result = crew.run(
      task=research_tasks,
      prompt=agent_prompt
  )
  
print(result)
