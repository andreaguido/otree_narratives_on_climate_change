# Narratives on Climate Change

An oTree experiment designed to elicit and study how people reason about climate change — their causal narratives, policy preferences, media consumption habits, and willingness to act.

## Overview

This survey experiment was developed for online deployment via [Prolific](https://www.prolific.com/). Participants are presented with factual information about climate change and then asked to articulate their personal causal explanations, policy proposals, and attitudes across a series of structured questionnaire pages.

The study is conducted by researchers at Paris School of Business and the University of Montpellier (France). Contact: a.guido@psbedu.paris

## Survey Structure

The experiment (`climate_questionnaire` app) follows this page sequence:

| Page | Description |
|---|---|
| Presentation | Participant information statement and consent |
| NarrativeElicitation_text | Presents factual information about climate change |
| NarrativeElicitation_question | Elicits participant's causal narrative (min. 50 words) |
| NarrativeElicitation_question_certain | Confidence in the narrative provided |
| Circadian | Anti-bot verification page |
| NarrativeSharing | Multiple Price List (MPL) to measure willingness to share the narrative |
| Policy | Participant's preferred policy solution (min. 25 words) |
| Policy_question_certain | Confidence in the policy proposal |
| Policy_expectations | Expected effects of the policy on the economy, climate, and household |
| ClimateKnowledge | Self-assessed knowledge and energy source ranking task |
| MediaConsumption | Frequency of news consumption and media source usage |
| ClimateExpectations | Expected consequences of climate change (droughts, sea levels, migration, etc.) |
| ClimateConcern | Willingness to adopt pro-environmental behaviors |
| Demographics | Income and education |
| End | Redirects Prolific participants to completion URL |

## Key Features

- **Narrative elicitation**: Open-text fields with minimum word count validation
- **Incentivized task**: Multiple Price List (MPL / BDM mechanism) to elicit willingness to share narratives; 10 randomly selected participants per session receive a payoff
- **Multilingual**: English and French support (configurable via `LANGUAGE_CODE` in `settings.py`)
- **Prolific integration**: Handles participant routing, consent opt-out ("Request return"), and redirect links
- **Auto-fill mode**: `fill_auto` session config flag for automated testing

## Tech Stack

- [oTree](https://www.otree.org/) `5.11.4`
- Python
- PostgreSQL (`psycopg2`)
- Deployed on **Heroku** (see `Procfile`)

## Setup

### Local development

```bash
pip install -r requirements.txt
otree devserver
```

### Environment variables

| Variable | Description |
|---|---|
| `OTREE_ADMIN_PASSWORD` | Admin panel password |
| `DATABASE_URL` | PostgreSQL connection string (Heroku sets this automatically) |

### Heroku deployment

The `Procfile` configures a two-process setup:

```
web:    otree prodserver1of2
worker: otree prodserver2of2
```

Push to Heroku with:

```bash
git push heroku main
```

## Session Configuration

Edit `SESSION_CONFIGS` in `settings.py` to configure:

```python
dict(
    name='only_climate_change',
    app_sequence=['climate_questionnaire'],
    num_demo_participants=1,
    prolific=True,          # enables Prolific-specific UI (opt-out button, redirect)
    url_validate="",        # Prolific completion URL
    url_return=""           # Prolific return URL
)
```

Set `fill_auto=True` to enable automatic form completion for testing.

## Language

Set `LANGUAGE_CODE` in `settings.py` to `'en'` (English) or `'fr'` (French).
