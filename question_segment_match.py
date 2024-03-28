
# all_questions = ["To my great frustration, the computer I had ____ went wrong again.",
#                  "Emergency line operators must always ____ calm and make sure that they get all the information they need to send help.",
#                  "Even today I still remember the great fun we had ____ games on the beach on those happy days.",
#                  "He was the first to enter the classroom the morning, ____ with him.",
#                  "Although he is very busy every day as manager of the company, he spends as much time as he can ___ with his family.",
#                  "Proper exercise is good ___ your health, and a scientific diet does good ___ you , too.",
#                  "The dog seems very quiet now, but he still ___ go by.",
#                  "____ going to take on your next visit to Beijing?",
#                  "It is the first time he _____ in public.",
#                  "Young people nowadays could not imagine what difficulty their fathers had ____ for a better life for their children.",
#                  "___ it or not, his first attempt was a great success.",
#                  "---Dad! Tom’s broken a glass!    --- ______. Accidents will happen.",
#                  "He left home, ____ never ____ back again.",
#                  "He wouldn’t accept the job. ____, he didn’t want to work in the charge of his father; _____, he wouldn’t like to work during the night.",
#                  "I have been dreaming of ___ such a good chance for further education abroad, and now my dream has come true.",
#                  "---Dane hasn’t arrived yet.     ---______? To my knowledge ,  he is a punctual person.",
#                  "They examined again and again _____ any possible error might destroy the whole shuttle.",
#                  "Pollution should by any means be stopped ____ the environment.",
#                  "They asked me whether I’d like to ____ them in the discussion.",
#                  "People in the village believed that he has died ____ they saw him in the flesh on the street.",
#                  "After ____ in peace with no hunting, South China tigers will no longer be in danger of disappearing.",
#                  "As the mid-term exam was drawing near, the teachers were busy ____ the test papers.",
#                  "I think you’re old enough to know ____ to spend all your money on fancy goods.",
#                  "I wish _____ no war, no poverty and no famine in the world. Everyone can enjoy their life.",
#                  "He walked to work every day, the _____ his father had done.",
#                  "Please introduce to native English speakers how to learn Chinese.",
#                  "Please introduce your hometown.",
#                  "Health is very important for all of us, but your parents are so busy with their work every day that they neglect this problem, I feel worried about them.Please write them a letter。",
#                  "Career or Family: which is more important?",
#                  "Please introduce tourism in China."]
# inp = [[[[34.0, 105.0], [51.0, 105.0], [51.0, 127.0], [34.0, 127.0]], ('a', 0.9815136)],
#        [[[34.0, 194.0], [238.0, 195.0], [238.0, 212.0], [34.0, 211.0]],
#         ('information they needy send help', 0.9265751)],
#        [[[202.0, 233.0], [265.0, 235.0], [264.0, 250.0], [201.0, 247.0]], ('become', 0.64928836)],
#        [[[34.0, 235.0], [77.0, 235.0], [77.0, 250.0], [34.0, 250.0]], ('a GROW', 0.6391508)],
#        [[[118.0, 236.0], [174.0, 236.0], [174.0, 250.0], [118.0, 250.0]], ('B.APPEAR', 0.8142995)],
#        [[[311.0, 232.0], [353.0, 235.0], [352.0, 252.0], [310.0, 249.0]], ('D.stY', 0.58184826)],
#        [[[32.0, 287.0], [48.0, 287.0], [48.0, 310.0], [32.0, 310.0]], ('a', 0.99644595)],
#        [[[29.0, 343.0], [542.0, 347.0], [542.0, 366.0], [29.0, 362.0]],
#         ('EventodayIstillrememberthegreatfunwehadgamesonthebeach on those', 0.93200076)],
#        [[[27.0, 381.0], [99.0, 383.0], [98.0, 401.0], [27.0, 399.0]], ('happydays.', 0.9388164)],
#        [[[27.0, 418.0], [69.0, 420.0], [68.0, 439.0], [26.0, 436.0]], ('APLAY', 0.648998)],
#        [[[114.0, 420.0], [175.0, 422.0], [174.0, 439.0], [114.0, 437.0]], ('into play', 0.885515)],
#        [[[198.0, 421.0], [260.0, 423.0], [259.0, 440.0], [197.0, 438.0]], ('C.PLAyINg', 0.5411011)],
#        [[[310.0, 421.0], [369.0, 423.0], [368.0, 441.0], [309.0, 439.0]], ('D.played', 0.89300543)],
#        [[[26.0, 474.0], [48.0, 474.0], [48.0, 498.0], [26.0, 498.0]], ('a', 0.9916881)],
#        [[[24.0, 533.0], [415.0, 537.0], [415.0, 554.0], [24.0, 550.0]],
#         ('Hewasthefirst to entertheclassroomthemorningwithhim.', 0.9562277)],
#        [[[25.0, 573.0], [287.0, 575.0], [286.0, 589.0], [25.0, 587.0]], ('ASUAL C.THAT I USUAL', 0.77699155)],
#        [[[323.0, 575.0], [415.0, 577.0], [415.0, 591.0], [322.0, 589.0]], ('D.WHATIS USUAL', 0.80450505)],
#        [[[25.0, 635.0], [38.0, 635.0], [38.0, 653.0], [25.0, 653.0]], ('a', 0.9869392)],
#        [[[20.0, 689.0], [219.0, 688.0], [219.0, 705.0], [20.0, 706.0]], ('Pleaseintroduceyourhometown.', 0.94524395)],
#        [[[9.0, 788.0], [186.0, 775.0], [188.0, 803.0], [11.0, 816.0]], ('and it such on fishy', 0.73457485)]]

