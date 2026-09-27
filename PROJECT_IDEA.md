# Project Idea: Fictional Radio Catalogue

A small, Global Player–inspired API for a catalogue of fictional radio stations.
All content is fictional; this is not an official Global product.

## Current scope

### Entity

**Station**

| Field  | Notes                                           |
|--------|-------------------------------------------------|
| `id`   | Primary key                                     |
| `slug` | Unique, used in URLs (e.g. `beat-fm`)           |
| `name` | Display name (e.g. "Beat FM")                   |
| `genre`| e.g. "pop", "rock", "news"                      |

### Client questions (the API)

1. List all stations (paginated)
2. Get one station by slug
3. Create a station (validation, `201`, `409` on duplicate slug)

Each question is served by one shared service layer, exposed through both REST and GraphQL.

## Deliberate limits

- No users or authentication
- No audio or streaming
- No schedules or shows (yet)

## Possible later extension

- **Show** entity (title, presenter, weekday, start/end time) linked to a Station
- "What's on station X today?" and "What's on air now?"
