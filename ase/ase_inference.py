import os
import time
import argparse
import random
import numpy as np
import json
from .configs.configs import Configs
from .models.CTS import build_CTS
from .utils.data_utils import get_feature
from .utils.general_utils import get_scaled_down_scores, pad_hierarchical_text_sequences, get_attribute_masks
from .custom_layers.zeromasking import ZeroMaskedEntries
from .custom_layers.attention import Attention

def Build_ase_model(weight_path):
    fake_input = "When I was really patient when I wonti my pcar and mother to cook me some lazuge. I did not haved any of it scence my pass away is @DATE1. My mom had my @CAPS1  to cook @CAPS2 on my first birthday. when she cooked some for my first birthday party it was all goned. My @CAPS3 mother cooked @NUM1 pans of it. It was so good it was gone soon as she had put it out when I say soon I mean soon. I turned @NUM2 years old. My mother did it big for my birthday party. My mom died from open heart sergrey. She was @NUM3 years old. She had alto friends at her furnal. The furnal was very nice. But getting back to what I was writing about so In @DATE2 I asked my @CAPS1. To cook me some . She said ito me girl it coust to much to make it. I said @CAPS1 do you want me to gived you some money to cook the food, for me. She said no save your little money that you have. I said but @CAPS1 it s okay to take my money to buy my lazangae and cook it for me. She said girl what did I say. So I hurry up and put my money in my pocket. Then I was keeping it moving. When we got in the truck she said now @CAPS5 I am going to cook it for when I get some , more, money, and when I pay my bills. In @DATE3 she cooked me some. The day she cooked me some it was @CAPS6 @NUM4, @DATE3. My antyes came over a got some, my brother and sister got some, and my @CAPS1 and @CAPS8 got some. When they all wont I some I stood there and watch them get some, and when to stop getting some. Selfer when my @CAPS1 and @CAPS8 got some. I did not tell them when it was anoft because I live in they house. My brother and sister lives with them. The lanag only lasted for @NUM5 days and that it. When she cooked it I was happy. I brang it to school and ate it for my lunch."
    configs = Configs()
    # create_feature
    with open(configs.POS_PATH, "r") as f:
        pos_tag = json.load(f)
    fake_sample = {'essay_id': '19159', 'prompt_id': '7', 'score': '16', 'content': 5, 'organization': 4, 'style': 4,
                   'conventions': 3}
    fake_sample['content_text'] = fake_input
    X_pos, X_linguistic_features, X_readability, Y = get_feature(fake_sample, pos_tag, configs)
    # build model
    model = build_CTS(len(pos_tag), configs.MAX_SENTNUM, configs.MAX_SENTLEN,
                      X_readability.shape[1],
                      X_linguistic_features.shape[1],
                      configs, Y.shape[1])
    model.load_weights(weight_path)
    return model, pos_tag, configs

def Score_essay(model, pos_tag, configs, essay):
    trait = ['score', 'content', 'organization', 'word_choice', 'sentence_fluency', 'conventions', 'prompt_adherence',
             'language', 'narrativity']
    sample = {'essay_id': '19159', 'prompt_id': '7', 'score': '16', 'content': 5, 'organization': 4, 'style': 4,
                   'conventions': 3}
    sample['content_text'] = essay
    X_pos, X_linguistic_features, X_readability, Y = get_feature(sample, pos_tag, configs)
    output = np.array(model([X_pos, X_linguistic_features, X_readability]) * 100)
    score = dict(zip(trait, output.tolist()[0]))
    return score
    # print(json.dumps(result, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    essay = "When I was really patient when I wonti my pcar and mother to cook me some lazuge. I did not haved any of it scence my pass away is @DATE1. My mom had my @CAPS1  to cook @CAPS2 on my first birthday. when she cooked some for my first birthday party it was all goned. My @CAPS3 mother cooked @NUM1 pans of it. It was so good it was gone soon as she had put it out when I say soon I mean soon. I turned @NUM2 years old. My mother did it big for my birthday party. My mom died from open heart sergrey. She was @NUM3 years old. She had alto friends at her furnal. The furnal was very nice. But getting back to what I was writing about so In @DATE2 I asked my @CAPS1. To cook me some . She said ito me girl it coust to much to make it. I said @CAPS1 do you want me to gived you some money to cook the food, for me. She said no save your little money that you have. I said but @CAPS1 it s okay to take my money to buy my lazangae and cook it for me. She said girl what did I say. So I hurry up and put my money in my pocket. Then I was keeping it moving. When we got in the truck she said now @CAPS5 I am going to cook it for when I get some , more, money, and when I pay my bills. In @DATE3 she cooked me some. The day she cooked me some it was @CAPS6 @NUM4, @DATE3. My antyes came over a got some, my brother and sister got some, and my @CAPS1 and @CAPS8 got some. When they all wont I some I stood there and watch them get some, and when to stop getting some. Selfer when my @CAPS1 and @CAPS8 got some. I did not tell them when it was anoft because I live in they house. My brother and sister lives with them. The lanag only lasted for @NUM5 days and that it. When she cooked it I was happy. I brang it to school and ate it for my lunch."
    # output = main(input)
    model, postag, configs = Build_ase_model("saved_model/saved_weight")
    print(Score_essay(model, postag, configs, essay))