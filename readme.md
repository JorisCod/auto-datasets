## Remote sensing: auto-updating dataset information

Goal: automatically update a list of datasets used for machine learning in remote sensing.

This will be done leveraging a combination of webscraping and an LLM to process the information into a structured format. Basically, this will create an AWESOME list that is automatically maintained.

Starting point: the [list of datasets](https://ieeexplore.ieee.org/document/10213439) composed by (Schmitt et al., 2023).

Tasks:
1. Convert pdf with list of datasets to a more readable format
2. Get Langchain's [example](https://python.langchain.com/docs/use_cases/web_scraping#research-automation) web scraping working
3. Fill extra columns of the list: application, license, reference & link to Github/Zenodo
4. Add new datasets to the list
5. Write out new list

Task 1. was done by using Adobe's pdf to Excel [tool](https://www.adobe.com/be_en/acrobat/online/pdf-to-excel.html). However, it might be more interesting to convert it to a (sql) database format. This will be done in task 5. if necessary.

### Set-up

Installation:

```bash
conda env create -f environment.yml
playwright install
playwright install-deps
```

Additionally, it is necessary to get the following API keys:
1. OpenAI API key
2. Google API key: https://developers.google.com/webmaster-tools/search-console-api/v1/configure

### How to run
```bash
python main.py
```