# McGlynn MyMas Crew

This describes the **Product Feature Comparison Multi-Agent System (MAS)**.The goal of this project is to learn how to go from “Prompts to Production,” meaning how to build the system from the beginning until the end.
* This collaborative multi-agent system is designed to help consumers make informed purchasing decisions by systematically gathering, analyzing, and presenting comprehensive product feature comparisons across multiple brands and companies.
* Three agents are set up to Analyze, Research, and Summarize the results. 

## Prompts
Once the business goals and strategies are decided, prompts are created. This example is one main prompt for the Project Master Plan and states the goal for the target persona: 

"Act as a consumer who wants to compare product features and options from many brands or companies for an informed decision.
Design a Multi-Agent System (MAS) using CrewAI.com framework. 
Write a three-agent MAS master plan.  Describe each agent’s roles, responsibilities, skills, tasks, and output deliverables for the above purpose and output as a markdown format artifact."

 Then other prompts are used to help create all the code files (main, crew, agents, tasks).  It is an iterative process of crafting providing AI input, reviewing output, testing and carefully checking output.

## User Input
In this MAS, the user is prompted for three types of input:  "Product_Category.” "Target_Brands,” and “Needs Features.”  Any relevant input can be used, depending upon the users’ desires.

For example:  
Product Category: "Noise-canceling headphones"

Target Brands: "Sony, Bose, Apple, Beats"

Needs Features: "High-quality sound, long battery life, comfortable for extended wear, good noise cancellation, suitable for professional and personal use"
## Agents
Each agent is set up to accomplish one or more tasks; agents collaborate with each other.  The process starts effectively using better prompts with various AI assistants (Claude.ai, etc.)  and using their output to help create a project plan, do research, create code, and help with troubleshooting problems.  There are final output deliverables, including a report and various charts of comparative data as a result of the agent collaborations. 
### 1. Analyst Agent
Role: Problem Definition and Requirements Gathering Key Responsibilities:

* Define the scope of product comparison
* Identify critical feature categories and comparison criteria
* Establish evaluation framework and metrics
* Determine consumer decision-making priorities

Tasks:

* Create a structured feature comparison template
* Define weighted importance for different product attributes
* Develop initial set of comparative parameters
* Validate requirements with other agents

Output Deliverables:
* Comprehensive requirements document
* Feature comparison matrix template
* Weighted feature importance scorecard

### 2. Researcher Agent
Role: Information Collection and Data Aggregation Key Responsibilities:

* Gather detailed product specifications
* Collect pricing information
* Source user reviews and expert opinions
* Compile technical specifications from multiple sources

Tasks:

* Perform web research across manufacturer websites
* Collect product specification sheets
* Aggregate user reviews from verified platforms
* Cross-reference technical specifications
* Validate data accuracy and recency

Output Deliverables:

* Detailed product specification spreadsheet
* Aggregated user review summary
* Price comparison chart
* Source documentation log.

### 3. Summary Agent
Role: Findings Synthesis and Analysis Key Responsibilities:

* Consolidate research findings
* Perform comparative analysis
* Identify key similarities and differences
* Generate insights from collected data

Tasks:

* Normalize data across different product lines 
* Create comparative scoring mechanisms
* Highlight unique product strengths and weaknesses
* Develop preliminary comparative insights

Output Deliverables:

* Comparative analysis report
* Normalized feature comparison matrix
* Insights and trend identification document
* Comparative scoring spreadsheet

## Technical Overview and Stack
This project involved using various processes and tools (Anaconda navigator, Python, Visual Studio, GitHub and more) along with the Crewai framework (crew.ai). 

Technology Stack
* Framework: CrewAI
* Language: Python

The MAS was initially run on my local C: drive, for testing and trouble-shooting. Then it was moved to my crew.ai account via GitHub and run from there.

## Sample Output -  Comparative Scoring Spreadsheet Summary 
This is one portion of the entire output. The entire output includes text, comparative data, the best choice, and a chart of comparative scoring and more.

| Feature                      | Weight (%) | Score: Sony WH-1000XM5 | Score: Bose Noise Cancelling 700 | Score: Apple AirPods Max | Score: Beats Studio3 Wireless |
|------------------------------|------------|--------------------------|----------------------------------|--------------------------|-------------------------------|
| Sound Quality                | 30%        | 9 (2.7)                  | 8 (2.4)                          | 9 (2.7)                  | 7 (2.1)                       |
| Battery Life                 | 20%        | 10 (2.0)                 | 7 (1.4)                          | 7 (1.4)                  | 8 (1.6)                       |
| Comfort                      | 20%        | 9 (1.8)                  | 8 (1.6)                          | 8 (1.6)                  | 6 (1.2)                       |
| Noise Cancellation           | 20%        | 10 (2.0)                 | 9 (1.8)                          | 9 (1.8)                  | 7 (1.4)                       |
| Use Case                    | 10%        | 9 (0.9)                  | 8 (0.8)                          | 8 (0.8)                  | 7 (0.7)                       |
| **Total Score**             | 100%       | **9.4**                  | **8.0**                          | **8.5**                  | **7.0**                       |

## Potential Enhancements
* Machine learning for personalized preference adaptation.
* Allowing for more input types to expand this use case.
* Integration with product brand store APIs for real-time pricing.
* Validation of data by cross-checking brand websites and review websites.

## Limitations
* Requires detailed user input for accurate results.
* Relies on the trained data.

## Contributing
Contributions are welcome! To propose changes:

* Fork the repository.
* Create a new branch (feature/your-feature).
* Commit changes and open a pull request.
## License
This project is licensed under the MIT License.

## Contact
For questions or support, contact:

* Developer: Marianne McGlynn
* Email: marianne.mcglynn@gmail.com
* GitHub: https://github.com/mcglynn-m/McGlynnMAS.git

