from youtube_transcript_api import YouTubeTranscriptApi



link = 'https://www.youtube.com/watch?v=gjde39AslTo'
id = []

while link != '':
	link = input()
	id.append('')
	for i in range(len(link) - 1, -1, -1):
		if link[i] == '=' or link[i] == '/':
			break

		id[len(id) - 1] = link[i] + id[len(id) - 1]

del id[len(id) - 1]
print('video id is' + str(id))

# print(YouTubeTranscriptApi.get_transcripts(video_ids=id, language='ru'))

f = open('result.txt', 'w')

for k in range(len(id)):
	f.write('\tVIDEO #1\n\n')
	length = len(YouTubeTranscriptApi.get_transcripts(video_ids=id)[0][id[k]])

	for i in range(length):
		Done = False
		while not Done:
			string = YouTubeTranscriptApi.get_transcripts(video_ids=id)[0][id[0]][i]['text']
			for j in string:
				try:
					f.write(j)

				except:
					print('Couldn`t write {} symbol'.format(j))

			f.write('\n')
			Done = True
			print('String № ' + str(i + 1) + '/' + str(length) + ' written')

	f.write('=' * 20 + '\n')

f.close()
print('DONE, press ENTER to exit')
input()