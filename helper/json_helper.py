# Helper function to give back JSON for search
class JsonHelper:
    @staticmethod
    def search_to_json(u):
        files = {}
        num = 1

        for row in u:
            files[num] = {
                "image": row.img_location,
                "caff": row.caff_location
                }
            num+=1
        return files