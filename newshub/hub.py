from newshub.utils import Utils
from newshub.hn_scraper import HNScraper

class Hub:

    utils = None

    # store a run name here, or have a "makerun" function
    
    def __init__(self, workFolder):
        print("----------------------------------------")
        self.utils = Utils(workFolder)
        self.utils.makeTimePoint("hub")
        self.utils.log("hub", "Initializing hub...")
        
    def __del__(self):
        try:
            self.utils.dumpLogs()
        except: print("@ WARNING! - deconstructor failed.")
        print("========================================")

    def getHNScraper(self):
        scraper = HNScraper(self.utils)
        return scraper
