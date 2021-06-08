import os
import io
from google.cloud import vision
import pandas as pd
# file_name = 'dog.jpeg'
# folder_path = r'/home/user/Desktop/moc/mysql/uploads'
# image_path = os.path.join(folder_path, file_name)
def gcp_reverse_image_search(filename):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"access_token.json"

    client = vision.ImageAnnotatorClient()
# def reverse_image_search():
    # filename = '琇花球_水平翻轉.jpg'
    folder_path = r'E:/ChainSecurity/combine2/testcase/'
    image_path = os.path.join(folder_path, filename)
    client = vision.ImageAnnotatorClient()
    
    search_results  = []
    full_match = []
    partial_match = []
    visually_match = []
    # full_match.append('full_match')
    # partial_match.append('partial_match')
    # visually_match.append('visually_match')
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
        print('read file')
    # construct an iamge instance
    image = vision.Image(content=content)
    response = client.web_detection(image=image)
    web_detection= response.web_detection

    # if web_detection.best_guess_labels:
    #     for label in web_detection.best_guess_labels:
    #         print('\nBest guess label: {}'.format(label.label))
    #         print(format(label.label))

    if web_detection.pages_with_matching_images:
        # print('\n{}Pages with matching images found:'.format(
        #     len(web_detection.pages_with_matching_images)
        # ))
        for page in web_detection.pages_with_matching_images:
            # print('\nPage  url:{}'.format(page.url))
            if page.full_matching_images:
                # print('{}Full Matches : '.format(
                #     len(page.full_matching_images)
                # ))
                for image in page.full_matching_images:
                    # print('Image Url : {}'.format(image.url))
                    print(image)
                    full_match.append(image.url)
            if page.partial_matching_images:
                # print('{} Partial Matches : '.format(
                #     len(page.partial_matching_images)
                # ))
                for image in page.partial_matching_images:
                    # print('Image Url : {}'.format(image.url))
                    partial_match.append(image.url)
    if web_detection.visually_similar_images:
        # print('\n{} visually similar image found:\n'.format(
        #     len(web_detection.visually_similar_images)
        #  ))
        for image in web_detection.visually_similar_images:
            # print('Image url : {}'.format(image.url))
            visually_match.append(image.url)
    # for i in range(0, 1, 3):
    #     for j in range(0, 1, 10):
    #         print()search_results[i][j]
    search_results.append(full_match)
    search_results.append(partial_match)
    search_results.append(visually_match)
    print(search_results)
    # if web_detection.web_entities:
    #      print('\n{} Web entities found: '.format(
    #         len(web_detection.web_entities)
    #      ))
    #      for entity in web_detection.web_entities:
    #          print('\n\t Score : {}'.format(entity.score))
    #          print(u'\t Description : {}'.format(entity.description))
    return search_results
# reverse_image_search()
