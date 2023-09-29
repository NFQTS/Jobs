# Need to match people to jobs
# Filtering based on interest, skill, and depth of skill makes sense
# Need a differentiator but... that should be easy due to the way I run things we are already different by being proactive.
# Will probably need a neural network or adapt a recommendation system to it.
# May have to get wild and assign scores to each job for each candidate based on tons of metrics but idk.

#job_sites = ["LinkedIn", "GitHub", "Indeed", "Monster Jobs", "GlassDoor", "Dice Jobs", "SimplyHired", "Seekr", "Stack Overflow", "CareerJet", "Adzuna", "Neuvoo",
            #"Authentic Jobs", "We Work Remotely", "Remote OK"]

#api_dict = {}

# Seems like a lot of these services have restricted API access, most likely to prevent losing placement fees.
# Best bet to start with seems like the google cloud talent solutions (cant remember name, its something like that)
# Google is a little confusing to connect to so going to have to scope documentation to figure it out.

class JobCandidate:
    def __init__(self, candidate_id, name, contact_info, employment_history, skills, strengths, weaknesses, resume, cv, interests, references=None):
        self.candidate_id = candidate_id  # Unique ID for the candidate
        self.name = name
        self.contact_info = contact_info  # This could be a dictionary with email, phone, LinkedIn, etc.
        self.employment_history = employment_history  # List of dictionaries with job details
        self.skills = skills  # List of skills
        self.strengths = strengths  # List of strengths
        self.weaknesses = weaknesses  # List of weaknesses
        self.resume = resume  # File path or link to the resume
        self.cv = cv  # File path or link to the CV
        self.interests = interests  # List of interests or hobbies
        self.references = references or []  # List of reference contacts

    def match_with_job(self, job_requirements):
        # Implement matching logic here, comparing candidate's skills with job requirements
        matched_skills = [skill for skill in self.skills if skill in job_requirements['skills']]
        
        # You can define your matching criteria based on the job requirements
        
        return matched_skills

    def display_info(self):
        # Display candidate information in a structured format
        print(f"Candidate ID: {self.candidate_id}")
        print(f"Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")
        print("Employment History:")
        for job in self.employment_history:
            print(f"  - {job['position']} at {job['company']} ({job['start_date']} - {job['end_date']})")
        print(f"Skills: {', '.join(self.skills)}")
        print(f"Strengths: {', '.join(self.strengths)}")
        print(f"Weaknesses: {', '.join(self.weaknesses)}")
        print(f"Interests: {', '.join(self.interests)}")
        if self.references:
            print("References:")
            for reference in self.references:
                print(f"  - Name: {reference['name']}, Contact: {reference['contact']}")

# Example usage:
candidate_data = {
    "candidate_id": 1,
    "name": "John Doe",
    "contact_info": {"email": "johndoe@example.com", "phone": "+1234567890"},
    "employment_history": [
        {"position": "Software Engineer", "company": "Tech Inc.", "start_date": "2020-01-01", "end_date": "2022-12-31"},
        {"position": "Data Analyst", "company": "Data Co.", "start_date": "2018-05-01", "end_date": "2019-12-31"}
    ],
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "strengths": ["Problem Solving", "Teamwork"],
    "weaknesses": ["Public Speaking", "Time Management"],
    "resume": "https://example.com/johndoe_resume.pdf",
    "cv": "https://example.com/johndoe_cv.pdf",
    "interests": ["Hiking", "Reading"],
    "references": [
        {"name": "Jane Smith", "contact": "janesmith@example.com"},
        {"name": "Bob Johnson", "contact": "bobjohnson@example.com"}
    ]
}

john_doe = JobCandidate(**candidate_data)
john_doe.display_info()
