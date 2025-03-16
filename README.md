# FactCheck+ 🧐

FactCheck+ is a personal project to test how well LLMs can generate fact-checking reports given sources. It takes a claim that has already been fact-checked by [PolitiFact](https://www.politifact.com/), gathers the same sources they used (plus extra ones from news APIs), and asks an LLM to write its own verification report. 

### Motivation

I am curious to see how the AI-generated report compares against PolitiFact’s original verdict—seeing where they align, where they differ, and how reliable the LLM’s reasoning is.

### Current Status

🛠 **Work in progress**  Just getting started, so things are rough.

🚫 **Private repo, non-commercial** This is purely for experimentation.

⏳ **Updates?** Likely on weekends, whenever I have time.

### Additional Information

>[!NOTE]
>Due to content restrictions, the collected data cannot be shared in this repository. However, a sample instance is available [here](sample/)

This project fetches news from the following aggregators:
- **GNews** ([gnews.io](https://gnews.io/))
- **NewsAPI** ([newsapi.org](https://newsapi.org/))
- **APITube** ([apitube.io](https://apitube.io/))
- **TheNewsAPI** ([thenewsapi.com](https://thenewsapi.com/))

<hr>

#### Log

* March 16, 2025 : [~4.5 hrs] 
  * Start date.
  * Explored Project Ideas, and picked FactCheck+
  * Searched for Data sources, reused previous news api ingestion code.
  * Completed data collection pipeline. 
  * Collected 10 politifact claim checks:
    * [Pants on Fire: President Joe Biden’s immigration policy was “a giant voter importation scam.”](https://www.politifact.com/factchecks/2025/feb/21/elon-musk/fact-check-elon-musk-cpac-bidens-immigration-polic/)
    * [Pants on Fire: “We've never audited government for 100 years.”](https://www.politifact.com/factchecks/2025/feb/26/kevin-oleary/kevin-oleary-shark-tanks-mr-wonderful-says-no-gove/)
    * [False: “Tariffs are a tax cut for the American people.”](https://www.politifact.com/factchecks/2025/mar/13/karoline-leavitt/karoline-leavitt-says-tariffs-are-a-tax-cut-econom/)
    * [False: "Deceased InfoWars reporter Jamie White was on a 'Ukrainian enemies hit list'."](https://www.politifact.com/factchecks/2025/mar/14/alex-jones/infowars-reporter-jamie-white-who-was-fatally-shot/)
    * [Half True: “71 out of 72 Wisconsin counties filed lawsuits against Purdue Pharma. Brad Schimel refused to join them.”](https://www.politifact.com/factchecks/2025/mar/11/better-wisconsin-together/did-court-candidate-schimel-not-join-71-wisconsin/)
    * [Half True: “The single biggest driver of our national debt since 2001 has been Republican tax cuts.”](https://www.politifact.com/factchecks/2025/feb/25/patty-murray/are-republican-tax-cuts-the-single-biggest-driver/)
    * [Mostly True :“Under the previous administration … the cost of a median-price home in America more than doubled, and that was just in four years.”](https://www.politifact.com/factchecks/2025/mar/12/jd-vance/did-the-cost-of-buying-a-home-double-under-joe-bid/)
    * [Mostly True: "We’re one of the very few nations that allowed birthright citizenship.”](https://www.politifact.com/factchecks/2025/feb/04/ron-johnson/wis-sen-johnson-says-us-is-one-of-very-few-nations/)
    * [True: “After the referendum, Milwaukee Public Schools has a larger tax levy than the City of Milwaukee.”](https://www.politifact.com/factchecks/2025/mar/03/cavalier-johnson/mps-does-indeed-have-a-larger-tax-levy-than-the-ci/)
    * [True: “90% of the (school) districts in Wisconsin already have a policy” banning cellphones during class time."](https://www.politifact.com/factchecks/2025/feb/28/joel-kitchens/do-90-of-wisconsin-school-districts-ban-cellphones/)

    * Will not be sharing collected content due to content restrictions. Sample data item shared [here](data/sample/2d9a9d81-4774-48a8-9f7a-07bb2610333d.json)
