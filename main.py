from youtube_transcript_api import YouTubeTranscriptApi

id = []

print('Insert links')
link = input()
while link != '':
    id.append('')
    for i in range(len(link) - 1, -1, -1):
        if link[i] == '=' or link[i] == '/':
            break

        id[len(id) - 1] = link[i] + id[len(id) - 1]

    link = input()

print('video id are ' + str(id))

f = open('result.txt', 'w')

for k in range(len(id)):
    f.write(f'\tVIDEO #{k + 1}\n\n')
    subs = YouTubeTranscriptApi.get_transcripts(video_ids=id)[0][id[k]]

    for i in range(len(subs)):
        Done = False
        while not Done:
            string = subs[i]['text']
            for j in string:
                try:
                    f.write(j)
                except:
                    print('Couldn`t write {} symbol'.format(j))

            f.write('\n')
            Done = True
            print('String № ' + str(i + 1) + '/' + str(len(subs)) + ' written')

    f.write('=' * 20 + '\n')

f.close()
print('DONE, press ENTER to exit')
input()
