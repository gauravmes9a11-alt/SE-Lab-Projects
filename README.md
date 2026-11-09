# Software Engineering Lab Projects

Lab work for the **Software Engineering** course at PES University, covering requirements engineering, Agile planning, architecture, static analysis, coverage-driven testing and fuzz testing.

Labs 1–3 build up a single running case study, the **Alumni Mentorship & Mock Interview Platform** (Problem Statement #06, Campus & Academic Operations). Lab 4 is a Pygame game project that lives in its own repository. Labs 5–7 are hands-on code quality and testing exercises in Python.

---

## Table of Contents

- [Lab Index](#lab-index)
- [Lab Summaries](#lab-summaries)
- [Repository Structure](#repository-structure)
- [Tools and Technologies](#tools-and-technologies)
- [Getting Started](#getting-started)
- [Running the Code Labs](#running-the-code-labs)
- [Author](#author)

---

## Lab Index

| Lab | Topic | Type | Folder |
|---|---|---|---|
| **1** | Requirements Engineering & UML Use-Case Modelling | Report (PDF) | [Lab 1](./Lab%201/) |
| **2** | Agile Backlog Creation & Sprint Simulation in Jira | Report (PDF) | [Lab 2](./Lab%202/) |
| **3** | Component Modelling & Architectural Pattern Selection | Report (PDF) + UML diagram | [Lab 3](./Lab%203/) |
| **4** | Meteor Dodge: adding features to a Pygame game | Python project (separate repo) | [38-meteor-dodge](https://github.com/gauravmes9a11-alt/38-meteor-dodge) |
| **5** | Static Code Analysis (Pylint, Flake8, Bandit) | Python + tool reports | [Lab 5](./Lab%205%20-%20Static%20Code%20Analysis/) |
| **6** | Code and Branch Coverage | Python + pytest suites | [Lab 6](./Lab%206%20-%20Code%20and%20Branch%20Coverage/) |
| **7** | Fuzz Testing | Python + Hypothesis tests | [Lab 7](./Lab%207%20-%20Fuzz%20Testing/) |

> Lab 4 is hosted in its own repository rather than a folder here. Follow the link in the table above.

---

## Lab Summaries

### Lab 1: Requirements Engineering & UML Use-Case Modelling
Defines the problem context for the Alumni Mentorship & Mock Interview Platform, with five functional requirements (FR-001 to FR-005) and two non-functional requirements (NFR-001, NFR-002). Each requirement has an ID, description, priority, measurable acceptance criteria and rationale. The actors are the **Student Mentee** and the **Alumni Mentor**, and the report includes the use-case model.

### Lab 2: Agile Backlog & Sprint Simulation (Jira)
Turns the Lab 1 requirements into a Scrum backlog in Jira (project key `AM`). The work covers five epics, user stories, prioritisation, Fibonacci story-point estimation, two simulated sprints, burndown charts and a written reflection.

### Lab 3: Component Modelling & Architecture
Selects a **Layered Architecture** for the platform and justifies it on separation of responsibilities, maintainability, security and performance. The UML component diagram is included as an image.

- **Presentation layer:** User Interface
- **Business layer:** Authentication Service, Mentor Matching Service, Booking Manager, Calendar & Notification Service, Scorecard Manager
- **Data layer:** Platform Database

### Lab 4: Meteor Dodge
A space-survival arcade game built with **Python** and **Pygame**. Starting from a basic meteor-dodging game, the lab adds these features:

- Laser firing with `SPACE`
- Large meteors that split into two fragments when destroyed
- Shield orbs that absorb one meteor collision each, and stack
- A score multiplier that rises every 10 seconds of uninterrupted survival and resets when a shield absorbs a hit
- Meteors that spawn faster over time

The repository includes `Before.mp4` and `After.mp4` gameplay demos, a controls table and a manual testing checklist. To play it:

```bash
git clone https://github.com/gauravmes9a11-alt/38-meteor-dodge.git
cd 38-meteor-dodge
python -m pip install -r requirements.txt
python main.py
```

### Lab 5: Static Code Analysis
Runs **Pylint**, **Flake8** and **Bandit** on `tournament_scoreboard.py`, a tournament scoreboard with league statistics and SCP publishing, then fixes every finding.

| Tool | Before | After |
|---|---|---|
| Pylint | 4.75 / 10 | 10.00 / 10 |
| Flake8 | Formatting violations (E203, E231, E261, E302) | Clean |
| Bandit | 4 issues (1 High, 1 Medium, 2 Low) | 0 issues |

Main fixes: hardcoded password moved to an environment variable, insecure temp file replaced with `NamedTemporaryFile`, shell command replaced with `subprocess.run`, `random` replaced with `secrets.choice`, mutable default argument removed, docstrings added, and names converted to snake_case. See [`issues.md`](./Lab%205%20-%20Static%20Code%20Analysis/issues.md) for the full table and the raw `*_before.txt` / `*_after.txt` reports.

### Lab 6: Code and Branch Coverage
Tests an elevator dispatch module (`next_direction`, `door_action`, `pick_elevator`) with two pytest suites, one targeting statement coverage and one targeting branch coverage. Both reach **100%** (39 statements, 28 branches). Coverage report screenshots are in the `screenshots/` folder.

### Lab 7: Fuzz Testing
Extends the elevator module with input-parsing functions (`parse_request`, `total_travel`, `load_percent`) and fuzzes them with **Hypothesis**. Fuzzing exposed crashes in the original application. The fixed version validates input and raises a clean `ValueError`. Screenshots of the original failures, the fixed application and the passing fuzz runs are in the `screenshots/` folder.

---

## Repository Structure

```text
SE-Lab-Projects
│
├── Lab 1/
│   └── PES1UG24AM104_Lab1_Project_Report.pdf
├── Lab 2/
│   └── PES1UG24AM104_Lab2_Project_Report.pdf
├── Lab 3/
│   ├── PES1UG24AM104_Lab3_Report.pdf
│   └── PES1UG24AM104_uml_diagram.png
├── Lab 4 → hosted separately: github.com/gauravmes9a11-alt/38-meteor-dodge
├── Lab 5 - Static Code Analysis/
│   ├── tournament_scoreboard.py
│   ├── issues.md
│   ├── bandit_before.txt / bandit_after.txt
│   ├── pylint_before.txt / pylint_after.txt
│   └── flake8_before.txt / flake8_after.txt
├── Lab 6 - Code and Branch Coverage/
│   ├── elevator_dispatch.py
│   ├── CodeCoverageTest_elevator_dispatch.py
│   ├── BranchCoverageTest_elevator_dispatch.py
│   └── screenshots/
├── Lab 7 - Fuzz Testing/
│   ├── elevator_dispatch.py
│   ├── test_elevator_dispatch.py
│   └── screenshots/
├── README.md
└── .gitignore
```

---

## Tools and Technologies

| Tool | Used for |
|---|---|
| Git / GitHub | Version control and hosting |
| Jira (Scrum) | Backlog and sprint simulation (Lab 2) |
| UML | Use-case and component modelling (Labs 1, 3) |
| Python 3 | Lab 4, 5, 6 and 7 code |
| Pygame | Game development (Lab 4) |
| Pylint, Flake8, Bandit | Static analysis (Lab 5) |
| pytest, pytest-cov | Unit testing and coverage (Lab 6) |
| Hypothesis | Property-based fuzz testing (Lab 7) |

---

## Getting Started

### Prerequisites

- Git
- Python 3.9 or newer (for Labs 5–7); Lab 4 needs Python 3.10+ and Pygame
- A PDF viewer (for the Lab 1–3 reports)

### Clone the repository

```bash
git clone https://github.com/gauravmes9a11-alt/SE-Lab-Projects.git
cd SE-Lab-Projects
```

---

## Running the Code Labs

Install the dependencies once:

```bash
pip install pytest pytest-cov hypothesis pylint flake8 bandit
```

**Lab 5: Static analysis**

```bash
cd "Lab 5 - Static Code Analysis"
pylint tournament_scoreboard.py
flake8 tournament_scoreboard.py
bandit tournament_scoreboard.py
```

The scoreboard reads the referee password from the `REFEREE_PASSWORD` environment variable, so set it before using the publishing feature.

**Lab 6: Coverage**

The test files are not named `test_*.py`, so pass them to pytest explicitly:

```bash
cd "Lab 6 - Code and Branch Coverage"
pytest CodeCoverageTest_elevator_dispatch.py --cov=elevator_dispatch --cov-report=term-missing
pytest BranchCoverageTest_elevator_dispatch.py --cov=elevator_dispatch --cov-branch --cov-report=term-missing
```

**Lab 7: Fuzz testing**

```bash
cd "Lab 7 - Fuzz Testing"
pytest -v
python elevator_dispatch.py   # interactive demo
```

---

## Author

**Gaurav Shivakumar**
PES1UG24AM104 · B.Tech Computer Science (AI/ML), PES University, Bengaluru
