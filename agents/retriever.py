
class RetrieverAgent:
    def retrieve(self, query):
        if query == "FAIL":
            raise Exception("Retriever Failed")

        return "Sample Data"
