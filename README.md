# McGlynn MyMas Crew

The goal of this project is to learn how to go from “Prompts to Production,” in building a Multi-Agent system (MAS) for Product Feature Comparison. 
This collaborative multi-agent system is designed to help consumers make informed purchasing decisions by systematically gathering, analyzing, and presenting comprehensive product feature comparisons across multiple brands and companies.

## Prompts
Initial prompt for a Master Plan: 

Act as a consumer who wants to compare product features and options from many brands or companies for an informed decision.
Design a Multi-Agent System (MAS) using CrewAI.com framework. 
Write a 3-agent MAS master plan.  Describe each agent’s roles, responsibilities, skills, tasks, and output deliverables for the above purpose and output as a markdown format artifact. 

Other prompts are used to help create all files (main, crew, agents, tasks).

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

## Technical Overview
This project involved using various processes and tools (Anaconda navigator, Python, Visual Studio, GitHub and more) along with the Crewai framework. Three agents are set up to Analyze, Research, and Summarize the results. 

