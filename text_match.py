from transformers import BertTokenizer, BertModel
import torch
class match_model:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained("bert-base-uncased")

    def encode(self, text_list):
        model_inputs = self.tokenizer(text_list, padding=True, return_tensors="pt")
        return self.model(**model_inputs)["last_hidden_state"][:,0,:]

    def compute_cosine_similarity(self, tensor1, tensor2):
        return torch.cosine_similarity(tensor1, tensor2, dim=1)

    def plagiarism_detection(self, input_essay, reference):
        inp = [input_essay, reference]
        out = self.encode(inp) # 2 x dim
        tensor1,tensor2 = out[0].unsqueeze(0), out[1,:].unsqueeze(0)
        assert tensor1.shape == tensor2.shape
        score = self.compute_cosine_similarity(tensor1, tensor2).item()
        return score

    def question_retrieval(self, input_question, all_questions):
        inp = [input_question] + all_questions
        out = self.encode(inp)
        tensor1, tensor2 = out[0].unsqueeze(0), out[1:, :]
        if len(tensor2.shape) == 1:
            tensor2 = tensor2.unsqueeze(0)
        score = self.compute_cosine_similarity(tensor1, tensor2)
        max_idx = torch.argmax(score.unsqueeze(0))
        max_score = score[max_idx]
        return max_score, max_idx


if __name__ == "__main__":
    plagiarism_detection_threshold = 0.9
    question_retrieval_threshold = 0.9
    model = match_model()
    # test of plagiarism_detection
    input_essay = "Recent years have seen a tendency in China that tourism is growing faster. According to a recent survey made by some experts, about 47% urban residents travel regularly, and 28% rural residents also make their tour across the country. The survey also shows that more people are interested in tourism, and will join the army in the future. Facing this tendency, we can’t help exploring some underlying factors that are responsible. In the very first place, with the policy of reform and opening up, Chinese people’s living standard has been greatly improved, and therefore, most of them can afford to travel around. What’s more, it is believed that people now take a more positive attitude to tourism, and regard it as a life style. In addition, tourism facilities are becoming better and better. For example, transportation develops fast, and many scenic spots are available now."
    reference = "Recent years have seen a trend in China that tourism is growing faster. According to a recent survey made by some experts, about 47% urban residents travel regularly, and 28% rural residents also make their tour across the country. The survey also shows that more people are interested in tourism, and will join the army in the future. Facing this tendency, we can’t help exploring some underlying factors that are responsible. In the very first place, with the policy of reform and opening up, Chinese people’s living standard has been greatly improved, and therefore, most of them can afford to travel around. What’s more, it is believed that people now take a more positive attitude to tourism, and regard it as a life style. In addition, tourism facilities are becoming better and better. For example, transportation develops fast, and many scenic spots are available now."
    score = model.plagiarism_detection(input_essay, reference)
    if score > plagiarism_detection_threshold:
        print("抄袭")
    else:
        print("没有抄袭")
    # test of question_retrieval
    input_question = "To my great frustration, the computer I had ___ went wrong again."
    all_questions = ["To my great frustration, the computer I had ____ went wrong again.",
                     "Emergency line operators must always ____ calm and make sure that they get all the information they need to send help.",
                     "Even today I still remember the great fun we had ____ games on the beach on those happy days.",
                     "He was the first to enter the classroom the morning, ____ with him.",
                     "Although he is very busy every day as manager of the company, he spends as much time as he can ___ with his family.",
                     "Proper exercise is good ___ your health, and a scientific diet does good ___ you , too.",
                     "The dog seems very quiet now, but he still ___ go by.",
                     "____ going to take on your next visit to Beijing?",
                     "It is the first time he _____ in public.",
                     "Young people nowadays could not imagine what difficulty their fathers had ____ for a better life for their children.",
                     "___ it or not, his first attempt was a great success.",
                     "---Dad! Tom’s broken a glass!    --- ______. Accidents will happen.",
                     "He left home, ____ never ____ back again.",
                     "He wouldn’t accept the job. ____, he didn’t want to work in the charge of his father; _____, he wouldn’t like to work during the night.",
                     "I have been dreaming of ___ such a good chance for further education abroad, and now my dream has come true.",
                     "---Dane hasn’t arrived yet.     ---______? To my knowledge ,  he is a punctual person.",
                     "They examined again and again _____ any possible error might destroy the whole shuttle.",
                     "Pollution should by any means be stopped ____ the environment.",
                     "They asked me whether I’d like to ____ them in the discussion.",
                     "People in the village believed that he has died ____ they saw him in the flesh on the street.",
                     "After ____ in peace with no hunting, South China tigers will no longer be in danger of disappearing.",
                     "As the mid-term exam was drawing near, the teachers were busy ____ the test papers.",
                     "I think you’re old enough to know ____ to spend all your money on fancy goods.",
                     "I wish _____ no war, no poverty and no famine in the world. Everyone can enjoy their life.",
                     "He walked to work every day, the _____ his father had done."]
    score, idx = model.question_retrieval(input_question, all_questions)
    if score > question_retrieval_threshold:
        print(f"匹配到第{idx+1}个问题：{all_questions[idx]}")
    else:
        print("匹配失败")
