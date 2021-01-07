# # import speech_recognition as sr
# # r = sr.Recognizer()
# # m = sr.Microphone()
# # try:
# #     print("a moment of silence, please")
# #     with m as source:r.adjust_for_ambient_noise(source)
# #     while True:
# #         print('listening')
# #         with m as source: audio = r.listen(source)
# #         try:
# #             value = r.recognize_google(audio)
# #             if str is bytes:
# #                 speech = format(value).encode("utf-8")
# #                 print("->}".format(value).encode("utf-8"))
# #                 print(speech)
# #             else:
# #                 speech = format(value)
# #                 print('->'.format(value))
# #         except sr.UnknownValueError:
# #             print("sorry didn't catch that")
# # except:
# #     print('unknown error')
# import speech_recognition as sr
#
# # get audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak:"
#     r.adjust_for_ambient_noise(source,duration=4)
#     audio = r.listen(source)
#     try:
#         print("You said " + r.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e   :
#         print("Could not request results; {0}".format(e))
from googlesearch import search
import webbrowser
query = 'play mirzapur netflix prime'
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
   # if "https://www.primevideo.com" or "https://www.netflix.com" in j:
    print(j)
    webbrowser.get('firefox').open_new_tab(j)
