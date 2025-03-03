# Reference Hybrid System Designs

## Table of Contents
1. [Introduction](#introduction)
2. [Reference Design Overview](#reference-design-overview)
3. [Getting Started](#getting-started)
3. [Developers Guide](#developers-guide)

## Introduction
This repository is intended to house reference hybrid system designs created at NREL. We hope that by hosting these designs on a public repository we will encourage and facilitate collaboration on these designs so they can be improved and refined through external input and use. If you are interested in using these designs, we hope you find them useful and ask that you properly reference this repository. If you are interested in contributing, please following the developers guide provided below.

## Reference Design Overview

| ID | Region (detail) | Product | Grid connection | Land-based technology | Offshore technology |
|-|-|-|-|-|-|
| 01 | Minnesota | Steel | Yes (ore and steel tech only) | Wind, solar (pv), battery storage, electrolysis, hydrogen storage (rock cavern), iron ore refining, steel production | N/A |
| 02 | Texas | Ammonia | Yes (ammonia tech only) | Wind, solar (pv), battery storage, electrolysis, hydrogen storage (salt cavern), ammonia production| N/A |
| 03 | Texas (gulf coast) | Hydrogen | No | Solar (pv), battery storage, electrolysis, hydrogen storage (salt cavern) | Wind (fixed foundation) |
| 04 | New York Bight | Hydrogen | No | Solar (pv), battery storage, electrolysis, hydrogen storage (rock cavern) | Wind (fixed foundation) |
| 05 | California | Hydrogen | No | Solar (pv), battery storage, electrolysis, hydrogen storage (rock cavern) | Wind (floating foundation) |

## Getting Started
You will need to clone this repository and set up any software packages you wish to use to run the reference designs. Software is not included in this repository.

### Organization
You will find files for the reference designs organized as follows:
- Run scripts for using the reference design with a specific software package: `reference-systems/<##-region-product>/<software-name>/`
- Input files for using the reference design with a specific software package: `reference-systems/<##-region-product>/<software-name>/input-files/`
- Supporting documentation, such as pdf files: `reference-systems/<##-region-product>/doc/`
- Tests: `tests/test-<##-region-product>/test-<software-name>.py` 

## Developers Guide

### Forking the Repository

1. Navigate to the [repository homepage](https://github.com/NREL/ReferenceHybridSystemDesigns).
2. Click the **Fork** button in the upper-right corner to create a personal copy of the repository under your GitHub account.

### Cloning Your Fork

1. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/your-username/ReferenceHybridSystemDesigns.git
   ```
2. Navigate into the cloned directory:
   ```bash
   cd ReferenceHybridSystemDesigns
   ```

### Making Changes

1. **Create a New Branch**: For each new change, create a separate branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Add or Update Files**: Make your changes to the reference files as needed.

3. **Commit Your Changes**: Commit your changes with a clear, descriptive message:
   ```bash
   git add .
   git commit -m "Add/update reference file for [specific purpose]"
   ```

4. **Push Your Changes**: Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

### Adding Tests

- **Test Files**: If your changes involve adding or modifying files that could benefit from automated tests (e.g., validation scripts for file formats), include test files in the `tests/` directory within the repository (see [Organization](#organization)).
  
- **Test Instructions**: Add instructions for running tests in a `README.md` or a `TESTING.md` file if appropriate. Ensure your tests are clear, reproducible, and relevant to the changes made.

### Creating a Pull Request

1. Go to your repository on GitHub.
2. Click the **Compare & pull request** button next to your branch.
3. Provide a detailed description of the changes you made, including any relevant context and test results.
4. Submit the pull request.

### Review and Merge Process

- **Review**: Repository maintainers will review your pull request, check for any issues, and provide feedback if necessary.
- **Merge**: Once approved, your changes will be merged into the main branch.

### Code of Conduct

We strive to maintain a positive and respectful community.

--
ChatGPT was used to assist in development of this document
