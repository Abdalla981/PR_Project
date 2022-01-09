from preprocessing.CaptionsCleaning import CaptionsCleaning
from training.DatasetProcessor import DatasetProcessor

'''
This script loads the dataset and pre-processes it and writes the clean dataset captions to a new file.
The new dataset captions and corresponding images are loaded and their info is printed
'''
if __name__ == '__main__':
    captions_path = 'dataset/Captions3.txt'
    images_path = 'embedding/efficientNet'
    new_captions_path = 'dataset/CaptionsClean3.txt'
    
    if input('Clean Dataset?(y/n) ') == 'y':
        clean_obj = CaptionsCleaning(captions_path)
        clean_obj.clean_dataset()
        clean_obj.save_captions_to_file(new_captions_path)
    
    process_obj = DatasetProcessor(new_captions_path, images_path, 'B0')
    process_obj.process_dataset()
    process_obj.print_dataset_info()
    process_obj.print_sample_of_sequences()
    