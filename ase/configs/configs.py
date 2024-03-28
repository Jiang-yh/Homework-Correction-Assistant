class Configs:
    FEATURES_PATH = r'D:\code\homework_viewer\mycode\ase\data\hand_crafted_v3.csv'
    READABILITY_PATH = r'D:\code\homework_viewer\mycode\ase\data\allreadability.pickle'
    POS_PATH = r"D:\code\homework_viewer\mycode\ase\data\pos_vocab.json"
    VOCAB_SIZE = 4000
    MAX_SENTLEN = 50
    MAX_SENTNUM = 97
    DROPOUT = 0.5
    CNN_FILTERS = 100
    CNN_KERNEL_SIZE = 5
    LSTM_UNITS = 100
    EMBEDDING_DIM = 50
    PRETRAINED_EMBEDDING = True
    EMBEDDING_PATH = r'D:\code\homework_viewer\mycode\ase\embeddings\glove.6B.50d.txt'
    DATA_PATH = r'D:\code\homework_viewer\mycode\ase\data\cross_prompt_attributes'
    EPOCHS = 50
    BATCH_SIZE = 10
    OUTPUT_PATH = 'outputs/'
