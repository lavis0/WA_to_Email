# WA to Email and vice versa.

Welcome to the repo. This document is organised into Preface, Project Overview, and Implementation Notes.

## Preface
This chapter is to provide an overview of the project, at a glance, and to also provide some definitions for the rest of the document.

### Nomenclature
- A **User** is a unique individual that accesses a Client.
- A **Client** is a platform that the User interacts with, that abstracts calls to a Server instance.
- A **Server** is hosted on private company machines with particular exposed endpoints.
- A **DB** or **db** is an instance of a database that contains information relevant to the User.
- **WA** or **wa** is a messaging system that instances of User's use to interact with another User.

### TLDR
This project shows a holistic approach to how WA to Email could be handled. The priorities of this project were:
- To showcase a React-based app, using Server Components
- To showcase a microservices app with potential to vertically scale at many instances (how I imagine GRID would be utilised)
- To demonstrate how internal API calls are handled (via `server/commander.py`)
- To demonstrate a clear separation of concerns and logical flow

Limitations (projected):
- Does not handle encryption in a way that would be safe to use in production
- Does not expose endpoints ready for production, instead runs from CLI with a dev instance of the frontend
- Does not implement comprehensive error checking (if at all)
- Does not have a polished frontend

This project is to show a system design for a far less complicated system than the project I had proposed recently.

Its functionality could have been handled in a point-to-point fashion, but I chose to artificially increase the complexity so it more closely resembles a real system.

## Project Overview
I have tried to structure this project so that it is easy to understand the flow of internal and external API calls.

| Directory             | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| `client/next/`        | Root of the Next.js (React) frontend                            |
| `server/db/`          | Scripts to start an instance of the tables used in the app      |
| `server/crypt.py`     | Encryption and decryption pipeline, responds to `GET` with `POST` |
| `server/send.py`      | Handling of send to: WA, Email. `db` -> (en-)`crypt` -> `POST`  |
| `server/recieve.py`   | Moves incoming messages to Messages table.                      |
| `server/transform.py` | Essentially puts WA into email shape, takes email into WA shape |
| `server/app.py`       | The event handler.                                              |
 
## Implementation Notes
(1) The Server is implemented as a python module for ease of handling. Hence, `pyproject.toml` and a few extra files to meet the PyPI suggested module layout.
(2) 

## License
GNU GPLv3 because I want to see any forks of this project, even if it's a simple change :D