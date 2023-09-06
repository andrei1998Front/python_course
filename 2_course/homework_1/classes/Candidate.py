class Candidate():
    def __init__(self, obj):
        self.name = obj["name"]
        self.position = obj["position"]
        self.picture = obj["picture"]
        self.skills = obj["skills"]

    def get_skills_string(self):
        return ', '.join(self.skills)
