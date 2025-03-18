# FactCheck+ 🧐

FactCheck+ is a personal project to test how well LLMs can generate fact-checking reports given sources. It takes a claim that has already been fact-checked by [PolitiFact](https://www.politifact.com/), gathers the same sources they used (plus extra ones from news APIs), and asks an LLM to write its own verification report. 

### Motivation

I am curious to see how the AI-generated report compares against PolitiFact’s original verdict—seeing where they align, where they differ, and how reliable the LLM’s reasoning is.

### Current Status

🛠 **Work in progress**  Started writing the data processing pipeline

🚫 **Private repo, non-commercial** This is purely for experimentation.

⏳ **Updates?** Likely on weekends, whenever I have time.

### Additional Information

>[!NOTE]
>Due to content restrictions, the collected data cannot be shared in this repository. However, a sample instance is available [here](https://github.com/beingenfa/face-check-plus/blob/bc2dd8e76445db25157db477fe43248bde99752b/data/sample/2d9a9d81-4774-48a8-9f7a-07bb2610333d.json)

This project fetches news from the following aggregators:
- **GNews** ([gnews.io](https://gnews.io/))
- **NewsAPI** ([newsapi.org](https://newsapi.org/))
- **APITube** ([apitube.io](https://apitube.io/))
- **TheNewsAPI** ([thenewsapi.com](https://thenewsapi.com/))

<hr>

