Resume and Job Description Matcher or Shortlister
This application uses the uagents library and the agentverse.ai server to short-list a given set resumes for a particular job description. 
The tkinter modules was used to create the User-Interface for this application. 
The NLTK and spacy libraries are used to conduct the comparisons of the job description and resumes

The "ui2.py" module takes the file names of job description and resumes from the users and stores in th directory jds and resumes respectively.Module "pdfconvs.py" converts the resumes in pdf format and saves in .txt format in text_resumes directory.The "agent_input.py" contains an aget which reads the jds and resumes in .txt format as strings and sends it to the resume matching agent in  the module "JD.py" .The "JD.py" module comares the job description and resumes by natural language processing and returns the top 2 matches for resumes and percentage similarity 
