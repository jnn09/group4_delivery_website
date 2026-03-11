# TIW Web App

Flask web application for TIW ordering system.

## Setup Instructions
Prerequisites: have github desktop installed, then restart your code editor. type 'git --version' to check install.  

1. Clone the repository

git clone https://github.com/jnn09/group4_delivery_website.git  
cd group4_delivery_website

2. Create virtual environment

python -m venv venv

3. Activate virtual environment

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Run the app, in the terminal, run the command to debug

flask --app app --debug run

Then open the link that appeard in the terminal:  

http://127.0.0.1:5000
