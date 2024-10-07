
# Reimann Sum

## Overview

Welcome to the **Reimann Sum** project repository! This project is written in Python and is used to calculate area underneath of a curve. To help make it run on your computer, we will use something called a virtual machine. If you do not know what that is, it is like an isolated part on your computer which can have it's own versions of things and it will not affect the rest of your machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3**: Download the latest version from [Python's official website](https://www.python.org/downloads/).

## Setup Instructions

Follow these steps to get the project up and running on your machine.

### Step 1: Clone the Repository

1. Clone this repository using Git, or download it as a ZIP file and extract it.
   
   **Using Git**:
   ```bash
   git clone <repository-url>
   cd Reimann-Sum` 

### Step 2: Create a Virtual Environment

2.  Set up a virtual environment to isolate the project dependencies.
    
   - On **Windows**:
       ```bash
       python -m venv venv 
       venv\Scripts\activate
   - On **macOS/Linux**: 
        ```bash
        python3 -m venv venv
        source venv/bin/activate
### Step 3: Install Dependencies

3.  Once the virtual environment is activated, install the required dependencies using the `requirements.txt` file.
    
    `pip install -r requirements.txt` 
    

### Step 4: Running the Project

4.  With the environment set up and dependencies installed, you can run the project. Ensure the virtual environment is still activated.
   
    `python main.py` 
    

### Step 5: Deactivate the Virtual Environment

5.  After you're done working with the project, deactivate the virtual environment by typing: 
    
    `deactivate`
    
## Troubleshooting

### PowerShell Execution Policy on Windows

If you encounter an error when trying to activate the virtual environment on Windows using PowerShell, you may need to temporarily change your execution policy.

1.  Open **PowerShell as Administrator** and run:
    
    `Set-ExecutionPolicy RemoteSigned` 
