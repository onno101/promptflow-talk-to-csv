# promptflow-talk-to-csv

This repository contains artifacts for a solution that enables communication with CSV files using an Azure AI Studio prompt flow.

## Azure AI Studio Prompt Flow

The Azure AI Studio prompt flow is a powerful tool that allows you to create RAG flows in a seamless manner. It provides a user-friendly interface for building, validating and deploying RAG workflows. 

This prompt flow is designed to simplify the process of working with CSV files by providing a set of predefined prompts that guide you through the necessary steps. These prompts allow you to ask questions on the data in the CSV - and get an answer in natural language.

By leveraging the capabilities of Azure AI Studio, this prompt flow enables you to easily perform tasks such as data extraction and analysis on CSV files. Whether you are a data scientist, analyst, or developer, the Azure AI Studio prompt flow provides a convenient and efficient way to work with CSV data.

## Prompt flow benefits
Azure Machine Learning prompt flow offers several benefits for developing AI applications powered by Large Language Models (LLMs). Here are the key advantages:

1. Prompt Engineering Agility:
  - Interactive Authoring Experience: Azure Machine Learning prompt flow provides a visual representation of your project’s structure, making it easy to understand and navigate. It also offers a notebook-like coding experience for efficient flow development and debugging.
  - Variants for Prompt Tuning: You can create and compare multiple prompt variants, facilitating an iterative refinement process.
  - Built-in Evaluation Flows: Evaluate the quality and effectiveness of your prompts and flows using built-in evaluation tools.
2. Comprehensive Resources:
  - Azure Machine Learning prompt flow includes a library of built-in tools, samples, and templates. These resources serve as a starting point for development, inspire creativity, and accelerate the process.
3. Enterprise Readiness for LLM-based Applications:
  - Collaboration: Azure Machine Learning prompt flow supports team collaboration, allowing multiple users to work together on prompt engineering projects, share knowledge, and maintain version control.
  - All-in-One Platform: Streamline the entire prompt engineering process, from development and evaluation to deployment and monitoring. Deploy your flows as Azure Machine Learning endpoints and monitor their performance in real-time1.

In summary, Azure Machine Learning prompt flow simplifies prototyping, experimenting, iterating, and deploying AI applications powered by LLMs. It’s a versatile and intuitive tool for streamlined development! 😊🚀

## Functionality
This flow allows you to ask questions on CSV files in an Azure blob container. This allows use of natural languague in chat bots, and have its response fed by structured data, like CSV files. This example only uses CSV files, but it could be extended to any database that allows extraction of data through programmatical interfaces (e.g. SAP, SQL DBs, SaaS products with APIs).


## The flow
The flow takes an input, and should be a question on the data in the container. The `get_csv_config` takes examples of the csv files and adds it to the prompt of `get_sql_query`. That tool takes the input and the table samples and forms an SQL query that queries the data that can answer the initial question. As a next step `get_records` will execute the query against the csv files (using `pandasql`) and take the data of the relevant table. The last step `final_answer` will form an answer to the user using natural language.

![image](https://github.com/onno101/promptflow-talk-to-csv/assets/77727051/7c79e7ed-b41f-46db-8e40-7c1dc98ad15b)


## Alternatives

There are many alternatives available, by using packages/technologies like `pandasai`, `LangChain`, `Assistant API`, `Semantic Kernel`, or a combination of them. This flow is simply an example of how it could work, not definitively how it should.

## Getting Started

To get started with the prompt flow, follow these steps:

1. Clone this repository to your local machine.
2. Open the Azure AI Studio prompt flow in your preferred development environment.
3. Run the prompt flow and follow the prompts to interact with CSV files.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
