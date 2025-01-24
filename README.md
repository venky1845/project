# project
# PubMed Paper Analysis

## Overview
This project provides a Python-based framework to analyze papers from PubMed. It focuses on identifying papers with authors affiliated with non-academic organizations. The script fetches metadata about PubMed papers, filters authors based on their affiliations, and saves the results to a CSV file for further analysis.

## Features
- Fetch paper IDs based on a search query using PubMed APIs.
- Retrieve detailed metadata for each paper.
- Identify non-academic authors by analyzing author affiliations.
- Save the filtered results in a CSV file.

## Requirements
To run the code, you need the following dependencies:

- Python 3.6+
- Libraries:
  - `requests`
  - `xml.etree.ElementTree`
  - `pandas`
  - `fpdf` (for generating PDF reports)

You can install the required libraries using:
```bash
pip install requests pandas fpdf
```

## File Structure
- **main.py**: Contains the main script to execute the analysis.
- **results.csv**: Output file storing filtered paper details.
- **report.pdf**: (Optional) Generated report summarizing the methodology and results.

## How to Use

### 1. Define Your Query
Specify a search query to fetch relevant PubMed papers. Example:
```python
query = "Machine Learning in Medicine"
```

### 2. Run the Script
Execute the main function with your query:
```python
main(query, filename="results.csv")
```
This will:
- Fetch paper IDs matching the query.
- Retrieve metadata for each paper.
- Filter papers with non-academic authors.
- Save the filtered data to a CSV file.

### 3. Review Results
The output file (`results.csv`) will contain:
- PubMed ID
- Title
- Publication Date
- Non-academic Authors
- Company Affiliations

### 4. (Optional) Generate a Report
To create a PDF report summarizing the analysis, include:
```python
pdf = PDF()
# Add details to the PDF as needed
pdf.output("report.pdf")
```

## Functions

### `fetch_papers(query: str) -> list`
Fetches paper IDs from PubMed based on a search query.
- **Parameters**: `query` (str) - Search term.
- **Returns**: List of PubMed IDs.

### `fetch_paper_details(id: str) -> list`
Retrieves detailed metadata for a given paper ID and identifies non-academic authors.
- **Parameters**: `id` (str) - PubMed ID.
- **Returns**: List of dictionaries with filtered paper details.

### `filter_non_academic_papers(papers: list) -> list`
Filters papers with at least one non-academic author.
- **Parameters**: `papers` (list) - List of paper metadata.
- **Returns**: Filtered list of papers.

### `save_to_csv(papers: list, filename: str)`
Saves the filtered data to a CSV file.
- **Parameters**: `papers` (list) - Filtered paper details.
  `filename` (str) - Name of the output CSV file.

### `main(query: str, filename: str)`
Orchestrates the entire process of fetching, filtering, and saving results.
- **Parameters**: `query` (str) - Search term.
  `filename` (str) - Output CSV filename.

## Example Output

### Input
Search Query: `"Artificial Intelligence in Healthcare"`

### Output (results.csv)
| PubMedID     | Title                               | Publication Date | Non-academic Authors | Company Affiliations     |
|--------------|-------------------------------------|------------------|-----------------------|--------------------------|
| 12345678     | AI in Diagnostics                  | 2024-03-12       | John Doe             | HealthTech Inc.          |
| 87654321     | Machine Learning for Health        | 2025-01-15       | Jane Smith           | MedTech Corp.            |

## Notes
- Ensure a stable internet connection to interact with PubMed APIs.
- The code is modular and can be extended to include additional filters or output formats.

## License
This project is open-source and available for use under the MIT License.

