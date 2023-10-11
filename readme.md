## Remote sensing: auto-updating dataset information

Goal: automatically update a list of datasets used for machine learning in remote sensing.

This will be done leveraging a combination of webscraping and an LLM to process the information into a structured format. Basically, this will create an AWESOME list that is automatically maintained.

Note that is not possible with GPT-4 out of the box, the link reader/search pluging and the advanced data analysis (allowing to load an excel file) cannot be combined.

Starting point: the [list of datasets](https://ieeexplore.ieee.org/document/10213439) composed by (Schmitt et al., 2023).

Tasks:
1. Convert pdf with list of datasets to a more readable format
2. Get Langchain's [example](https://python.langchain.com/docs/use_cases/web_scraping#research-automation) web scraping working
3. Fill extra columns of the list: application, license, reference & link to Github/Zenodo
4. Add new datasets to the list
5. Write out new list

Task 1. was done by using Adobe's pdf to Excel [tool](https://www.adobe.com/be_en/acrobat/online/pdf-to-excel.html). However, it might be more interesting to convert it to a (sql) database format. This will be done in task 5. if necessary.

Possible prompt:
"In this excel, can you fill the last 3 columns for the first 10 items?
These are datasets for remote sensing, ie for training and validating deep learning methods. You will need to perform search to fill the last 3 columns, using the <dataset name> remote sensing as search criteria. The application column is the application domain, such as flooding, urban or land cover. The license column is the license of the data, often on github or zenodo. The last column is a link to the dataset or dataset paper; just paste any of the links you used to extract the data for previous two columns here."

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