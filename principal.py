import json

class EvaluateComments():

    def get_json(self, filename):
        with open(filename, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object

    def get_score(self, is_positive, is_negative, emphasis):
        multiplier = 1 if is_positive else -1
        return emphasis * multiplier

    def get_comment_disposition(self, score):
        disposition = "neutral"
        if score > 0:
            disposition = "positive"
        elif score < 0:
            disposition = "negative"
        return disposition


if __name__ == "__main__":
    ec = EvaluateComments()
    feedback = ec.get_json('feedback.json')
    keywords = ec.get_json('keywords.json')
    pos_neg_keywords = [k for k in keywords if k["is_neutral"] is False]

    for f in feedback:
        comment = f.get("comment")
        score = 0
        for k in pos_neg_keywords:
            if k.get("keyword") in comment.lower():
                score += ec.get_score(k.get("is_positive"), k.get("is_negative"), k.get("emphasis"))
        disposition = ec.get_comment_disposition(score)
        print(f"\nOn {f.get('date')} {f.get('first_name')} {f.get('last_name')} had a {disposition} experience. "
              f"Score: {score}")





