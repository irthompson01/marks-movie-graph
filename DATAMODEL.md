# Movie Collection Data Model

## Overview
This data model represents Mark's extensive DVD/BluRay collection as a graph database using Neo4j. The model focuses on relationships between movies, people, and production entities while remaining simple yet comprehensive.

## Node Types

### Movie
**Properties:**
- `id`: String (UUID, unique identifier)
- `title`: String (required)
- `original_title`: String (for non-English titles)
- `release_year`: Integer (required)
- `runtime_minutes`: Integer
- `imdb_id`: String
- `tmdb_id`: String
- `synopsis`: String (long text)
- `format`: String (enum: DVD, BLURAY, UHD_BLURAY)
- `condition`: String (enum: MINT, EXCELLENT, GOOD, FAIR, POOR)
- `purchase_date`: Date
- `purchase_price`: Float
- `notes`: String (Mark's personal notes)
- `rating`: Float (personal rating 1-10)
- `watched`: Boolean (default: false)
- `watch_count`: Integer (default: 0)
- `last_watched`: Date
- `cover_image_url`: String

### Person
**Properties:**
- `id`: String (UUID, unique identifier)
- `name`: String (required)
- `birth_date`: Date
- `death_date`: Date
- `imdb_id`: String
- `tmdb_id`: String
- `biography`: String
- `photo_url`: String
- `notes`: String

### Genre
**Properties:**
- `id`: String (UUID, unique identifier)
- `name`: String (required, unique)
- `description`: String
- `tmdb_genre_id`: Integer

### ProductionCompany
**Properties:**
- `id`: String (UUID, unique identifier)
- `name`: String (required)
- `country`: String
- `founded_year`: Integer
- `imdb_id`: String
- `logo_url`: String
- `notes`: String

### Language
**Properties:**
- `id`: String (UUID, unique identifier)
- `name`: String (required)
- `code`: String (ISO 639-1, 2-letter code)
- `native_name`: String

### Country
**Properties:**
- `id`: String (UUID, unique identifier)
- `name`: String (required)
- `code`: String (ISO 3166-1 alpha-2)
- `native_name`: String

## Relationship Types

### Movie Relationships
- `DIRECTED_BY`: Movie → Person (directed relationship)
  - Properties: `credit_order`: Integer
- `ACTED_IN`: Person → Movie (acting relationship)
  - Properties: `character_name`: String, `credit_order`: Integer, `billing`: String
- `PRODUCED_BY`: Movie → Person (producer relationship)
  - Properties: `role`: String (Producer, Executive Producer, etc.), `credit_order`: Integer
- `WRITTEN_BY`: Movie → Person (writer relationship)
  - Properties: `credit_order`: Integer, `story_type`: String (Screenplay, Story, etc.)
- `CINEMATOGRAPHY_BY`: Movie → Person (cinematographer)
  - Properties: `credit_order`: Integer
- `EDITED_BY`: Movie → Person (editor)
  - Properties: `credit_order`: Integer
- `COMPOSED_BY`: Movie → Person (composer)
  - Properties: `credit_order`: Integer
- `BELONGS_TO_GENRE`: Movie → Genre
- `PRODUCED_BY_COMPANY`: Movie → ProductionCompany
  - Properties: `role`: String (Primary, Distributor, etc.)
- `ORIGINAL_LANGUAGE`: Movie → Language
- `COUNTRY_OF_ORIGIN`: Movie → Country
- `SPOKEN_LANGUAGE`: Movie → Language (for dubbed/subtitled versions)

### Person Relationships
- `BORN_IN`: Person → Country
- `DIED_IN`: Person → Country
- `WORKS_FOR`: Person → ProductionCompany (for recurring collaborations)

### Genre Relationships
- `SUBGENRE_OF`: Genre → Genre (hierarchical relationship)

## Graph Structure Examples

### Basic Movie Entry
```
(Movie {title: "The Godfather", release_year: 1972})
  -[:DIRECTED_BY]-> (Person {name: "Francis Ford Coppola"})
  -[:ACTED_IN {character_name: "Michael Corleone"}]-> (Person {name: "Al Pacino"})
  -[:BELONGS_TO_GENRE]-> (Genre {name: "Crime"})
  -[:BELONGS_TO_GENRE]-> (Genre {name: "Drama"})
  -[:PRODUCED_BY_COMPANY]-> (ProductionCompany {name: "Paramount Pictures"})
  -[:ORIGINAL_LANGUAGE]-> (Language {name: "English", code: "en"})
  -[:COUNTRY_OF_ORIGIN]-> (Country {name: "United States", code: "US"})
```

### Complex Relationships
- Actors can be connected to multiple movies
- Directors can have multiple films
- People can have multiple roles (actor + director)
- Movies can have multiple genres
- Production companies can produce multiple films
- Genres can have subgenres

## Query Examples

### Find all movies by a director
```
MATCH (p:Person {name: "Christopher Nolan"})-[:DIRECTED_BY]->(m:Movie)
RETURN m.title, m.release_year ORDER BY m.release_year DESC
```

### Find movies in a specific genre
```
MATCH (m:Movie)-[:BELONGS_TO_GENRE]->(g:Genre {name: "Science Fiction"})
RETURN m.title, m.release_year ORDER BY m.release_year DESC
```

### Find actor's filmography
```
MATCH (p:Person {name: "Leonardo DiCaprio"})-[:ACTED_IN]->(m:Movie)
RETURN m.title, m.release_year, m.rating ORDER BY m.release_year DESC
```

### Find movies with high personal ratings
```
MATCH (m:Movie)
WHERE m.rating >= 8 AND m.watched = true
RETURN m.title, m.rating, m.notes ORDER BY m.rating DESC
```

This model provides a robust foundation for tracking Mark's collection while allowing for rich relationship queries and visualization of the movie network.
