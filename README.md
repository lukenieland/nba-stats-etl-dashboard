# NBA Stats Scraper & Dashboard

This project combines data engineering, sports analytics, and interactive dashboards to explore NBA player performance over the last 25 years. Using Python for data collection and transformation, and Power BI for visual storytelling, I built a tool to analyze player trends, team performance, and league evolution from 2000 through 2025.

**Interactive Dashboard**:  [Explore the Power BI Dashboard](https://app.powerbi.com/groups/me/reports/6bd6e996-e5ee-403f-b4e8-5393fe444a33/cd42f6c69297499da3eb?experience=power-bi)

## Project Structure

 - main.py # Script to scrape and compile NBA stat
 - stats.csv # Generated dataset from the script (optional)
 - NBAStatsDashboard.pbix # Power BI dashboard built on the dataset
 - README.md # Project overview and usage

## Tools & Technologies
- **Python**: Web scraping (BeautifulSoup), data processing (pandas, Power Query)
- **Power BI**: Data modeling, interactive dashboard design
- **Data Source**: [Basketball-Reference.com](https://www.basketball-reference.com/) per-game player stats (2000–2025)

## Dashboard Features

| Feature | Description |
|--------|-------------|
| **Drilldowns** | Navigate by Team -> Year -> Position |
| **Top Performer Explorer** | Dynamic filters for PPG, AST, REB, and more |
| **Player Profiles** | Individual statistics for all players with filtering options |
| **Position Breakdown** | Compare stats across Guards, Forwards, and Centers |

## How To Use

Use the interactive link above ... OR:
1. Clone the repository.
2. Run `main.py` (uncomment HTML scraping block) to scrape and build the dataset.
3. Open the `.pbix` file in Power BI Desktop and connect to `stats.csv`.
4. Explore insights or customize visuals as needed.

## Skills Demonstrated
- End-to-end data pipeline creation (ETL)
- Web scraping & data cleansing
- Business intelligence design with Power BI
- Exploratory and descriptive analytics

## License
This project is open for educational and portfolio purposes. Data belongs to Basketball Reference.
