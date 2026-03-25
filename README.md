# AstroAnalysis Web App

A beginner-friendly Flask web app that:

- Accepts birth data (date, time, location)
- Calls an astrology API to get house chart info
- Uses Google Gemini AI to analyze the chart
- Returns a structured personality report rendered from Markdown

## Features

- Flask backend with modular classes (`Astro`, `AiAnswer`)
- AI integration via Google Gemini
- Markdown → HTML rendering for clean output
- Input validation and API error handling
- Styled forms and analysis cards

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/astro-analysis.git