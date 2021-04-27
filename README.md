# Orlando Job Market Data

> Gathering greater Orlando career opportunity data to empower job search.

**Code is being refactored**

## Overview of Project

[Orlando Job Market Data](https://github.com/JovaniPink/orlando-job-market-data) repo hold the folder structure and jupyter notebooks to gather career data from four job sites:

- [LinkedIn](https://www.linkedin.com/jobs)
- [Indeed](https://www.indeed.com/)
- [ZipRecruiter](https://www.ziprecruiter.com/)
- [Monster](https://www.monster.com/)

Currently I've only set up a web gathering job for Indeed an example csv file is located within data/processed folder:

HEADER
Index, Job Title, Location, Salary, Company, Job Rating, Post Time, Apply URL

EXAMPLE
| Index | Job Title | Location | Salary | Company | Job Rating | Post Time | Apply URL |
|-|-|-|-|-|-|-|-|
| 0 | Director of Technology | Ocala, FL | Not shown | R+L Global Logistics | 2.8 | today | https://www.indeed.com/viewjob?jk=b24eb9d1a3308a5b |
| 1 | PMO Senior Analyst, ISG Technology | Tampa, FL | Not shown | Citi | 3.9 | today | https://www.indeed.com/viewjob?jk=df91edf3091bad03 |
| 2 | Software Engineer | Orlando, FL | Not shown | LOCKHEED MARTIN CORPORATION | 4 | today | https://www.indeed.com/viewjob?jk=7d811c0a20b0f8c8 |
| 3 | Application developer | Tampa, FL | Not shown | IT Experts USA | | today | https://www.indeed.com/viewjob?jk=f6886167c6b289d1 |
| 4 | Documents Technology Sr. Project Manager | Tampa, FL | Not shown | Citi | 3.9 | today | https://www.indeed.com/viewjob?jk=cadc478dd4c6095f |
| 5 | Data Analyst | Orlando, FL | Not shown | LOCKHEED MARTIN CORPORATION | 4 | today | https://www.indeed.com/viewjob?jk=8869ccf911ead00a |
| 6 | IT Security Analyst | Kennedy Space Center, FL | Not shown | Jacobs | 3.9 | today | https://www.indeed.com/viewjob?jk=ee11eca42be1cfc0 |
| 7 | Documents Technology Project Manager | Tampa, FL | Not shown | Citi | 3.9 | today | https://www.indeed.com/viewjob?jk=63c94ccf177b8a4f |
| 8 | Junior Level PHP Developer | Tampa, FL | Not shown | American Partner Solutions | | today | https://www.indeed.com/viewjob?jk=83b636c528fcc91d |

## Installation

## **Requirements**

- Google Chrome version 84
- pip3: `pip3 install --upgrade pip`
- pipenv: `pip3 install pipenv`
- Python 3.8 or higher: will be automatically installed in the local virtual environment

## **Indeed Jobs Scraper setup**

1. Clone this repository in your machine
2. Traverse to the project directory and create a virtual environment:
   `pipenv install`
3. Run `pipenv run python indeed_crawler.py` to check it works.
   - It should open up a dialog saying: "Do you wish to scrape Indeed with the default search config?(yes/no)"
   - Enter "yes". It should look for Spanish teacher jobs in New York

## How to use Indeed Jobs Scraper

If you don't want to see how the bot interacts with the site through the browser open `config/driver_window.json`, change the `false` value to `true` and save it. This will minimize the browser.

To launch the bot, run `pipenv run python indeed_crawler.py`

Upon initiation, you will be prompted to either use the default search configuration or to create a new search.

If "yes" is entered, the bot will search with the parameters given in the previous search. To make a new search, enter "no".

You will be able to specify the following:

- **Country of search** (even if the job is remote, it will search for companies located wherever you specify)
- **The job title**
- **Specific location**: You can look for remote jobs or jobs located somewhere specifically
- **Your base salary**: This **will not filter out jobs not offering this salary** (since many of the posts don't show it). But it will be added as a search parameter
- **Job post recency**
- **Matching terms**: The bot will use your input to select or discard job posts containing specific terms. You can specify:
  - Words you want in the job title
  - Words you don't want in the job title
  - Words you want in the job description
  - Words you don't want in the description

You can also skip entering matching terms, in which case the bot will yield everything it finds with your search parameters.

Your search parameters and matching terms will be saved as default configuration. Therefore, in your next search you will only have to enter "yes" when prompted to use the default configuration.

#### **Warning**:

The logic behind the terms matching will make the bot bring you jobs which either title or description contains selected terms, provided either the description or the title doesn't contain unwanted terms.

This means that you might get jobs with unwanted terms in either the description or in the title because they contain wanted terms in one of those elements. Also you might see jobs which either the title or the description doesn't contain wanted terms because only one of them does.

This is done to make the crawling process more open so you don't miss out potentially interesting results. Nevertheless, the results should always have wanted terms at least in the title or in the description.

## What do you get at the end of the process?

You will get a csv file in the 'results' folder with:

- Jobs titles
- Jobs locations
- Jobs salaries (if shown)
- Companies names
- Jobs ratings (if shown)
- Post recency
- Jobs description
- Url to apply

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Everything :)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

1. Fork this repository;
2. Create your branch: `git checkout -b my-new-feature`;
3. Commit your changes: `git commit -m 'Add some feature'`;
4. Push to the branch: `git push origin my-new-feature`.

**After your pull request is merged**, you can safely delete your branch.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more information.
