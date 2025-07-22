import asyncio
from agents import Agent, Runner, function_tool, FileSearchTool, Runner
from typing import Dict



@function_tool
async def get_leave_balance(employee_id: str):
  employee_data = [
      {
        "employee_id": "E101",
        "first_name": "Priya",
        "last_name": "Sharma",
        "basic_salary": 50000,
        "earn_leaves": 12,
        "sick_leaves": 7
      },
      {
        "employee_id": "E102",
        "first_name": "Rahul",
        "last_name": "Verma",
        "basic_salary": 65000,
        "earn_leaves": 15,
        "sick_leaves": 5
      },
      {
        "employee_id": "E103",
        "first_name": "Sneha",
        "last_name": "Patel",
        "basic_salary": 45000,
        "earn_leaves": 10,
        "sick_leaves": 8
      },
      {
        "employee_id": "E104",
        "first_name": "Amit",
        "last_name": "Singh",
        "basic_salary": 70000,
        "earn_leaves": 18,
        "sick_leaves": 6
      },
      {
        "employee_id": "E105",
        "first_name": "Divya",
        "last_name": "Reddy",
        "basic_salary": 55000,
        "earn_leaves": 11,
        "sick_leaves": 9
      }
    ]
  
  for rec in employee_data:
    if rec["employee_id"]== employee_id:
      earn_leaves = rec["earn_leaves"]
      sick_leaves = rec["sick_leaves"]
      basic_salary = rec["basic_salary"]
      return earn_leaves,sick_leaves,basic_salary


# Create the agent
leave_balance_agent = Agent(
    name="Leave Agent",
    instructions="""
                  You are a helpful assistant that can pull employee leave information from a database.
                  The database has first_name that equals name and last_name that equal surname of employees separated
                 """,
    tools=[get_leave_balance],  # Pass the list of tools
)


policy_search_agent = Agent(
    name="Assistant",
    tools=[
        FileSearchTool(
            max_num_results=1,  # Retrieve up to 3 results
            vector_store_ids=["vs_6817147711d88191964ef85a21ea57d5"] # Replace with your vector store ID
        )
    ]
)

triage_agent = Agent(
    name="Triage Agent",
    instructions= """
                  You determine which agent to use based on the user's question.
                  If the user us asking for specific leave balance please route him to the leave balance agent.
                  If the user us asking for policy details please route him to the policy search agent.
                  """,
    handoffs=[leave_balance_agent, policy_search_agent]
)


async def main():

  # Example usage
    print("\nRunning agent:")

    # print("Question : My employee_id is E102. How many earn leaves do I have ?")
    # result1 = await Runner.run(triage_agent, "My employee_id is E102. How many earn leaves do I have ?")
    # print(result1.final_output)
  
    # print("Question : How is a leave encashment calculated as per company policy ?")
    # result1 = await Runner.run(triage_agent, "How is a leave encashment calculated as per company policy ?")
    # print(result1.final_output)
  
    print("My employee id is E105.Please find my earn leave balance and basic salary.Once you have it please calculate my leave encashment amount?")
    result1 = await Runner.run(triage_agent, "My employee id is E105.\
                                              Please find my earn leave balance and basic salary.\
                                              Once you have it please calculate my leave encashment amount?")
    print(result1.final_output)
    
   

 
if __name__ == "__main__":
    asyncio.run(main())