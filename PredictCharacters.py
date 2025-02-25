import SegmentCharacters
import pickle
import subprocess
#print("Loading model")
filename = './finalized_model.sav'
model = pickle.load(open(filename, 'rb'))
classification_result = []
for each_character in SegmentCharacters.characters:
    each_character = each_character.reshape(1, -1);
    result = model.predict(each_character)
    classification_result.append(result)
plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]
column_list_copy = SegmentCharacters.column_list[:]
SegmentCharacters.column_list.sort()
rightplate_string = ''
for each in SegmentCharacters.column_list:
    rightplate_string += plate_string[column_list_copy.index(each)]

# detectplate = subprocess.Popen(['python', 'DetectPlate.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# segmentCharacters = subprocess.Popen(['python', 'SegmentCharacters.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# trainRecognizeCharacters = subprocess.Popen(['python', 'TrainRecognizeCharacters.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# subprocess.Popen(['python', 'DetectPlate.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# subprocess.Popen(['python', 'SegmentCharacters.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# subprocess.Popen(['python', 'TrainRecognizeCharacters.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#print proc.communicate()[0]
print('License plate')
print(rightplate_string)