import Levenshtein


def preprocess(s):
    return s.replace(" ", "").lower()

def levenshtein(s1, s2):
    return Levenshtein.distance(s1, s2)


def lcs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(l1 - 1, -1, -1):
        for j in range(l2 - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]


def jaccard_distance(s1, s2):
    return len(set(s1) & set(s2)) / len(set(s1) | set(s2))


def edit_distance(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            # print(dp)
            if i == n:
                dp[i][j] = m - j
            elif j == m:
                dp[i][j] = n - i
            else:
                d1 = 1 + dp[i + 1][j]
                d2 = 1 + dp[i][j + 1]
                d3 = dp[i + 1][j + 1] if s1[i] == s2[j] else 1 + dp[i + 1][j + 1]
                dp[i][j] = min(d1, d2, d3)
    return dp[0][0]


def get_y_distance(dot1, dot2):
    return abs(dot1[1] - dot2[1])


def get_x_distance(dot1, dot2):
    return abs(dot1[0] - dot2[0])


def get_distance(dot1, dot2):
    y_dis = get_y_distance(dot1, dot2)
    x_dis = get_x_distance(dot1, dot2)
    return x_dis, y_dis, (y_dis ** 2 + x_dis ** 2) ** 1 / 2


def judge(box1, box2):
    # print(box1)
    # print(box2)
    left_bottom1, right_bottom1, right_top1, left_top1 = box1
    centre_bottom1 = [(left_bottom1[0] + right_bottom1[0]) / 2, (left_bottom1[1] + right_bottom1[1]) / 2]
    # print(centre_bottom1)
    centre_top1 = [(left_top1[0] + right_top1[0]) / 2, (left_top1[1] + right_top1[1]) / 2]
    # print(centre_top1)
    left_bottom2, right_bottom2, right_top2, left_top2 = box2
    centre_bottom2 = [(left_bottom2[0] + right_bottom2[0]) / 2, (left_bottom2[1] + right_bottom2[1]) / 2]
    # print(centre_bottom2)
    centre_top2 = [(left_top2[0] + right_top2[0]) / 2, (left_top2[1] + right_top2[1]) / 2]
    # print(centre_top2)
    if centre_bottom2[1] > centre_top1[1] or centre_bottom1[1] > centre_top2[1]: # 两个框相差很远
        return False
    else:
        if (centre_bottom1[1] - centre_bottom2[1]) * (centre_top1[1] - centre_top2[1]) > 0: # 一个在上，一个在下
            y_list = sorted([centre_bottom1[1], centre_top1[1], centre_bottom2[1], centre_top2[1]])
            rate = abs(y_list[1] - y_list[2]) / abs(y_list[0] - y_list[3])
            # print(rate)
            if 0.5 < rate < 1:
                return True
            else:
                return False
        else: # 有交错
            return True
    # if (centre_bottom1[1] - centre_bottom2[1]) * (centre_top1[1] - centre_top2[1]) > 0 and (centre_bottom2[1] > centre_top1[1] or centre_bottom1[1] > centre_top2[1]):
    #     y_list = sorted([centre_bottom1[1], centre_top1[1], centre_bottom2[1], centre_top2[1]])
    #     rate = abs(y_list[1] - y_list[2]) / abs(y_list[0] - y_list[3])
    #     # print(centre_top2[1], centre_bottom1[1], centre_top2[1] - centre_bottom1[1])
    #     # print(centre_top1[1], centre_bottom1[1], centre_top1[1] - centre_bottom1[1])
    #     # rate = abs(centre_top2[1] - centre_bottom1[1]) / (centre_top1[1] - centre_bottom1[1])
    #     print(rate)
    #     if 0.7 < rate < 1:
    #         return True # 同一行
    #     else:
    #         return False
    # else:
    #     return True # 同一行


def get_question_answer(inp):
    # 拼接
    idx = 1
    new_inp = [inp[0]]
    while idx != len(inp):
        box1 = new_inp[-1]
        box2 = inp[idx]
        # print(box1[1][0])
        # print(box2[1][0])
        judge_result = judge(box1[0], box2[0])
        # print(judge_result)
        # print("----")
        if judge_result: # 同一行
            if box1[0][0][0] < box2[0][0][0]:
                combine_box = [box1, box2]
            else:
                combine_box = [box2, box1]
            new_inp.pop(-1)
            new_inp.append([[combine_box[0][0][0], combine_box[1][0][1], combine_box[1][0][2], combine_box[0][0][3]],(" ".join([combine_box[0][1][0], combine_box[1][1][0]]), 0.0)])
        else: # 不是同一行
            new_inp.append(box2)
        idx += 1
    inp = new_inp
    print(inp)
    centre = []
    for box in inp:
        dot = box[0]
        left_bottom, right_bottom, right_top, left_top = dot
        centre_dot = [(left_bottom[0] + right_top[0]) / 2, (left_bottom[1] + right_top[1]) / 2]
        centre.append(centre_dot)
    dis_threshold = 90
    print([get_distance(centre[i-1], centre[i])[1] for i in range(1, len(centre))])
    pre_y_dis_list = sorted([get_distance(centre[i-1], centre[i])[1] for i in range(1, len(centre))])
    # dis_threshold = (pre_y_dis_list[0] + pre_y_dis_list[-1]) / 2
    dis_threshold = 105
    print(dis_threshold)
    now = 0
    pre_dot = None
    now_dot = None
    question = []
    answer = []
    question_answer = []
    flag = None  # 0表示目前是连续的题目，1表示目前是连续的答案
    while now != len(centre):
        now_dot = centre[now]
        if now == 0:
            flag = 0
            question.append(inp[now][1][0])
            pre_dot = centre[now]
            now += 1
            continue
        x_dis, y_dis, dis = get_distance(now_dot, pre_dot)
        # print(inp[now][1][0])
        # print(y_dis)
        if y_dis < dis_threshold:
            if flag == 0:
                question.append(inp[now][1][0])
            else:
                answer.append(inp[now][1][0])
        else:
            flag = 1 - flag
            if flag == 0:  # 发现新的题目-答案对
                assert len(question) > 0 and len(answer) > 0
                question_str = " ".join(question)
                answer_str = " ".join(answer).lstrip().lstrip("answer").lstrip(":").lstrip()
                question_answer.append([question_str, answer_str])
                question = [inp[now][1][0]]
                answer = []
            else:
                answer.append(inp[now][1][0])
        pre_dot = centre[now]
        now += 1
    if len(question) > 0 and len(answer) > 0:
        question_str = " ".join(question)
        answer_str = " ".join(answer).lstrip().lstrip("answer").lstrip(":").lstrip()
        question_answer.append([question_str, answer_str])
    else:
        question_answer[-1][1] += " "+" ".join(question)
    return question_answer

def convertimg2problemanswer(inp, all_questions):
    question_answer = get_question_answer(inp)
    res = []
    for ques, answer in question_answer:
        preprocessed_ques = preprocess(ques)
        distances = [lcs(preprocessed_ques, preprocess(q)) / len(preprocessed_ques + preprocess(q)) for q in
                     all_questions]
        mx_idx = distances.index(max(distances))
        print('question:', ques)
        print('answer:', answer)
        print('matched: question', all_questions[mx_idx])
        print('-'*30)
        res.append([answer, mx_idx])
    return res

if __name__ == "__main__":
    question_answer = get_question_answer(inp)
    for ques, answer in question_answer:
        preprocessed_ques = preprocess(ques)
        print(preprocessed_ques)
        distances = [lcs(preprocessed_ques, preprocess(q)) / len(preprocessed_ques + preprocess(q)) for q in all_questions]
        print(distances)
        max_idx = 0
        max_dis = 0
        for idx, dis in enumerate(distances):
            if dis > max_dis:
                max_idx = idx
                max_dis = dis
        print(f"匹配到第{max_idx + 1}个问题：{all_questions[max_idx]}")
        print("----")
