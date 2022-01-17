from testing.EvaluateModel import EvaluateModel
from training.MergeModel import MergeModel
from training.DatasetProcessor import DatasetProcessor, Dataset
from keras.preprocessing.text import Tokenizer

'''
This script trains a merge model using the mergeModel, DatasetProcessor and EvaluateModel classes.
'''

if __name__ == '__main__':
    images_path = 'dataset/memes3'
    image_embeddings_path = 'embedding/efficientNet'
    train_captions_path = 'dataset/CaptionsClean3_train.txt'
    test_captions_path = 'dataset/CaptionsClean3_test.txt'
    embeddings_path = 'embedding/glove/captionsGlove.pkl'
    model_folder_path = 'models/Test/'
    model_name = 'Merge-model-B0-ep002-loss5.801-val_loss49.877.h5'
    gen_output = 'Meme_drawer/Model_generated/Test/'

    if input('Evaluate Model?(y/n) ') == 'y':
        train_obj = Dataset(train_captions_path)
        captions_list = train_obj.captions_to_list()
        test_dp_obj = DatasetProcessor(test_captions_path, image_embeddings_path, 'B0', embeddings_path)
        test_dp_obj.process_dataset(captions_list)
        model_obj = MergeModel(model_folder_path, test_dp_obj, init=False, model_name=model_name)
        eval_obj = EvaluateModel(model_obj, images_path, k=5, num=25)
        eval_obj.save_captions()
        eval_obj.save_evaluation()
        eval_obj.show_generated_examples(output_folder_path=gen_output, num=20)
        