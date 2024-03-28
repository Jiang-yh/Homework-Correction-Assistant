from PIL import Image
import cv2

from paddleocr import PaddleOCR, draw_ocr
from ekphrasis.classes.spellcorrect import SpellCorrector
from question_segment_match import convertimg2problemanswer, lcs
from DBNet.dbnet.dbnet_infer import DBNET
from ase.ase_inference import Build_ase_model, Score_essay

def Load_models():
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", cls_model_dir='D:\code\homework_viewer\mycode\PaddleOCR\weights\ch_ppocr_mobile_v2.0_cls_train',
                    det_model_dir=r'D:\code\homework_viewer\mycode\PaddleOCR\weights\det\ch_ppocr_server_v2.0_det_train',
                    rec_model_dir=r'D:\code\homework_viewer\mycode\PaddleOCR\weights\rec\en_number_mobile_v2.0_rec_slim_train')  # need to run only once to download and load model into memory
    # sp = SpellCorrector(corpus="english")
    sp = SpellCorrector(corpus="coca", corpus_path='D:\code\homework_viewer\mycode\coca')
    dbnet = DBNET(MODEL_PATH="D:\code\homework_viewer\mycode\DBNet\models\dbnet.onnx")
    return ocr, sp, dbnet


def detect_homework(img_path, ocr_model, sp_model, db_model, save_path=None):

    d_res = ocr_model.ocr(img_path, cls=True, db_model=db_model)
    result = []
    for line in d_res:
        # print(' '.join([sp_model.correct(w) for w in line[1][0].split(' ')]), line[1][1])
        line[1] = (' '.join([sp_model.correct(w) for w in line[1][0].split(' ')]), line[1][1])
        result.append(line)

    if save_path is not None:
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf', drop_score=0.0)
        im_show = Image.fromarray(im_show)
        im_show.save(save_path)
    return result

if __name__ == '__main__':
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
                     "He walked to work every day, the _____ his father had done.",
                     "Please introduce to native English speakers how to learn Chinese.",
                     "Please introduce your hometown.",
                     "Health is very important for all of us, but your parents are so busy with their work every day that they neglect this problem, I feel worried about them.Please write them a letter。",
                     "Career or Family: which is more important?",
                     "Please introduce tourism in China."] + ["_____ is known to us all is that China has launched ShenZhou V spaceship successfully.", "_____ the Atlantic Ocean crosses the equator, the trade winds cause a flow of water to the west.","It’s impossible for all the people to get jobs because _____ of them are not fit for them.", "When will you leave for Paris for a visit? _____ next month.", "It was the training _____ he had at school that made him good jumper."]
    ocr, sp, dbnet = Load_models()
    inp = detect_homework(r'D:\code\homework_viewer\mycode\PaddleOCR\pics\jiangyuhao.jpg', ocr, sp, dbnet, 'result.jpg')
    question_answer = convertimg2problemanswer(inp, all_questions)
    # [[matched_question: 'his known thus a', detected_answer: 'what', idx_of_matched_question_in_all_questions: 30]]
    model, postag, configs = Build_ase_model(r"D:\code\homework_viewer\mycode\ase\saved_model\saved_weight")
    # essay = "When I was really patient when I wonti my pcar and mother to cook me some lazuge. I did not haved any of it scence my pass away is @DATE1. My mom had my @CAPS1  to cook @CAPS2 on my first birthday. when she cooked some for my first birthday party it was all goned. My @CAPS3 mother cooked @NUM1 pans of it. It was so good it was gone soon as she had put it out when I say soon I mean soon. I turned @NUM2 years old. My mother did it big for my birthday party. My mom died from open heart sergrey. She was @NUM3 years old. She had alto friends at her furnal. The furnal was very nice. But getting back to what I was writing about so In @DATE2 I asked my @CAPS1. To cook me some . She said ito me girl it coust to much to make it. I said @CAPS1 do you want me to gived you some money to cook the food, for me. She said no save your little money that you have. I said but @CAPS1 it s okay to take my money to buy my lazangae and cook it for me. She said girl what did I say. So I hurry up and put my money in my pocket. Then I was keeping it moving. When we got in the truck she said now @CAPS5 I am going to cook it for when I get some , more, money, and when I pay my bills. In @DATE3 she cooked me some. The day she cooked me some it was @CAPS6 @NUM4, @DATE3. My antyes came over a got some, my brother and sister got some, and my @CAPS1 and @CAPS8 got some. When they all wont I some I stood there and watch them get some, and when to stop getting some. Selfer when my @CAPS1 and @CAPS8 got some. I did not tell them when it was anoft because I live in they house. My brother and sister lives with them. The lanag only lasted for @NUM5 days and that it. When she cooked it I was happy. I brang it to school and ate it for my lunch."
    # print(Score_essay(model, postag, configs, essay))
    # print(question_answer)
    # answer, detected_answer, detected_answer_2 = 'after', 'affer', 'answerafter'
    # print(2*lcs(answer, detected_answer)/(len(answer)+len(detected_answer)))
    # print(2 * lcs(answer, detected_answer_2) / (len(answer) + len(detected_answer_2)))
