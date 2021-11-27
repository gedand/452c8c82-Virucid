# Helper function to give back JSON for search
class JsonHelper:
    @staticmethod
    def search_to_json(u):
        files = {}
        num = 1

        # TODO: kommentek is menjenek hozzá
        for row in u:
            files[num] = {
                "caff": row.filename
            }
            num += 1
        return files
