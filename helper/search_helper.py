# Helper function to give back JSON for search
class SearchHelper:
    @staticmethod
    def caff_files_to_json(u):
        files = {}
        num = 1

        for row in u:
            files[num] = {
                "image": row.img_location,
                "caff": row.caff_location
                }
            num+=1
        return files