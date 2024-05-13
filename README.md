# promptflow-talk-to-csv

This repository contains artifacts for a solution that enables communication with CSV files using an Azure AI Studio prompt flow.

## Azure AI Studio Prompt Flow

The Azure AI Studio prompt flow is a powerful tool that allows you to create RAG flows in a seamless manner. It provides a user-friendly interface for building, validating and deploying RAG workflows. 

This prompt flow is designed to simplify the process of working with CSV files by providing a set of predefined prompts that guide you through the necessary steps. These prompts allow you to ask questions on the data in the CSV - and 

By leveraging the capabilities of Azure AI Studio, this prompt flow enables you to easily perform tasks such as data extraction and analysis on CSV files. Whether you are a data scientist, analyst, or developer, the Azure AI Studio prompt flow provides a convenient and efficient way to work with CSV data.

## Functionality
This flow allows you to ask questions on CSV files in an Azure blob container. This allows use of natural languague in chat bots, and have its response fed by structured data, like CSV files. This example only uses CSV files, but it could be extended to any database that allows extraction of data through programmatical interfaces (e.g. SAP, SQL DBs, SaaS products with APIs).


## The flow
The flow takes an input, and should be a question on the data on t

![image](https://github.com/onno101/promptflow-talk-to-csv/assets/77727051/7aed607c-988a-4761-8a25-94feaaf86622)



## Alternatives

There are many alternatives available, by using packages/technologies like pandasai, LangChain, Assistant API, Semantic Kernel, or a combination of them. This flow is simply an example of how it could work, not definitively how it should.

## Getting Started

To get started with the prompt flow, follow these steps:

1. Clone this repository to your local machine.
2. Open the Azure AI Studio prompt flow in your preferred development environment.
3. Run the prompt flow and follow the prompts to interact with CSV files.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
