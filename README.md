# Ticket Analyzer
A machine learning-based ticket text analyzer that classifies provided text into queues (responsibilities) and priorities.

## Table of Contents
1. [Introduction](#introduction)
2. [Authors](#authors)
3. [Background](#background)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Further Information](#further-information)
7. [License](#license)

## Introduction
This project aims to automate the process of categorizing tickets into different queues and priorities based on their text content. The current implementation provides a web-based user interface for manual input, but it can be easily integrated into existing ticket systems.

## Authors
* [Lucas Roth (University of Würzburg)](https://github.com/Dherlou)
* Johannes Ruppel (Frankfurt University of Applied Sciences)

## Background
This project was created during a hackathon organized during the "KI-Konkret" convention of the ["Arbeitskreis IT-Strategie und Organisation" of the ZKI e.V.](https://www.zki.de/ueber-den-zki/arbeitskreise/arbeitskreis-it-strategie-und-organisation/).

## Getting Started
To set up the project, follow these steps:
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) on your system.
2. Ensure you have Python 3.12 or later installed.
3. Initialize the execution environment using the provided `environment.yaml` file:
```bash
conda env create -f environment.yaml
```
4. Activate the environment:
```bash
conda activate ticket-analyzer
```
5. Set up your OpenAPI-credentials: Copy the `settings.tmpl.yml` to `settings.yml` and fill out the fields with your personal credentials.

## Usage
1. Run `main.py` to spin up the web-based user interface.
2. Visit http://localhost:7860. (Sample Inputs can be found in the `inputs.txt`.)

## Further Information
Further information like opportunities and limitations can be found in the corresponding [Google Slide presentation](https://docs.google.com/presentation/d/1IaSUpkBniKGoKY7dxXPI23fodr6zc9HsiKsGO9fFzMs/edit?usp=sharing).

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.