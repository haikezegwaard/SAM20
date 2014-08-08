import slumber

class NikiConverter:
    oauth_token = "90302891-25b2-43cb-8ef9-3dd4bc0955be"
    def __init__(self):
        #https://api.niki.nl/projects/54/AMVHUUR/AMVGEN_0179C52C-111E-4A3A-8CD7-8EE5965DA0D7?oauth_token=90302891-25b2-43cb-8ef9-3dd4bc0955be
        self.api = slumber.API("https://api.niki.nl")

    def getProject(self):
        self.result = self.api.projects(54).get(oauth_token=self.oauth_token)
        return self.result